-------------------------------------------------------------
--------------- WORD SEARCH PUZZLE RULES ---------------------
--------------------------------------------------------------

Object 

In the Word Search Puzzle game, the player finds hidden 
words on a not-static board full of letters. All the 
words on the board are related to a subject.


Run the game

Run in the terminal:

>$      make run

Setup

To select the subject of the board, introduce the name 
of the subject. A set of 10 words is placed on a board 
of dimensions 10 x 10.

Gameplay

1. After selecting the subject, the game starts automatically.
2. The board and the list of words to find are displayed.
3. Each row can rotate horizontally and each column can rotate
	vertically to form words.
4. To rotate the board write on the command line the following 
	instruction:
			> rotate

   	The direction of the rotation will be asked. To specify, 
   	write on of the following options:
   			[up, down, left, right]

	The number of the column or row (according to the direction
	 selected) will be ask. To specify it, type the number. 
	 Only integers are valid, the minimum number is 1 and the
	 maximum number is the size of row or the column.

5. The words are placed horizontally or vertically. The words
	are never placed backwards.
6. To find a word on the board, type the following instruction:
			> find

	The initial and the final cell will be ask. Type the 
	numbers corresponding to their column and row. The numbers
	must be integers and must be inside the board.
7. To display the instructions type the following command:
			> help

8. Ending the game: the game ends when all the words of the 
	list are found.  To end the game before finding all the 
	words, type the following command:
			> exit

