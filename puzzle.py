from random import shuffle, randint, sample
from string import ascii_uppercase
import xml.etree.ElementTree as ET
import glob, os, time, re


commands = ["help","exit","rotate","find"]
bool_answers = ["yes","no"]
directions = ["right","left","up","down"]
messages = {
			"already_found_word":" was already found.",
			"choose_subject":"Please, choose a subject...\n",
			"error": "\nAn error occurred. Leaving the game.\n",
			"error_instruction": "\nAn error occurred. No instructions. Leaving the game.\n",
			"enter_to_continue":"\nEnter to Continue.",
			"exit_game": "\nLeaving the game.\n",
			"final_cell": "\nPlease, insert the coordinates of the final cell:",
			"good_word":"\nCongratulations! You just found ",
			"highscore": "NEW HIGHSCORE",
			"incorret_format":"\nERROR: Incorrect format. It was not added.",
			"incorret_format_clue":"\nERROR: Incorrect format. It was not selected.",
			"incorret_word":" is not on the list.", 
			"initial_cell": "\nPlease, insert the coordinates of the initial cell:",
			"insert_column_number": "Column number ?  ",
			"insert_command": "\nAction [rotate|find|help|exit] ? ",
			"insert_direction": "Direction [up|down|right|left] ? ",
			"insert_menu_action": "\nAction [p|h|e] ? ",
			"insert_number_spaces": "Spaces ? ",
			"insert_row_number": "Row number ?  ",
			"invalid_cell": "\nERROR: That cell is not inside the board.",
			"invalid_column": "\nERROR: That column is not inside the board.",
			"invalid_command": "\nERROR: That is an invalid command. Only 'rotate', 'find', 'help', 'exit' are possible.\n",
			"invalid_direction": "\nERROR: That is an invalid direction. Only 'right', 'left', 'up', 'down' are possible.",
			"invalid_menu_option":"\nERROR: Invalid option. Only 'p' for play, 'h' for help and 'e' for exit.\n",
			"invalid_number_spaces": "\nERROR: Invalid number of spaces.",
			"invalid_play_again_option": "\nERROR: Invalid option. Only 'yes' or 'no'.",
			"invalid_row": "\nERROR: That row is not inside the board.",
			"invalid_subject": "\nERROR: It is not a valid subject. Try again.\n",
			"it_is_not_a_line": "\nERROR: The cells must form a vertical or a horizontal line of at least 3 letters.",
			"it_is_not_an_integer": "\nERROR: It must be an integer.",
			"menu": "MENU\n\n[p] Play\n[h] Help\n[e] Exit\n",
			"play_again": "\n\nPlay again [yes|no] ? ",
			"separator": "\n----------------------------------------------------------\n",
			"setting_up": "Setting up...",
			"single_player_modes":"MODE\n\nPractice mode\n",
			"starting":"Starting...",
			"get_subject":"Type here your subject: ",
			"welcome":"WORD SEARCH PUZZLE\n\nLet's play!\n",
			"win": "\n\n\nCongratulations! You found all the words. You won. ",
			"winner":" is the winner.",
			"words_to_find":"Words to find: "
			}

class Instruction:
	''' Manage all the information corresponding to the rules of 
		the game.
	'''

	def __init__ (self):
		self.instruction = None

	def import_instruction(self, file):
		''' Import the set of instructions of the game from a file.

		Parameters
		----------
		file : str
			Path of the file where the instructions are found.

		'''

		try: 
			f = open(file,'r')
			self.instruction = f.read()
		except:
			print(messages["error_instruction"])
			exit()

	def display(self):
		''''Display on the standard output the rules of the game.

		'''
		print(self.instruction)

class Player:

	def __init__(self, nickname):
		self.nickname = nickname
		self.clue = None

	def set_clue(self, clue):
		''' Set a created clue into the player's clue. 

		Parameters
		----------
			clue: BySolution(Clue)
				A clue object

		'''
		pass

