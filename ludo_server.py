from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='templates/static')
socketio = SocketIO(app, async_mode='threading', transport='websocket')
CORS(app, origins=['http://localhost:5000'])

STATE = {}

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

@socketio.on('join')
def on_join(data):
    room_id = data['room_id']
    session_url = data['session_url']
    username = data['username']
    colour = data['colour']
    c = colour[0]
    # join_room(room)
    print(f'{username} joined the room: {room_id}')
    emit('message', {'message': f'{username} joined the room'}, room_id=room_id)

    # Initialize game state for the room if not already done
    if room_id not in STATE:
        STATE[room_id] = {
            "game_state": "waiting",
            "turn": colour,
            "players": [colour],
            colour: {"tokens": [f'c{c}01', f'c{c}02', f'c{c}03', f'c{c}04']}
        }

@socketio.on('take_turn')
def on_take_turn(data):
    room_id = data['room_id']
    # Implement your game logic to process the player's action
    # Update the game state accordingly
    # For example, you can update the position of the token, etc.
    # Then emit the updated game state to all players in the room
    emit('update_game_state', {'game_state': STATE[room_id]}, room_id=room_id)

if __name__ == '__main__':
    socketio.run(app, debug=True)
