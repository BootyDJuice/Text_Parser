# Student Name: Semen Mordovin
# Student ID: 29403413
# Start Date: 22.05.2018
# Last Mod Date: 24.05.2018

import numpy as np
import matplotlib as plt
from parser_29403413 import Parser
import pandas as pd

"""
Using this function to Visually represent number of posts and vocabulary size
via numpy and Matplotlib, inputFile presented with our "data.xml file"""
def visualizeWordDistribution(inputFile, outputImage):
	ele0_10 = []
	ele10_20 = []
	ele20_30 = []
	ele30_40 = []
	ele40_50 = []
	ele50_60 = []
	ele60_70 = []
	ele70_80 = []
	ele80_90 = []
	ele90_100 = []
	other_ele = []
	with open(inputFile, 'r', encoding='utf-8') as raw_text:
		vocabulary = []
		for line in raw_text:
			parsed_line = Parser(line)
			data = parsed_line.getVocabularySize()
			vocabulary.append(data)

		for each in vocabulary:
			if 0 <= each <= 10:
				ele0_10.append(each)
			elif 10 <= each <= 20:
				ele10_20.append(each)
			elif 20 <= each <= 30:
				ele20_30.append(each)
			elif 30 <= each <= 40:
				ele30_40.append(each)
			elif 40 <= each <= 50:
				ele40_50.append(each)
			elif 50 <= each <= 60:
				ele50_60.append(each)
			elif 60 <= each <= 70:
				ele60_70.append(each)
			elif 70 <= each <= 80:
				ele70_80.append(each)
			elif 80 <= each <= 90:
				ele80_90.append(each)
			elif 90 <= each <= 100:
				ele90_100.append(each)
			elif 100 < each:
				other_ele.append(each)
		# Extending final lists with all collected data via created lists before
		final_elements_list = []
		final_elements_list.extend([len(ele0_10), len(ele10_20), len(ele20_30), len(ele30_40), len(ele40_50)])
		final_elements_list.extend([len(ele50_60), len(ele60_70), len(ele70_80), len(ele80_90), len(ele90_100)])
		final_elements_list.extend([len(other_ele)])

		# Working with x_axis and y_axis to create matplotlib visualization graph
		number_of_posts	 = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70',
				 '70-80', '80-90', '90-100', 'others']
		y_axis = np.arange(len(number_of_posts))
		plt.bar(y_axis, final_elements_list, align='center', alpha=0.5)
		plt.xticks(y_axis, number_of_posts)
		plt.ylabel('Number of posts')
		plt.title('Vocabulary size')

		# received image is returned and saved as .png
		return plt.savefig(outputImage)

"""
Can not finished this part on time, but idea was to Pandas DataFrame to represent
diagram to complete this trend number task"""
#def visualizePostNumberTrend(inputFile, outputImage):
	#write your code here

	#df = pd.DataFrame.from_dict(self.calculated_data)
	#some = df.plot.bar()

	#some.set_ylabel('Meaning score')
	#some.set_xlabel('Indicators')
	#some.set_title('Researching results')

	#plt.subplots_adjust(bottom=0.25)

	#plt.savefig('result.png', dpi=400)
	#plt.show()"""


if __name__ == "__main__":

	f_data = "data.xml"
	f_wordDistribution = "wordNumberDistribution.png"
	f_postTrend = "postNumberTrend.png"
	
	visualizeWordDistribution(f_data, f_wordDistribution)
	#visualizePostNumberTrend(f_data, f_postTrend)
