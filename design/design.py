
def display_select_subject():
		
def display_select_clue():


class Player:

	def __init__(self, nickname):
		self.nickname = nickname
		self.clue = None

	def add_clue(self, clue):


class Board:

	def __init__(self):
		self.grid = [[]]
		self.rows = 10
		self.columns = 10

	def build (self, clue):

	def rotate(self, number, direction):

	def display(self):


class Subject:

	def __init__(self, name):
		self.name = name
		self.content = []

	def add_word(self, word):

	def import_subject(self, file):


class Dictionary:

	def __init__(self):
		self.subjets = []

	def add_subject(self, subjet):

	def display_subjets(self):


class Clue:
	# INHERITANCE FROM SUBJECT?
	def __init__(self, subject_name, words_not_found):
		self.subject_name = subject_name
		self.words_not_found = words_not_found
		self.words_found = []

	def is_word(self, word):

	def add_word_to_found(self, word):

	def remove_word_from_not_found(self, word):


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

	def __init__(self, board):
		self.board = board

	def find_word(self):


class SinglePlayer(Game):

	def __init__(self, player):
		self.player = player

	def display_current_state(self):

	def play():

	def restart(self):

	def exit_game(self):
		
class PracticeMode(SinglePlayer):

	def play():
		
class SimpleMode(SinglePlayer):

	def __init__(self):
		self.initial_time = 00:00

	def play():
		
	def manage_time(self):

	def compute_score(self, words, time):


class TimeRaceMode(SinglePlayer):

		self.initial_time = 03:00
		self.final_time = 00:00

	def play():
	
	def manage_time(self):

	def compute_score(self, words, time):

class MultiPlayer(Game):

	def __init__ (self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.current_player = player1

	def display_current_state(self):
	
	def play (self):

	def change_turn(self):

	def take_time(self):

	def restart(self):

	def exit_game(self):

class Instruction:

	def __init__ (self):
		self.instruction = None

	def import_instruction(self, file):

	def display():
