const socket = io();

// Example of joining a room and sending a message
socket.emit('join', { username: 'Player1', room: 'room1' });

// Example of taking a turn and sending game state updates
// socket.emit('take_turn', { room: 'room1' });

// Listen for game state updates
// socket.on('update_game_state', (data) => {
//     const updatedGameState = data.game_state;
//     // Update your frontend UI with the updated game state
// });

// Handle updating the list of players
socket.on('update_players', (data) => {
    const players = data.players;
    const playersList = document.getElementById('playersList');
    playersList.innerHTML = '<h2>Players:</h2>';
    for (const sid in players) {
        const color = players[sid];
        const playerDiv = document.createElement('div');
        playerDiv.innerHTML = `${color} player`;
        playersList.appendChild(playerDiv);
    }
});

// Simulate updating the list of players (remove this in actual implementation)
const mockPlayers = {
    'player1': 'red',
    'player2': 'green',
    'player3': 'yellow'
};
setTimeout(() => {
    socket.emit('update_players', { players: mockPlayers });
}, 3000);