class Board:
	''' Manage the board where the words to be found are placed.

	'''

	def __init__(self):
		self.original_grid = [[]]
		self.current_grid = [[]]
		self.rows = 10
		self.columns = 10
		self.min_word_length = 3
		self.max_word_length = 8
		self.max_num_words = 10

	def build (self, words):
		''' Add to the board all the words given and fill the blanks spaces left
			with random letters .

		Parameters
		----------
			words : [str]
				An array with the words to be placed on the board.

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

	def is_valid_row(self,row):
		""" Check if the row number is inside the grid.
			
		Paramenters
		----------- 
		row : int 
			row number.

		Returns
		-------
		bool 
			True for success, False otherwise.

		"""
		return (row < self.rows and row >= 0)

	def is_valid_column(self,column):
		""" Check if the column number is inside the grid.
			
		Paramenters
		-----------
		column : int
			column number.

		Returns
		-------
		bool 
			True for success, False otherwise.

		"""
		return (column < self.columns and column >= 0)

	def is_valid_number_spaces(self,direction,number):
		""" Check if the number is to rotate is correct.
			
		Paramenters
		----------- 
		direction : str
			direction to rotate.
		number : int
			number of spaces to rotate.

		Returns
		-------
		bool
			True for success, False otherwise.

		"""
		if number > 0 and \
			(((direction == "up" or direction == "down") and \
				number < self.columns) or\
			((direction == "left" or direction == "right") and\
				number < self.rows)):
				return True
		return False

	def rotate_horizontally(self, row, number, direction):
		""" Rotates a row of the current grid a 'number' amount of spaces.
			
		Paramenters
		----------- 
		row : int
			row number to rotate.
		number : int
			number of space to rotate.
		direction : str
			direction to rotate the row ("left" or "right").

		Returns
		-------
		bool
			True if the board was successfully rotate, False otherwise.

		"""
		if self.is_valid_row(row):
			number = number % self.rows
			if direction == "right":
				self.current_grid[row] = self.current_grid[row][-number:] +\
										 self.current_grid[row][:-number]
			elif direction == "left":	
				self.current_grid[row] = self.current_grid[row][number:] +\
										 self.current_grid[row][:number]
			return True
		return False
	
	def rotate_vertically(self, column, number, direction):
		""" Rotates a column of the current grid a 'number' amount of spaces.
			
		Paramenters
		-----------
		column : int
			column number to rotate.
		number : int
			number of space to rotate.
		direction : str 
			direction to rotate the column ("up" or "down").

		Returns
		------- 
		bool
			True if the board was successfully rotate, False otherwise.
			
		"""
		if self.is_valid_column(column):
			number = number % self.columns
			temp_col=[]
			for i in range(self.columns):
				temp_col.append(self.current_grid[i][column])

			if direction == "up":
				temp_col = temp_col[number:] + temp_col[:number]
			elif direction == "down":
				temp_col = temp_col[-number:] + temp_col[:-number]
		
			for i in range(self.columns):
				self.current_grid[i][column]=temp_col[i]
			return True
		return False

	def get_letter(self,row,column):
		''' Return the letter that inside a cell on the board.

		Paramenters
		-----------
		row : int
			row of the cell of the letter wanted.
		column : int
			column of the cell of the letter wanted.
		
		Returns
		-------
		str
			Letter extratect from the cell of the board.

		'''
		if self.is_valid_cell(row,column):
			return self.current_grid[row][column]
		return None

	def display(self):
		""" Display the grid on the standard output. Row and columns numbers
		are included.

		"""
		print ("\n   ", end='')
		for i in range (self.columns):
			print (str(i) + "   ", end='')
		print("\n")
		for i in range (self.rows):
			for j in range (self.columns):
				if j == 0:
					print (str(i) + "  ", end='')
				print (self.get_letter(i,j) + "   ", end='')
				if j == self.rows - 1:
					print (str(i), end='')
			print("\n")
		print ("   ", end='')
		for i in range (self.columns):
			print (str(i) + "   ", end='')
		print("\n")



	def is_valid_cell(self,row,column):
		""" Check if the cell is inside the grid.
			
		Paramenters
		-----------
		row : int
			row number of the cell.
		column : int 
			column number of the cell.

		Returns
		-------
		bool
			True for success, False otherwise.

		"""
		if self.is_valid_row(row) and self.is_valid_column(column):
			return True
		return False


	def can_generate_a_word(self,row1,column1,row2,column2):
		''' Receive 2 cells and check they are valid, if they form a vertical 
			or an horizontal line, and if they form a word long enough.

		Paramenters
		-----------
		row1 : int
			row number of the starting cell.
		column1 : int
			column number of the starting cell.
		row2 : int
			row number of the final cell.
		column2 : int
			column number of the final cell.

		Returns
		-------
		bool
			True for success, False otherwise.

		'''
		if  (self.is_valid_cell(row1,column1) and 
			 self.is_valid_cell(row2,column2) and \
			
			(row1 == row2 and column1 != column2 and 
			 abs(column1 - column2) + 1 >= self.min_word_length) or \
			
			(column1 == column2 and row1 != row2 and \
			abs(row1 - row2) + 1 >= self.min_word_length)):
			return True
		return False


	def get_word(self,row1,column1,row2,column2):
		""" Get the word from the grid. The word is specified by a starting cell
			and a final cell.
		
		Paramenters
		-----------
			row1 : int
				row number of the starting cell.
			column1 : int
				column number of the starting cell.
			row2 : int
				row number of the final cell.
			column2 : int
				column number of the final cell.

		Returns
		-------
		str
			Word obtained from the grid. None if the cells are not valid.

		"""

		if self.can_generate_a_word(row1,column1,row2,column2):
			word = "" 
			# The word is placed horizontally
			if (row1 == row2):
				start = min(column1,column2)
				end = max(column1,column2)
				for i in range (start,end+1):
					word = word + self.get_letter(row1,i)
				return word
			# The word is placed vertically
			elif (column1 == column2):
				start = min(row1,row2)
				end = max(row1,row2)
				for i in range (start,end+1):
					word = word + self.get_letter(i,column1)
				return word
		else:
			return None


	def add_word_into_row(self, row, word):
		''' Insert a word into a row of the board. 

		Parameters
		----------
		row: int
			The number of the row.
		word: str
			The word to be inserted.

		Returns
		-------
		bool
			True for success, False otherwise.

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

		Parameters
		----------
		column: integer
			The number of the column.
		word: string
			The word to be inserted.

		Returns
		-------
		bool
			True for success, False otherwise.

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
		''' Fill the blank spaces of the board with random letters.

		'''

		alfabet = ascii_uppercase
		for i in range(10):
			for j in range(10):
				if self.current_grid[i][j] == '':
					self.current_grid[i][j] = sample(alfabet,1)[0]

	def get_max_num_words(self):
		''' Return the maximun number of words allowed.

		Returns
		-------
		int
			The maximun number of words.

		'''
		return self.max_num_words

	def get_min_length_word(self):
		''' Return the Minimun length of a word allowed.

		Returns
		-------
		int
			The minimun length.
		'''
		return self.min_word_length

	def get_max_length_word(self):
		''' Return the Maximun length of a word allowed.

		Returns
		-------
		int
			The maximun length

		'''
		return self.max_word_length

