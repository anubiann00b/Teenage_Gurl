from random import randrange

possibleWords = ['like idk', 'omg shut up you are so annoying','just shut up','wat r u tlking about?!','omg','idk','lol']

while(1):
	rInput = raw_input("You >> ")
	print "Katy t3h PeNgU1N oF d00m >> " + possibleWords[randrange(len(possibleWords))]