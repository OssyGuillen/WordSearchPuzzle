from random import shuffle, randint, sample
from string import ascii_uppercase


commands = ["help","exit","rotate","word","initial"]
direction = ["right","left","up","down"]
messages = {"incorret_word":"The word is not on the list", 
			"found_word":"You already found this word",
			"good_word":"Congratulations! You just find a word",
			"welcome":"WORD SEARCH PUZZLE",
			"winner":" is the winner",
			"win": "Congratulations! You won",
			"highscore": "NEW HIGHSCORE",
			"wrong_direction": "That is an invalid direction. Only 'right', 'left', 'up', 'down' are possible",
			"invalid_cell": "That cell is not inside the board",
			"insert_direction": "Direction: ",
			"insert_row_number": "Row number: ",
			"insert_column_number": "Column number: "}


def display_initial_message():
# Displays the name of the game and a welcome message
# Version 1.0
	pass

def display_menu():
# Displays the menu with the options:
# Single Player
# Multi Player
# Instructions
# Exit
# Version 1.0
	pass

def display_single_player_modes():
# Version 1.0
	pass

def get_player_nickname():
	pass

def start_game():
	pass

def setup():
	pass

def exit_game():
	pass


class Player:
# Version 1.0
	def __init__(self, nickname):
		self.nickname = nickname
		self.clue = None

	def set_clue(self, clue):
		''' Set a created clue into the player's clue. 

		Parameters:
		----------
			clue: BySolution(Clue)
				A clue object

		'''
		pass

class Board:
# Version 1.0

	def __init__(self):
		self.original_grid = [[]]
		self.current_grid = [[]]
		self.rows = 10
		self.columns = 10

	def build (self, words):
		''' Add to the board all the words given and fill the 
			blanks spaces left with random letters 

		Parameters:
		----------
			words: [string]
				An array with the words.

		'''
		self.current_grid = [['' for x in range(10)] for y in range(10)]
		num_words = len(words)
		words.sort(key=len)
		words.reverse()
		cols = [0,1,2,3,4,5,6,7,8,9]
		rows = [0,1,2,3,4,5,6,7,8,9]
		for word in words:
			added = False
			while not added:
				position = randint(0,1) # 0 is row, 1 is column.
				if position and len(cols) > 0:
					num = sample(cols,1)[0]
					added = self.add_word_into_row(num,word)
					if added:
						cols.remove(num)
				elif not position and len(rows) > 0:
					num = sample(rows,1)[0]
					added = self.add_word_into_column(num,word)
					if added:
						rows.remove(num)
		self.fill()

		# Copy the built list.
		self.original_grid = []
		for row in self.current_grid:
			self.original_grid.append(list(row))

	def restart_board(self):
	# Restart the board to its original state
		pass

	def rotate(self, number, direction):
	# Rotates either the column or the row
	# TYPE OF DIRECTION?
		pass

	def display(self):
	# Prints the grid
		pass

	def is_valid_cell(self,row,column):
	# The cell is inside the board
		pass

	def can_generate_a_word(self,row1,column1,row2,column2):
	# The cells form a line where it is possible to find a word
		pass

	def get_word(self,row1,column1,row2,column2):
		pass

	def add_word_into_row(self, row, word):
		''' Insert a word into a row of the board. 

		Parameters:
		----------
			row: integer
				The number of the row.
			word: string
				The word to be inserted.

		'''
		column = randint(0,9)
		aux_column = column
		# Checking the posibility to add the word
		for letter in word:
			if aux_column > 9:
				aux_column = 0
			if self.current_grid[row][aux_column] != '':
				if self.current_grid[row][aux_column] != letter:
					return False
			aux_column += 1
		# Adding the word.
		for letter in word:
			if column > 9:
				column = 0
			if self.current_grid[row][column] == '':
				self.current_grid[row][column] = letter
			column += 1
		return True

	def add_word_into_column(self, column, word):
		''' Insert a word into a column of the board. 

		Parameters:
		----------
			column: integer
				The number of the column.
			word: string
				The word to be inserted.

		'''
		row = randint(0,9)
		aux_row = row
		# Checking the posibility to add the word
		for letter in word:
			if aux_row > 9:
				aux_row = 0
			if self.current_grid[aux_row][column] != '':
				if self.current_grid[aux_row][column] != letter:
					return False
			aux_row += 1
		# Adding the word.
		for letter in word:
			if row > 9:
				row = 0
			if self.current_grid[row][column] == '':
				self.current_grid[row][column] = letter
			row += 1
		return True

	def fill(self):
		''' Fill the blak spaces with random letters.'''

		alfabet = ascii_uppercase
		for i in range(10):
			for j in range(10):
				if self.current_grid[i][j] == '':
					self.current_grid[i][j] = sample(alfabet,1)[0]


