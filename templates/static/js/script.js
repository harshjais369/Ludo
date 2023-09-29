const socket = io('https://organic-guide-j77p6rjwq45fj56-5000.app.github.dev:5000');
const TOKEN_PATHS = {
  red: ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15',
  'c16', 'c17', 'c18', 'c19', 'c20', 'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30',
  'c31', 'c32', 'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c39', 'c40', 'c41', 'c42', 'c43', 'c44', 'c45',
  'c46', 'c47', 'c48', 'c49', 'c50', 'c51', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'],
  green: ['c14', 'c15', 'c16', 'c17', 'c18', 'c19', 'c20', 'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27',
  'c28', 'c29', 'c30', 'c31', 'c32', 'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c39', 'c40', 'c41', 'c42',
  'c43', 'c44', 'c45', 'c46', 'c47', 'c48', 'c49', 'c50', 'c51', 'c52', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6',
  'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'cg1', 'cg2', 'cg3', 'cg4', 'cg5'],
  blue: ['c40', 'c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48', 'c49', 'c50', 'c51', 'c52', 'c1',
  'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16', 'c17',
  'c18', 'c19', 'c20', 'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30', 'c31', 'c32',
  'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'cb1', 'cb2', 'cb3', 'cb4', 'cb5'],
  yellow: ['c27', 'c28', 'c29', 'c30', 'c31', 'c32', 'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c39', 'c40',
  'c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48', 'c49', 'c50', 'c51', 'c52', 'c1', 'c2', 'c3', 'c4',
  'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16', 'c17', 'c18', 'c19', 'c20',
  'c21', 'c22', 'c23', 'c24', 'c25', 'cy1', 'cy2', 'cy3', 'cy4', 'cy5']
}

const cells = document.querySelectorAll('.cell');
var currPosX = 0;
var currPosY = 0;
var currCellId = 'c0';
movePointerRecursive('red', 'rpt1', -1, 5); // Test

// Function to move the player pointer to a specific cell
function movePointerToCell(pointerId, cell) {
  const player = document.getElementById(`${pointerId}`);
  const cellRect = cell.getBoundingClientRect();
  const playerRect = player.getBoundingClientRect();
  const deltaX = cellRect.left - playerRect.left;
  const deltaY = cellRect.top - playerRect.top;
  // deltaX/Y + {num} ; num = pointer display offset
  currPosX += (deltaX + 10);
  currPosY += (deltaY + 10);
  player.style.transform = `translate(${currPosX}px, ${currPosY}px)`;
}

function movePointerRecursive(colour, pointerId, currCell, destCell) {
  if (destCell == -1) {
    alert(`${colour[0]}home${pointerId[3]}`);
    var cl = document.getElementById(`${colour[0]}home${pointerId[3]}`);
    movePointerToCell(pointerId, cl);
    // Need to modify
    currCellId = cl.getAttribute('id');
  }
  else if (currCell < destCell) {
    positions = TOKEN_PATHS[colour];
    var cl = document.getElementById(positions[currCell + 1]);
    movePointerToCell(pointerId, cl);
    // Need to modify
    currCellId = cl.getAttribute('id');
    setTimeout(() => {
      movePointerRecursive(colour, pointerId, currCell + 1, destCell);
    }, 300); // Delay b/w cell movements
  }
}

function loadGame(diceNumber, turn) {
  pass;
}

// Should be called after auth
function authCurrPlayer() {
  // Send page url to server
  // If url registered, it'd send "game state" & "current player's info" with "page url" as id to current player
  // else game spectator
  // Anyone with "this" page url, will be considered "this" player
  var sessionUrl = window.location.search;
  if (sessionUrl) {
    sessionUrl = sessionUrl.substring(1);
    // Send request to server
    skt_sendAuthRequest(sessionUrl);
  } else {
    // If no url params, then show error
    alert('Error: Invalid URL');
  }
}

// Add click event listeners to each cell
cells.forEach((cell) => {
  cell.addEventListener('click', function () {
    var dest_cell_id = cell.getAttribute('id');
    // Need to modify
    var i_currCell = bpath.indexOf(currCellId);
    var i_destCell = bpath.indexOf(dest_cell_id);
    // var tmp_path = bpath;
    // tmp_path.splice(0, tmp_path.indexOf(currCellId));
    // alert(tmp_path);

    movePointerRecursive(i_currCell, i_destCell);
  });
});




// Have to modify the following funcs below
function rollDice() {
  var randomNumber = Math.floor(Math.random() * 6) + 1;
  alert(randomNumber);
  return randomNumber;
}

function movePiece(piece, diceNumber) {
  piece.position += diceNumber;
}

function isWinner(piece) {
  return piece.position === 6;
}

var pieces = [
  {
    color: "red",
    position: 1,
  },
  {
    color: "green",
    position: 1,
  },
  {
    color: "yellow",
    position: 1,
  },
  {
    color: "blue",
    position: 1,
  },
];

var currentPlayer = 0;

function updateGame() {
  var diceNumber = rollDice();
  var piece = pieces[currentPlayer];
  movePiece(piece, diceNumber);

  if (isWinner(piece)) {
    alert("Player " + piece.color + " has won!");
  } else {
    currentPlayer = (currentPlayer + 1) % 4;
  }
}

window.onload = authCurrPlayer;

// Send request to server
function skt_sendAuthRequest(sessionUrl) {
  socket.emit('authRequest', { sessionUrl: sessionUrl }, (response) => {
    // If response is true, then load game
    if (response) {
      loadGame(response.diceNumber, response.turn);
    } else {
      // Else, show error
      alert('Error: Invalid URL');
    }
  }, 1000, 3, true);
}

// Receive response from server
socket.on('authResponse', (response) => {
  if (response) {
    // If response is true, then load game
    loadGame(response.diceNumber, response.turn);
  } else {
    // Else, show error
    alert('Error: Invalid URL');
  }
});

