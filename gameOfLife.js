/*
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician 
John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying dthe above rules simultaneously to every cell in the current state of the m x n grid board. 
In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.
*/

/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function (board) {
  const rows = board.length;
  const cols = board[0].length;
  const copyBoard = JSON.parse(JSON.stringify(board));
  const directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
  ];

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      let liveNeighbors = 0;
      for (const [x, y] of directions) {
        const newI = i + x;
        const newJ = j + y;
        if (newI >= 0 && newI < rows && newJ >= 0 && newJ < cols) {
          if (copyBoard[newI][newJ] === 1) {
            liveNeighbors++;
          }
        }
      }
      if (copyBoard[i][j] === 1) {
        if (liveNeighbors < 2 || liveNeighbors > 3) {
          board[i][j] = 0;
        }
      } else {
        if (liveNeighbors === 3) {
          board[i][j] = 1;
        }
      }
    }
  }
};

// test case:
let board = [
  [0, 1, 0],
  [0, 0, 1],
  [1, 1, 1],
  [0, 0, 0]
];
gameOfLife(board);
console.log(board); // [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

board = [
  [1, 1],
  [1, 0]
];
gameOfLife(board);
console.log(board); // [[1,1],[1,1]]