class Subject:
	''' Manage the subjects all the words on a board are related to. '''

	def __init__(self):
		self.name = None
		self.content = []

	def add_word(self, word):
		''' Add a word into the subject.

		Parameters
		----------
		word : str
			Word to be added.

		'''

		if word is not None:
			self.content.append(word)


	def import_subject(self, file):
		''' Import the content of a well-formed xml into a subject.

		Parameters
		----------
		file : str
			The path of the file.

		'''

		# Parsing XML
		# xml.etree.ElementTree from Python The ElementTree XML API
		# Source code: https://docs.python.org/3.4/library/xml.etree.elementtree.html
		tree = ET.parse(file)
		root = tree.getroot()
		words = 0
		if len(root) > 0:
			self.name = root[0].attrib['name']
			root = root[0]
			for child in root:
				if child. tag == "word":
					new_word = child.text
					# Parsing a string using Regular Expression
					# re from Python Regular expression operations
					# Source code: https://docs.python.org/3.4/library/re.html
					if re.match('^[a-zA-Z]+$', new_word) is not None:
						self.add_word(new_word)
						words += 1
		else:
			return False
		return words >= 12


	def get_name(self):
		''' Return the name of the subject. 

		Returns
		-------
		str
			Name of the subject.

		'''
		return self.name

	def get_words(self):
		''' Return all the words of the subject.

		Returns
		-------
		[str]
			All the words of the subject. Can be empty.

		'''
		return self.content


class Dictionary:
	''' Manage all the subjects available on the game. 

	'''

	def __init__(self):
		self.subjects = []

	def add_subject(self, subject):
		''' Add a subject object into the dictionary.

		Parameters
		----------
		subject: Subject
			Subject to be added.

		'''
		self.subjects.append(subject)

	def display_subjects(self):
		''' Display on the standard output the list of the names of the 
		all the subjects. 

		'''
		print('Subjects: ')
		for subject in self.subjects:
			print('- ' + subject.get_name())
		print('')

	def load(self):
		''' Load the dictionary from xml files into subjects directory. 

		Returns
		-------
		bool
			True for success, False otherwise.

		'''

		# Manage files and directories.
		# os.walk from Python Miscellaneous operating system interfaces.
		# Source code: https://docs.python.org/3.4/library/os.html#os.walk
		try:
			num_of_correct_subjects = 0
			for root, dirs, files in os.walk("subjects"):
				for file in files:
					if file.endswith(".xml"):
						new_subject = Subject()
						correct = new_subject.import_subject(os.path.join(root, file))
						if correct:
							self.add_subject(new_subject)
							num_of_correct_subjects += 1
			return num_of_correct_subjects > 0
		except:
			return False
		    

	def get_subject_by_name(self, name):
		''' Return a subject using its name element.

		Parameters
		----------
		name : str
			The name of the subject as a string.

		Returns
		-------
		Subject
			Subject corresponding to `name`.

		'''
		for subject in self.subjects:
			if subject.get_name().lower() == name.lower():
				return subject
		return None

