#James Pickles 2016

#libraries to import
import os
import csv
import random

#Function to clear the screen
#DOES NOT WORK IN EDITOR, ONLY IN CONSOLE
def clear():
	os.system('cls')
clear()

print("James Pickles 2016")
print("""
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/
""") 
input("\nPRESS ENTER TO PLAY")
clear()

#Shows word lists available to use
print("""
Available Word Lists
--------------------""")

#Scans the "word_lists" folder for csv files
word_lists = os.listdir("word_lists")
#repeats for every csv file in the folder
for wordlist in word_lists:
	#separates the path from the filename
	(filepath, filename) = os.path.split(wordlist)
	#separates the filename from the extension
	(shortname, extension) = os.path.splitext(filename)
	#prints filename without extension
	if extension == ".csv":
		print(shortname)
#prints a new line
print("\n")

#asks user to select a word list
wordlist_name = str(input("Please select a word list: "))
#appends the csv extension to the filename
wordlist_filename = wordlist_name+".csv"
#appends the folder to the filename with extension to create the full path
wordlist_path = os.path.join("word_lists",wordlist_filename)

#Open word list csv as read only
wordlist_csv = open(wordlist_path, 'r')
#initialize csv reader for word list csv
reader = csv.reader(wordlist_csv, delimiter=' ')
#set word count to 0
word_count = 0
#create list to store words in plain text
wordlist = []
for row in reader:
	#cleans word in csv to plain text (removes brackets etc)
	row_text = ','.join(row)
	#adds word to plain text word list
	wordlist.append(row_text)
#generates a random number in the range of the word list
word_number = random.randint(1,len(wordlist))
#finds word in list that matches the random number index
word = wordlist[word_number].upper()

print("\nRandom word selected from {0}".format(wordlist_name))

word_length = len(word)

wordletters = list(word)

display = list(wordletters)

for n in range(0,word_length):
	if wordletters[n] == ",":
		display[n] = ","
	else:
		display[n] = "_"
	n = n+1

textdisplay =" ".join(display)

input("PRESS ENTER TO PLAY")
clear()

hangman_pics =[
"""
______
|/   |
|    O
|   \\|/	
|    |
|   / \\
|
==========
""",

"""
______
|/   |
|    O
|   \\|/	
|    |
|   / 
|
==========
""",

"""
______
|/   |
|    O
|   \\|/	
|    |
|    
|
==========
""",

"""
______
|/   |
|    O
|   \\|	
|    |
|   
|
==========
""",

"""
______
|/   |
|    O
|    |	
|    |
|   
|
==========
""",

"""
______
|/   |
|    O
|    	
|    
|   
|
==========
""",

"""
______
|/   |
|    
|    	
|    
|   
|
==========
""",

"""
______
|/   
|    
|    	
|    
|   
|
==========
""",

"""
|  
|    
|    	
|    
|   
|
==========
""",

"""
==========
""",

"""""",
]

validinput = []
with open("config/validinput.txt", "r") as f:
	validinput = f.read().replace("\n","")
	validinput = list(validinput)

lives = 10
GameActive = True
GuessedLettersList = []

clear()

while GameActive == True:
	clear()
	GuessedLetters = " ".join(GuessedLettersList)
	print("Hangman")
	print("Lives Remaining {0}.".format(lives))
	print(hangman_pics[lives])
	print("Guessed Letters: {0}\n".format(GuessedLetters))
	print(textdisplay)
	GuessActive = True
	while GuessActive == True:
		guess = input("\nGuess a Letter: ").upper()
		if guess in GuessedLettersList:
			print("Already Guessed {0}, please choose another letter".format(guess))
		elif guess not in validinput:
			print("Invalid Input, please try again.")
		elif guess in wordletters:
			GuessActive = False
			GuessedLettersList.append(guess)
			for l in range(0,len(wordletters)):
				if guess == wordletters[l]:
					display[l] = guess
					textdisplay =" ".join(display)
		elif guess not in wordletters:
			GuessActive = False
			lives = lives - 1
			GuessedLettersList.append(guess)

	if display == wordletters:
		clear()
		print("\n"+textdisplay)
		print("YOU WIN! Your score is {0}".format(lives))
		GameActive = False

	if lives == 0:
		clear()
		print(hangman_pics[lives])
		print("Guessed Letters: {0}\n".format(GuessedLetters))
		print(textdisplay)
		print("\nGame Over! The word was {0}.".format(word))
		GameActive = False

input("\nPRESS ENTER TO EXIT")