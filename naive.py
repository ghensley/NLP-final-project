class Word:	
	cv = []
	pron = []
	def __init__(self,cvStr,pronStr):
		cvStr = cvStr.replace('[','')
		self.cv = cvStr.split(']')
		pronStr = pronStr.replace('[','')
		self.pron = pronStr.split(']')	
	def getCv(self):
		return self.cv
	def getPron(self):
		return self.pron	
		
diction = {}
f = open('./format_data.txt')
for line in f:
	line = line.split('\\')
	diction[line[0]] = Word(line[1],line[2])	
print diction['checkers'].getCv()
print diction['checkers'].getPron()