class Clue:
	''' Manage the list of words that the player needs to find on the game.

	'''

	def __init__(self):
		self.subject_name = None
		self.words_not_found = []
		self.words_found = []

	def build(self, subject, num_words, min_length, max_length):
		''' Build the clue, using the words of a subject, adding randomly
			the words into the not found list. There will be 10 clues per board 
			by default.

		Parameters
		----------
		subject : Subject
			Subject object that contain the words to be used.
		num_words : int
			Number of words to be selected.
		min_length : int
			Minimun length of a word.
		max_length: in
			Maximun length of a word.

		'''
		self.subject_name = subject.get_name()
		words = list(subject.get_words())
		# Functions from Python Random Lib.
		shuffle(words)
		if len(words) < num_words:
			lim = len(words)
		elif num_words <= 0:
			lim = 10
		else:
			lim = num_words

		i = 0
		while lim > 0 and i < len(words):
			if len(words[i]) <= max_length and len(words[i]) >= min_length:
				self.add_word_to_not_found(words[i].upper())
				lim -= 1
			i += 1

		# Inconsistency
		if lim > 0:
			print(messages["error"])
			exit()

	def word_already_found(self,word):
		""" Checks if a word is on the list of words already found.

		Parameters
		----------
		word : str
			Word to check.

		Returns
		-------
		bool
			True for success, False otherwise.

		"""
		return (word in self.words_found)

	def word_not_found(self,word):
		""" Cheks if a word is on the list of words that have not been found.

		Parameters
		----------
		word : str
			word to be checked.

		Returns
		-------
		bool 
			True for success, False otherwise.
			
		"""
		return (word in self.words_not_found)

	def word_in_clue(self, word):
		""" Cheks if a word belongs to a clue. Checks if a word is included on
			the list of words already found or on the list of words that have 
			not been found.

		Parameters
		----------
		word : str
			word to be checked.

		Returns
		-------
		bool
			True for success, False otherwise.
			
		"""		
		return (self.word_already_found(word) or self.word_not_found(word))

	def add_word_to_not_found(self, word):
		''' Add a word to the clue as not found.

		Parameters
		----------
		word : string
			Word that will be added.

		'''
		if word == "" or word == None:
			print(messages["incorret_format"])
		else:
			self.words_not_found.append(word)

	def add_word_to_found(self, word):
		""" Add a word to the list of words that have been found.

		Parameters
		----------
			word (str): word to be added.

		"""		
		self.words_found.append(word)

	def remove_word_from_not_found(self, word):
		""" Check if the word is on the list of words that have not been found
			and removed it.

		Parameters
		-----------
		word : str
			Word to be removed.

		Returns
		------- 
		bool
			True if the word was successfully removed. False otherwise.

		"""	
		if (self.word_not_found(word)):
			self.words_not_found.remove(word)
			return True
		return False

	def found_all_the_words(self):
		""" Check if the list of words that have not been found is empty and
			the list of words that have been found is not empty.

		Returns
		------- 
		bool
			True for success, False otherwise.

		"""	
		return ((len(self.words_not_found) == 0) and\
				(len(self.words_found) != 0))

	def get_words_not_found(self):
		''' Return the list of words not found. 

		Returns
		-------
		[str]
			List of words that has not been found by the player.

		'''
		return self.words_not_found


class BySubject(Clue):

	def display (self):
		pass

class BySolution(Clue):
	''' Subclass that displays all the words in the Clue.

	''' 

	def display (self):
		''' Display on the standard output the name of the subject and the complete
			list of words that the player needs to find.

		'''
		print(self.subject_name + ": ")
		print(self.words_not_found)
		
class ByLetters(Clue):

	def display (self):
		pass
		
class ByLength(Clue):

	def display (self):
		pass