class Subject:
# Version 1.0

	def __init__(self, name):
		self.name = name
		self.content = []

	def add_word(self, word):
	#Add a word to self.content.
		pass

	def import_subject(self, file):
	# Import all the words corresponding to a subject from a file
		pass

	def get_name(self):
		''' Return the name of the subject. 

		Return:
		------
			string
				The name - Valid case.

		'''
		return self.name

	def get_words(self):
		''' Return all the words of the subject.

			Return:
			------
				[string]
					The words. Can be empty.

		'''
		return self.content


class Dictionary:
# Version 1.0
	def __init__(self):
		self.subjects = []

	def add_subject(self, subject):
	# Return if there was an error.
	# Version 1.0
		pass

	def display_subjects(self):
		''' Display the list of the names of the subjects. '''
		print('Subjects: ')
		for subject in self.subjects:
			print('- ' + subject.get_name())
		print('')

	def load(self,file):
	# Version 1.0
		pass

	def get_subject_by_name(self, name):
		''' Return a subject using its name element.

		Parameters:
		----------
			name: string
				The name of the subject as a string

		Return:
		------
			Subject
				Valid case.
			None 
				Invalid case. 

		'''
		for subject in self.subjects:
			if subject.get_name() == name:
				return subject
		return None

class Clue:
# Version 1.0

	def __init__(self):
		self.subject_name = None
		self.words_not_found = []
		self.words_found = []

	def build(self, subject, n):
		''' Build the clue, using the words of a subject, adding randomly
			the words into the not found list. In this version, there will 
			be 12 clues per board by default.

		Parameters:
		----------
			subject: Subject
				Subject object that contain the words to be used.
			n: integer
				Number of words to be selected.

		'''
		self.subject_name = subject.get_name()
		words = list(subject.get_words())
		# Functions from Python Random Lib.
		shuffle(words)
		if len(words) < n:
			lim = len(words)
		elif n <= 0:
			lim = 12
		else:
			lim = n
		for i in range(lim):
			self.add_word_to_not_found(words[i].upper())


	def word_in_clue(self, word):
	# Checks if the word is on the list of words that have not been found
		pass

	def already_found(self,word):
	# Cheks if the word is has already been found
		pass

	def add_word_to_not_found(self, word):
		''' Add a word to the clue as not found.

		Parameters:
		----------
			word: string
				Word that will be added.

		'''
		if word == "" or word == None:
			print("Error: Incorrect format. It was not added.")
		else:
			self.words_not_found.append(word)

	def add_word_to_found(self, word):
		pass

	def remove_word_from_not_found(self, word):
	# Return if the word is in NOT FOUND
		pass

	def found_all_the_words(self):
		pass

	def get_words_not_found(self):
		''' Return the list of words not found. 

		Parameters:
		----------
			[string]
				Words not found.

		'''
		return self.words_not_found


class BySubject(Clue):

	def display ():
		pass
		
class BySolution(Clue):
# Version 1.0

	def display ():
	# Version 1.0
		pass
		
class ByLetters(Clue):

	def display ():
		pass
		
class ByLength(Clue):

	def display ():
		pass


