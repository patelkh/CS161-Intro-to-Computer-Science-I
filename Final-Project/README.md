Write a class called FourLetterBoard that represents the board for a two-player game that is played on a 4x4 grid. This class does not do everything needed to play a game - it just takes care of the logic for the game board. A turn consists of placing one of the four letters A-D on an empty space of the board. Your class does not keep track of whose turn it is, so it will allow multiple moves by the same player consecutively (things like keeping track of player turn, reading input from the user, and displaying output would belong in another class, but you don't have to worry about that).

If you split the board in half both horizontally and vertically, it separates the board into four 2x2 "regions". The winner is the one who plays the last letter in a row, column, or region that now contains one of each letter - regardless of who played the other letters. A player cannot put a letter in a row, column, or region if the **opponent** has already played that letter in that row, column, or region. Otherwise, a player may duplicate a letter.

The class should have the following **private** data members: a representation of the board, and the current state, which holds one of the three following values: "X_WON", "O_WON", "DRAW", or "UNFINISHED". 

It should have an init method that initializes the board to being empty, initializes the current_state to "UNFINISHED", and appropriately initializes any other data members. Tip: Probably the easiest way of representing the board is to use a list of lists.  The init method could then initialize the board to a list of 4 lists, each of which contains 4 empty strings (or whatever character you want to use to represent an empty space).

It should have a get method named get_current_state, which returns the current state.

It should have a method named make_move that takes four parameters - the row and the column (in that order) of the square being played on, the letter being played there, and either 'x' or 'o' to indicate the player making the move. If the game has already been won or drawn, or if the square is not empty, or if the letter duplicates an opponent letter in the same row, column, or region, make_move should just **return False**. Otherwise, it should record the move, update the current state, and **return True**. To update the current state, you need to detect if this move causes a win for either player, or a draw. A draw occurs when the board is full, but neither player has won.

It's not required, but you'll probably find it useful for testing and debugging to have a method that prints out the board.

Whether you think of the list indices as being [row][column] or [column][row] doesn't matter as long as you're consistent.

As a very simple example, your class could be used as follows:
```
board = FourLetterBoard()
board.make_move(0,0,'B','o')  # The o player places a B in one of the corners
board.make_move(3,3,'D','o')  # The o player places a D in the opposite corner
print(board.get_current_state())
```
Your file must be named: FourLetterBoard.py