class Score:
	
	def __init__ (self, nickname, points):
		self.nickname = nickname
		self.points = points

	def __str__(self):
		pass

class HighScores:

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
	''' Superclass. Manage information of a game on its different modes.

	'''

	def __init__(self):
		self.board = None
		self.clue = None
		self.start_again = False

	def add_board(self, board):
		''' Associate a built board to the game.

		Parameters
		----------
		board : Board
			Board to be added to the game.

		'''
		self.board = board
		

	def select_subject(self):
		''' Return a selected subject from the dictionary.

		Returns
		-------
		Subject
			Subject selected by the player.

		'''
		sname = ""
		subject = None
		while subject == None:
			print(messages["choose_subject"])
			dictionary.display_subjects()
			sname = input(messages["get_subject"])
			subject = dictionary.get_subject_by_name(sname)
			if subject == None:
				print(messages["separator"])
				print(messages["invalid_subject"])
		return subject

	def select_clue(self, subject, num_words, min_length, max_length):
		''' Select a specific type of clue. For this version, it will be 
			BySolution.

		Parameters
		----------
		subject : Subject
			subject that will be used into the building clue process.
		num_words : int
			Number of words to be selected
		min_length : int
			Minimun length of a word.
		max_length: int
			Maximun length of a word.

		'''
		clue = BySolution()
		if subject == None:
			print(messages["incorret_format_clue"])
		else:
			clue.build(subject, num_words,min_length, max_length)
			self.clue = clue


	def get_row_number(self):
		""" Read from standard input an integer.

		Returns
		------- 
			int : row number read. 

		"""	
		is_valid = False
		while not is_valid:
			try: 
				n = int(input(messages["insert_row_number"]))
				if self.board.is_valid_row(n):
					return n
				print(messages["invalid_row"])
			except:
				print(messages["it_is_not_an_integer"])

	def get_column_number(self):
		""" Read from standard input an integer.

		Returns
		------- 
			int : column number read. 

		"""	
		is_valid = False
		while not is_valid:
			try:
				n = int(input(messages["insert_column_number"]))
				if self.board.is_valid_column(n):
					return n
				print(messages["invalid_column"])
			except:
				print(messages["it_is_not_an_integer"])

	def find_word(self):
		""" Find a word specified by the user. Get the row and the column 
			numbers corresponding to initial and the final cells of the word.
			Get the word from the board, and check if the word is valid.
			Display appropiate messages to the user.

		"""	
		print (messages["initial_cell"])
		row1 = self.get_row_number()
		column1 = self.get_column_number()
		print (messages["final_cell"])
		row2 = self.get_row_number()
		column2 = self.get_column_number()
		word = self.board.get_word(row1,column1,row2,column2)
		if word != None:
			if not self.clue.word_in_clue(word):
				print("'" + word + "'"+ messages["incorret_word"])
				return
			if self.clue.word_already_found(word):
				print("'" + word + "'" + messages["already_found_word"])
			else:
				self.clue.add_word_to_found(word)
				self.clue.remove_word_from_not_found(word)
				print(messages["good_word"] + "'" + word + "'.")
		else:
			print(messages["it_is_not_a_line"])

	def setup(self):
		''' Setup all the configuration of the game before starting.'''

		new_board = Board()
		selected_subject = self.select_subject()
		self.select_clue(selected_subject,
						 new_board.get_max_num_words(),
						 new_board.get_min_length_word(),
						 new_board.get_max_length_word())
		words = list(self.clue.get_words_not_found())
		new_board.build(words)
		self.add_board(new_board)

	def get_direction(self):
		""" Read from standard input a string corresponding to a direction.
			Only 'right', 'left', 'up', 'down' are possible.
		
		Returns
		-------
		str
			direction read. 

		"""	

		is_valid = False
		while not is_valid:
			direction = (input(messages["insert_direction"])).lower()
			if direction in directions:
				return direction
			print(messages["invalid_direction"])

	def get_number_spaces(self,direction):
		""" Read from standard input an integer.
		
		Parameters
		----------
		direction : str
			Direction the board is going to rotate to.

		Returns
		-------
		int
			Number of spaces read. 

		"""	
		is_valid = False
		while not is_valid:
			try:
				n = int(input(messages["insert_number_spaces"]))
				if self.board.is_valid_number_spaces(direction,n):
					return n
				print(messages["invalid_number_spaces"])
			except:
				print(messages["it_is_not_an_integer"])


	def get_rotation_attr(self): 
		""" Get the direction to rotate the board, the number of row or column
		that is going to rotate and the amount of spaces to rotate. Then
		rotates the board accordint to these parameters.

		"""	
		direction = self.get_direction()
		if direction == "up" or direction == "down":
			column = self.get_column_number()
			number = self.get_number_spaces(direction)
			self.board.rotate_vertically(column,number,direction)
		elif direction == "left" or direction == "right":
			row = self.get_row_number()
			number = self.get_number_spaces(direction)
			self.board.rotate_horizontally(row,number,direction)

	def get_play_again(self):
		''' Ask the user if he-she wants to start a new game.

		Returns
		-------
		bool
			True if success, False otherwise.

		'''
		while True:
			answer = (input(messages["play_again"])).lower()
			if answer in bool_answers:
				if answer == "yes":
					return True
				elif answer == "no":
					return False
			print(messages["invalid_play_again_option"])

	def end_current_game(self):
		''' If the player wants to end the game, sets the variable start_again 
			to True. Otherwise exit the game.

		'''
		if self.get_play_again():
			self.start_again = True
		else:
			exit_game()

	def read_command(self):
		'''' Reads a command from standard input. Only 'rotate', 'word', 'help', 
			'exit' are valid. Calls the corresponding function to execute each 
			command.

		'''
		is_valid = False
		while not is_valid:
			command = (input(messages["insert_command"])).lower()
			if command in commands:
				if command == "help":
					inst.display()
				elif command == "exit":
					self.end_current_game()	
				elif command == "rotate":
					self.get_rotation_attr()
				elif command == "find":
					self.find_word()
				return None
			else:
				print(messages["invalid_command"])

	def turn(self):
		''' Manages the turns of the player. Call the function to read the
			commands, and display the current state of the game. 

		'''
		print (messages["separator"])
		self.board.display()
		self.clue.display()
		self.read_command()

	def play_again(self):
		''' Return if the player wants to play again.

		Returns
		-------
		bool
			True if the player wants to play again. False otherwise.

		'''
		return self.start_again

