# Student Name: Semen Mordovin
# Student ID: 29403413
# Start Date: 20.05.2018
# Last Mod Date: 24.05.2018

import re

"""
Function created to receive unprocessed plain text text and using regular 
expressions conduct the number of pre-processing tasks to make necessary changes
according to the task requirements. Returns final pre-processed form of a text.
"""
def preprocessLine(inputLine):
	# preprocess the data in each line
	# write your code here
	first_form = re.sub("&amp;", "&", str(inputLine))
	second_form = re.sub("&quot;'", '"', first_form)
	third_form = re.sub("&apos;", '’', second_form)
	fourth_form = re.sub("&gt;", ">", third_form)
	fifth_form = re.sub("&lt;", "<", fourth_form)
	sixth_form = re.sub("&#xA;", " ", fifth_form)
	seventh_form = re.sub("&#xD;", " ", sixth_form)
	eight_form = re.sub('”', "", seventh_form)
	ninth_from = re.sub('"', "", eight_form)
	final_form = re.sub("<.*?>", "", ninth_from)
	return final_form


"""
Open raw xml file for reading, striping in on big chunk of data, converting to
string ( easier to avoid possible errors working with one data type), applying
variables to look for answers and questions in text via their id numbers,each 
found Body of answers and questions then pre-processed via our preProcess line 
function and written it two separate text files as prescribed. Utf-8 encoding
used to work with XML type of files.  
"""
def splitFile(inputFile, outputFile_question, outputFile_answer):
	# preprocess the original file, and split them into two files.
	# please call preprocessLine() function within this function
	# write you code here
	with open(inputFile, "r", encoding="utf-8") as raw_file:
		for data in raw_file:
			data = data.strip()
			answer_id = 'PostTypeId="2"'
			question_id = 'PostTypeId="1"'
			if answer_id in data:
				all_answers = re.findall('Body="(.*)/>', data)
				for each_answer in all_answers:
					answer_processed = preprocessLine(each_answer)
					with open(outputFile_answer, "a+", encoding="utf-8") \
						as answers_file:
						answers_file.write(answer_processed + "\n")
						answers_file.close()  # good practice in Python
			elif question_id in data:
				all_questions = re.findall('Body="(.*)/>', data)
				for each_question in all_questions:
					questions_processed = preprocessLine(each_question)
					with open(outputFile_question, "a+", encoding="utf-8") \
						as questions_file:
						questions_file.write(questions_processed + "\n")
						questions_file.close()  # good practice in Python


if __name__ == "__main__":

	f_data = "data.xml"
	f_question = "question.txt"
	f_answer = "answer.txt"

	splitFile(f_data, f_question, f_answer)