class Score:
	# IS THE NICK NAME ENOUGH?
	def __init__ (self, nickname, points):
		self.nickname = nickname
		self.points = points

	def __str__(self):
		pass

class HighScores:

	# SEPARATE AS 2 INTANCES?

	def __init__(self):
		self.simple_mode = []
		self.racetime_mode = []

	def add_simple_mode_highscore(self, score):
		pass
	
	def add_race_time_mode_highscore(self, score):
		pass

	def import_highscores(self, file):
		pass
		
	def export_highscores(self, file):
		pass

	def is_highscore(self, score):
		pass

	def display(self):
		pass


class Game:
# Version 1.0

	def __init__(self):
		self.board = None
		self.clue = None

	def add_board(self, board):
		''' Add the board into the element board of the game 

		Parameters:
		----------
			board: Board
				Object of type Class Board.

		'''
		self.board = board
		

	def select_subject(self):
		''' Return a selected subject from the dictionary.

		Return:
		------
		Subject
			the selected subject - Valid case.

		'''
		sname = ""
		subject = None
		while subject == None:
			print('Please, choose a correct subject...')
			dictionary.display_subjects()
			sname = input("Type here your subject: ")
			subject = dictionary.get_subject_by_name(sname)
			if subject == None:
				print('----------------------------------------------')
				print('Error: It is not a correct subject. Try again.')
		return subject

	def select_clue(self, subject):
		''' Select an specific type of clue. For this version,
			it will be BySolution.

		Parameters:
		----------
			subject: Subject
				subject that will be used into the building clue processes.

		'''
		clue = BySolution()
		if subject == None:
			print("Error: Incorrect format. It was not selected")
		else:
			clue.build(subject,12)
			self.clue = clue


	def read_command(self):
	# Version 1.0
		pass

	def find_word(self):
	# Version 1.0
		pass

	def turn(self):
	# reads the commands of the user.
	# the user rotates the board, find words, etc..
	# Version 1.0
		pass

	def setup(self):
		''' Setup all the configuration of the game before starting.'''

		selected_subject = self.select_subject()
		self.select_clue(selected_subject)
		words = list(self.clue.get_words_not_found())
		new_board = Board()
		new_board.build(words)
		self.add_board(new_board)

class SinglePlayer(Game):
# Version 1.0

	def __init__(self):
		self.player = None

	def display_current_state(self):
	# Display the board, the list of words according to the clue
	# Version 1.0
		pass

	def restart(self):
	# Version 1.0
		pass


class PracticeMode(SinglePlayer):
# Version 1.0

	def play(self):
	# Version 1.0
		pass
		
	def restart(self):
	# Version 1.0
		pass
		
class SimpleMode(SinglePlayer):

	def __init__(self):
		self.initial_time = 0
		
	def play(self):
		pass
		
	def manage_time(self):
	# Starts the time
	# Thread 
		pass

	def compute_score(self, words, time):
		pass


class TimeRaceMode(SinglePlayer):

	def __init__(self):
		self.initial_time = 0
		self.final_time = 0

	def manage_time(self):
	# Takes the time
		pass

	def is_time_over(self):
		pass
	
	def play(self):
		pass

	def compute_score(self, words, time):
		pass

class MultiPlayer(Game):

	def __init__ (self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.current_player = player1
		self.time_per_turn = 0

	def display_current_state(self):
	# Display the board, the list of words according to the clue
	# The name of the player in turn
		pass

	def set_current_player(self):
	# change of current_player
		pass

	def manage_time(self):
	# take the time corresponding to each turn
		pass

	def play(self):
		pass

	def is_time_over(self):
		pass

	def display_winner(self):
		pass

	def restart(self):
	# Setup of the game again, keeping the same players.
		pass

class Instruction:

	def __init__ (self):
		self.instruction = None

	def import_instruction(self, file):
		pass

	def display():
		pass


# Dictionary of words.
dictionary = Dictionary()

def main():
	pass

if __name__ == '__main__':
  main()


	