class SinglePlayer(Game):

	def __init__(self):
		self.player = None

	def add_player(self,player):
		pass

	def display_current_state(self):
	# Display the board, the list of words according to the clue
		pass

	def restart(self):
	# Version 1.0
		pass


class PracticeMode(SinglePlayer):
	''' Single player mode of game implemented on version 1. 
		Subclass managing specific behaviours of the game.

	'''

	def is_win (self):
		''' Check the winning condition.

		Returns
		-------
		bool
			True if success, False otherwhise.

		'''
		return (self.clue.found_all_the_words())

	def play(self):
		''' 
			Manage the gameplay. Handle the turns.
		'''
		self.start_again = False
		while not self.start_again:
			self.turn()
			if self.is_win():
				print(messages["win"])
				self.end_current_game()
		
	def restart(self):
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

# Dictionary of words.
dictionary = Dictionary()

# Class game.
game = PracticeMode()

# Instructions of the game
inst = Instruction()

def configure_instructions():
	''' Import the instructions into the program. '''

	inst.import_instruction("./rules/instructions.txt")

def display_initial_message():
	''' Display on the standard output a welcome message.

	'''
	print (messages["welcome"])

def display_menu():
	''' Display on the standard output a welcome message.

	'''
	print (messages["menu"])

def display_single_player_modes():
	print (messages["single_player_modes"])

def get_player_nickname():
	pass


def setup():
	pass

def start_game():
	''' Start the game. '''

	os.system('clear')
	display_initial_message()
	input(messages["enter_to_continue"])
	os.system('clear')

	option = ''
	while(option != 'p'):
		display_menu()
		option = input(messages["insert_menu_action"])
		option = option.lower()
		os.system('clear')
		if option == 'h':
			inst.display()
			print(messages["separator"])
		elif option == 'e':
			messages["exit_game"]
			exit()
		elif option != 'p':
			print(messages["invalid_menu_option"])

	print(messages["setting_up"])
	time.sleep(2)
	os.system('clear')
	game.setup()
	os.system('clear')
	print(messages["starting"])
	time.sleep(2)
	os.system('clear')
	game.play()

def exit_game():
	''' Display an exit message and exit the program. 

	'''
	print (messages["exit_game"])
	exit()

def main():
	''' Main function of the program 

	'''

	configure_instructions()
	correct = dictionary.load()
	if not correct:
		print(messages["error"])
		exit()
	play_again = True
	while play_again:
		start_game()
		play_again = game.play_again()

if __name__ == '__main__':
  main()
