# This class does some of the breaking down of the line
import copy
import sys
class Word:	
	cv = []
	pron = []
	def __init__(self,cvStr,pronStr):
		cvStr = cvStr.replace('[','')
		self.cv = cvStr.split(']')
		self.cv.remove('')
		pronStr = pronStr.replace('[','')
		self.pron = pronStr.split(']')
		self.pron.remove('\n')
	def getCv(self):
		return self.cv
	def getPron(self):
		return self.pron	
#This is going to be passed a word in CV notation, without syllables, and will generate
#the most likely result.
class Finder:
	cvStr = ""
	list = []
	def __init__(self,cvStr):
		self.cvStr = cvStr
	def listOfValidSubstrings(self, list):
		print ""		
		


#This is some code that creates a dictionary
diction = {}
f = open('./format_data.txt')
for line in f:
	line = line.split('\\')
	diction[line[0]] = Word(line[1],line[2])


#This part finds the percentages of syllables.
sylProbs = {}
sylCount = 0.0
for wrd in diction:
	temp = diction[wrd].getCv()
	for i in temp:
		sylCount += 1.0
		if i in sylProbs:
			sylProbs[i] += 1.0
		else:
			sylProbs[i] = 1.0
for syl in sylProbs:
	sylProbs[syl] = sylProbs[syl]/sylCount


#this breaks a CV structure into all possible syllables
partsOfWord = []
def program(word, partsOfWord):
	listOfSplits.append(partsOfWord)
	for eachPart in partsOfWord:
		if (len(eachPart) > 1):
			i = 1
			while(i < len(eachPart)):
				holder1 = ""
				holder2 = ""
				#holder= eachPart.split(i)
				holder1= eachPart[0:i]
				holder2=eachPart[i:len(eachPart)]
				temp = []
				temp = copy.deepcopy(partsOfWord)
				
				temp.remove(eachPart)
				temp.append(holder1)
				temp.append(holder2)
				program(word,temp)
				i+=1
		#else:
			#do something or maybe nothing?

word = sys.argv[1]

vowels = {'A':0, 'a':0, 'E':0, 'e':0, 'I':0, 'i':0, 'O':0, 'o':0, 'U':0, 'u':0, 'y':0}
tempWord = ""
for char in word:
	if char in vowels:
		tempWord += "V"
	else:
		tempWord += "C"
word = tempWord

array = []
array.append(word)

listOfSplits = []
program(word, array)
#print listOfSplits
bestSequenceHolder = []
bestProbHolder = 0

for combo in listOfSplits:
	tempProbHolder = 1
	for syl in combo:
		if (syl in sylProbs):
			tempProbHolder = tempProbHolder * sylProbs[syl]
		else:
			tempProbHolder = 0
	if tempProbHolder >= bestProbHolder:
		bestSequenceHolder = combo
		bestProbHolder = tempProbHolder
		
print bestProbHolder
print bestSequenceHolder