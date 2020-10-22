# Student Name: Semen Mordovin
# Student ID: 29403413
# Start Date: 20.05.2018
# Last Mod Date: 24.05.2018


"""Importing function preprocessLine from first template
importing regular expressions library"""

from preprocessData_29403413 import preprocessLine
import re
"""
Main class with constructor Init
"""
class Parser:
	"""docstring for ClassName"""
	def __init__(self, inputString):
		self.inputString = inputString
		self.ID = self.getID()
		self.type = self.getPostType()
		self.dateQuarter = self.getDateQuarter()
		self.cleanBody = self.getCleanedBody()


	def __str__(self): # using magical method to represent data in human
		# readable form
		# print ID, Question/Answer/Others, creation date, the main content
		# write your code here
		return "ID: " + self.ID + "\n" + "Post type: " + self.type + "\n" + \
			   "Creation date quarter: " + self.dateQuarter + "\n" + \
			   "The cleaned body: " + self.cleanBody + "\n" + \
			   "Vocabulary size: " + str(self.getVocabularySize())


	def getID(self):
		# function written to obtain post ID, using regular expressions and on
		# string operations
		id_final = str()
		raw_text = self.inputString
		id_found = re.findall('row Id="(.*)" P', raw_text)
		for id_final in id_found:
			','.join(id_final)
		return id_final


	def getPostType(self):
		# functions coded to obtain type of Post: Answer or Question or Other one
		# Used on string command such as strip to make it easier to work with one
		# bif chunk of data str type data, if statements that are checking for
		# matching data needed and returning legible output
		raw_text = self.inputString.strip()
		answers = 'PostTypeId="2"'
		questions = 'PostTypeId="1"'
		if answers in raw_text:
			return "2"
		if questions in raw_text:
			return "1"
		else:
			return "Other"


	def getDateQuarter(self):
		# function for obtaining Creation Date of a Post, using list to store
		# operational data, matching index for proper output
		first_quarter = "Q1"
		second_quarter = "Q2"
		third_quarter = "Q3"
		fourth_quarter = "Q4"
		date_list = []
		raw_text = self.inputString.strip()
		target_sequence = re.findall('CreationDate="(.*)T', raw_text)
		target_sequence = ','.join(str(digit) for digit in target_sequence)
		for items in target_sequence:
			date_list.append(items)
		if date_list[6] == "1" or date_list[6] == "2" or \
			date_list[6] == "3":
			return target_sequence[0:4] + first_quarter
		elif date_list[6] == "4" or date_list[6] == "5" or \
			date_list[6] == "6":
			return target_sequence[0:4] + second_quarter
		elif date_list[6] == "7" or date_list[6] == "8" or \
			date_list[6] == "9":
			return target_sequence[0:4] + third_quarter
		elif date_list[0] == "1" and date_list[5] == "0" or \
			date_list[0] == "1" and date_list[5] == "1" or \
			date_list[0] == "1" and date_list[5] == "2":
			return target_sequence[0:4] + fourth_quarter


	def getCleanedBody(self):
		# Obtaining clean data using imported function from Task 1, strip and
		# join operations on strings, matching needed data sequences with regular
		# expressions, returns data needed
		target_data_found = str()
		raw_text = self.inputString.strip()
		target_data = re.findall('Body="(.*)/>', raw_text)
		for target_data_found in target_data:
			','.join(target_data_found)
			target_data_found = preprocessLine(target_data_found)
		return target_data_found


	def getVocabularySize(self):
		# Code written to obtain length size of vocabulary, converting list,
		# to set and counting unique elements
		lower_case = str(self.getCleanedBody().lower())
		vocabulary_size = set(lower_case.split())
		return len(vocabulary_size)

# Created string object to test Class perfomance

y = '<row Id="2481" PostTypeId="1" CreationDate="2016-04-07T18:11:33.793" Body' \
	'="&lt;p&gt;In $200 ''price range, should I be looking at cards from AMD ' \
	'or Nvidia?&lt;/p&gt;&#xA;” />'
x = Parser(y)
print(x)


