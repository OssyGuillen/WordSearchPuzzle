

def display_initial_message():
# Displays the name of the game and a welcome message

def display_menu():
# Displays the menu with the options:
# Single Player
# Multi Player
# Instructions
# Exit

def display_single_player_modes():

def get_player_nickname():


commands = ["help","exit","rotate","word","initial"]
direction = ["right","left","up","down"]
messages = {"incorret_word":"The word is not on the list", 
			"found_word":"You already found this word",
			"good_word":"Congratulations! You just find a word",
			"welcome":"WORD SEARCH PUZZLE"
			"winner":" is the winner",
			"win": "Congratulations! You won",
			"highscore": "NEW HIGHSCORE",
			"wrong_direction": "That is an invalid direction. Only 'right', 'left', 'up', 'down' are possible",
			"invalid_cell": "That cell is not inside the board",
			"insert_direction": "Direction: ",
			"insert_row_number": "Row number: ",
			"insert_column_number": "Column number: "}

class Player:

	def __init__(self, nickname):
		self.nickname = nickname
		self.clue = None

	def set_clue(self, clue):


class Board:

	def __init__(self):
		self.original_grid = [[]]
		self.current_grid = [[]]
		self.rows = 10
		self.columns = 10

	def build (self, words):
	# Add to the board all the words in clue. 
	# Fill the blank spaces with random letters
	# Rotates the board randomly

	def restart_board(self):
	# Restart the board to its original state

	def rotate(self, number, direction):
	# Rotates either the column or the row
	# TYPE OF DIRECTION?

	def display(self):
	# Prints the grid

	def is_valid_cell(self,row,column):
	# The cell is inside the board

	def can_generate_a_word(self,row1,column1,row2,column2):
	# The cells form a line where it is possible to find a word

	def get_word(self,row1,column1,row2,column2):

class Subject:

	def __init__(self, name):
		self.name = name
		self.content = []

	def add_word(self, word):
	#Add a word to self.content.

	def import_subject(self, file):
	# Import all the words corresponding to a subject from a file


class Dictionary:

	def __init__(self):
		self.subjets = []

	def add_subject(self, subjet):

	def display_subjets(self):
	#Display the list of the names of the subjects


class Clue:
	# INHERITANCE FROM SUBJECT?
	def __init__(self, subject_name, words_not_found):
		self.subject_name = subject_name
		self.words_not_found = words_not_found
		self.words_found = []

	def word_in_clue(self, word):
	# Checks if the word is on the list of words that have not been found

	def already_found(self,word):
	# Cheks if the word is has already been found

	def add_word_to_found(self, word):

	def remove_word_from_not_found(self, word):

	def found_all_the_words(self):


class BySubject(Clue):

	def display ():
		
class BySolution(Clue):

	def display ():
		
class ByLetters(Clue):

	def display ():
		
class ByLength(Clue):

	def display ():


class Score:
	# IS THE NICK NAME ENOUGH?
	def __init__ (self, nickname, points):
		self.nickname = nickname
		self.points = points

	def __str__(self):

class HighScores:

	# SEPARATE AS 2 INTANCES?

	def __init__(self):
		self.simple_mode = []
		self.racetime_mode = []

	def add_simple_mode_highscore(self, score):
	
	def add_race_time_mode_highscore(self, score):

	def import_highscores(self, file):

	def export_highscores(self, file):

	def is_highscore(self, score):

	def display(self):


class Game:

	def __init__(self):
		self.board = None

	def add_board(self):
	
	def select_subject(self):
		
	def select_clue(self):

	def read_command(self):
	
	def find_word(self):

	def turn(self):
	# reads the commands of the user.
	# the user rotates the board, find words, etc..

class SinglePlayer(Game):

	def __init__(self, player):
		self.player = player

	def display_current_state(self):
	# Display the board, the list of words according to the clue

	def restart(self):


class PracticeMode(SinglePlayer):

	def play(self):
		
	def exit_game(self):
		
class SimpleMode(SinglePlayer):

	def __init__(self):
		self.initial_time = 00:00
		
	def play(self):
		
	def manage_time(self):
	# Starts the time
	# Thread

	def exit_game(self): 

	def compute_score(self, words, time):


class TimeRaceMode(SinglePlayer):

	def __init__(self):
		self.initial_time = 05:00
		self.final_time = 00:00

	def manage_time(self):
	# Takes the time

	def is_time_over(self):
	
	def play(self):

	def exit_game(self):

	def compute_score(self, words, time):

class MultiPlayer(Game):

	def __init__ (self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.current_player = player1
		self.time_per_turn = 02:00

	def display_current_state(self):
	# Display the board, the list of words according to the clue
	# The name of the player in turn

	def set_current_player(self):
	# change of current_player

	def manage_time(self):
	# take the time corresponding to each turn

	def play(self):

	def is_time_over(self):

	def display_winner(self):

	def exit_game(self):

	def restart(self):
	# Setup of the game again, keeping the same players.

class Instruction:

	def __init__ (self):
		self.instruction = None

	def import_instruction(self, file):

	def display():




