from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit, join_room
from flask_cors import CORS
import funcs

app = Flask(__name__, template_folder='templates', static_folder='templates/static')
socketio = SocketIO(app, async_mode='threading', transport='websocket')
CORS(app)

# Game state for all rooms
STATE = {}
SESSION_URLS = {} # Session URL of each player

def get_next_turn(room_id):
    if "turn" not in STATE[room_id]:
        STATE[room_id]["turn"] = "red"
    else:
        current_turn = STATE[room_id]["turn"]
        players = ["red", "green", "yplayer", "bplayer"]
        next_turn_index = (players.index(current_turn) + 1) % len(players)
        STATE[room_id]["turn"] = players[next_turn_index]

    return STATE[room_id]["turn"]

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('A user connected!')

@socketio.on('disconnect')
def on_disconnect():
    print('A user disconnected!')

@socketio.on('authRequest')
def on_auth_user(data):
    session_url = data['session_url']
    if session_url in SESSION_URLS:
        # The player has joined a room before (player mode)
        room_id, colour = SESSION_URLS[session_url]
        emit('authResult', {'status': 'passed', 'session_url': session_url, 'room_id': room_id, 'colour': colour}, to=request.sid)
        emit('updateGameState', {'game_state': STATE[room_id]}, to=room_id)
    elif funcs.getSessionData(session_url) is not None:
        room_id = funcs.getSessionData(session_url)['room_id']
        # The session URL is valid but the player has not joined any room (spectator mode)
        join_room(room_id)
        if room_id not in STATE:
            STATE[room_id] = {
                "game_state": "waiting",
                "turn": None,
                "players": []
            }
        emit('authResult', {'status': 'passed', 'session_url': session_url, 'room_id': room_id, colour: None}, to=request.sid)
        emit('updateGameState', {'game_state': STATE[room_id]}, to=request.sid)
    else:
        # The session URL is abused (e.g. modified by the user)
        emit('authResult', {'status': 'failed', 'session_url': session_url, 'room_id': None}, to=request.sid)

@socketio.on('join')
def on_join(data):
    session_url = data['session_url']
    data = funcs.getSessionData(session_url)
    if data is None:
        emit('authResult', {'status': 'failed', 'session_url': session_url, 'room_id': None}, to=request.sid)
        return
    room_id = data['room_id']
    username = data['username']
    colour = data['colour']
    c = colour[0]
    if len(STATE[room_id]['players'] < 1): # Initialize game state for the room if not already done
        STATE[room_id] = {
            "game_state": "waiting",
            "turn": colour,
            "players": [colour],
            colour: {"tokens": [f'c{c}01', f'c{c}02', f'c{c}03', f'c{c}04']}
        }
    elif (colour not in STATE[room_id]["players"]) and (STATE[room_id]['game_state'] == 'waiting'):
        STATE[room_id]["players"].append(colour)
        STATE[room_id][colour] = {"tokens": [f'c{c}01', f'c{c}02', f'c{c}03', f'c{c}04']}
    else:
        # Colour already choosen by someone else or the game has been started already
        return
    # Register the player's session URL
    SESSION_URLS[session_url] = (room_id, colour)
    emit('joinResult', {'status': 'passed', 'session_url': session_url, 'room_id': room_id, 'colour': colour}, to=request.sid)
    emit('updateGameState', {'game_state': STATE[room_id]}, room_id=room_id)
    if (len(STATE[room_id]['players'] >= 4)):
        # Room is full, start the game
        pass

@socketio.on('takeTurn')
def on_take_turn(data):
    room_id = data['room_id']
    # Implement your game logic to process the player's action
    # Update the game state accordingly
    # For example, you can update the position of the token, etc.
    # Then emit the updated game state to all players in the room
    emit('updateGameState', {'game_state': STATE[room_id]}, room_id=room_id)

if __name__ == '__main__':
    socketio.run(app, debug=True)
