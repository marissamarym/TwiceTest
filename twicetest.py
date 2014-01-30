#twicetest.py
#Marissa Montgomery

#myJumble takes in a word and returns a list of all the words the
#input can be jumbled to make
def myJumble(input):
	myDictionaryList = []
	fileIn = open('pythonwords copy.txt')
	for line in fileIn:
		myDictionaryList.append(line.strip())
	list = []
	if len(input) == 0:
		return 
	if len(input) == 1:
		return input
	else:
		i = 0
		while i < len(input):
			list.append(input[i])
				#go through everything in recursive jumble,
				#add current letter to everything at the beginning of the 
				#recursive list
			for each in myJumble(input[:i] + input[i+1:]):
				if (input[i] + each) in myDictionaryList:
					list.append(input[i] + each)
			i += 1
		return list

x = raw_input('What word would you like to jumble?')
print myJumble(x)
