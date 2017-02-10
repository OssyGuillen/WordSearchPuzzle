

def display_initial_message():
# Displays the name of the game and a welcome message
# Version 1.0

def display_menu():
# Displays the menu with the options:
# Single Player
# Multi Player
# Instructions
# Exit
# Version 1.0

def display_single_player_modes():
# Version 1.0

def get_player_nickname():

def start_game():

def setup():

def exit_game():


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
# Version 1.0
	def __init__(self, nickname):
		self.nickname = nickname # Not Version 1.0
		self.clue = None # Not Version 1.0

	def set_clue(self, clue):
	# Version 1.0


class Board:
# Version 1.0

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
# Version 1.0

	def __init__(self, name):
		self.name = name
		self.content = []

	def add_word(self, word):
	#Add a word to self.content.

	def import_subject(self, file):
	# Import all the words corresponding to a subject from a file


class Dictionary:
# Version 1.0
	def __init__(self):
		self.subjects = []

	def add_subject(self, subject):
	# Return if there was an error.
	# Version 1.0

	def display_subjects(self):
	#Display the list of the names of the subjects
	# Version 1.0

	def load(self,file):
	# Version 1.0

	def get_subject_by_name(self, name):
	# Version 1.0
	# Return subject

class Clue:
# Version 1.0

	# INHERITANCE FROM SUBJECT?
	def __init__(self, subject_name):
		self.subject_name = subject_name
		self.words_not_found = []
		self.words_found = []

	def build():

	def word_in_clue(self, word):
	# Checks if the word is on the list of words that have not been found

	def already_found(self,word):
	# Cheks if the word is has already been found

	def add_word_to_not_found(self, word):

	def add_word_to_found(self, word):

	def remove_word_from_not_found(self, word):
	# Return if the word is in NOT FOUND

	def found_all_the_words(self):


class BySubject(Clue):

	def display ():
		
class BySolution(Clue):
# Version 1.0

	def display ():
	# Version 1.0
		
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
# Version 1.0

	def __init__(self):
		self.board = None

	def add_board(self):
	# Version 1.0

	def select_subject(self):
	# Version 1.0
	# Return subject.

	def select_clue(self):
	# Version 1.0

	def read_command(self):
	# Version 1.0

	def find_word(self):
	# Version 1.0

	def turn(self):
	# reads the commands of the user.
	# the user rotates the board, find words, etc..
	# Version 1.0

	def setup(self):

class SinglePlayer(Game):
# Version 1.0

	def __init__(self, player):
		self.player = player

	def display_current_state(self):
	# Display the board, the list of words according to the clue
	# Version 1.0

	def restart(self):
	# Version 1.0


class PracticeMode(SinglePlayer):
# Version 1.0

	def play(self):
	# Version 1.0
		
	def restart(self):
	# Version 1.0
		
class SimpleMode(SinglePlayer):

	def __init__(self):
		self.initial_time = 00:00
		
	def play(self):
		
	def manage_time(self):
	# Starts the time
	# Thread 

	def compute_score(self, words, time):


class TimeRaceMode(SinglePlayer):

	def __init__(self):
		self.initial_time = 05:00
		self.final_time = 00:00

	def manage_time(self):
	# Takes the time

	def is_time_over(self):
	
	def play(self):

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

	def restart(self):
	# Setup of the game again, keeping the same players.

class Instruction:

	def __init__ (self):
		self.instruction = None

	def import_instruction(self, file):

	def display():




