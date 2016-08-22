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
#informs user a word has been selected, and notes the use of commas to separate words
print("N.B SPACES BETWEEN WORDS ARE INDICATED AS COMMAS (,)")
print("\nRandom word selected from {0}".format(wordlist_name))
#gets length of selected word
word_length = len(word)
#creates a list containing all the letters of the word, this is static and does not change
wordletters = list(word)

#creates a copy of this list, that can be changed as the user guesses letters.
display = list(wordletters)
#process to setup letter display
for n in range(0,word_length):
	#spaces are indicated as commas
	if wordletters[n] == ",":
		display[n] = ","
	else:
		#sets all letters to blanks, as they have not yet been guessed.
		display[n] = "_"
	n = n+1

#creates a plaintext version of the display, that can be shown to the user, looks much cleaner than a list
textdisplay =" ".join(display)

input("PRESS ENTER TO PLAY")
clear()

#Ascii Illustrations for hangman. The position in the list represents the number of lives left
hangman_pics =[
#0 lives remaining
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
#1 life remaining
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
#2 lives remaining
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
#3 lives remaining
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
#4 lives remaining
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
#5 lives remaining
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
#6 lives remaining
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
#7 lives remaining
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
#8 lives remaining
"""
|  
|    
|    	
|    
|   
|
==========
""",
#9 lives remaining
"""
==========
""",
#10 lives remaining
"""""",
]

#list to define what characters are valid input
validinput = []
#reads from validinput.txt in config folder
with open("config/validinput.txt", "r") as f:
	#removes \n formatting characters to read from the file
	validinput = f.read().replace("\n","")
	#stores valid characters in a list
	validinput = list(validinput)

#Sets player lives - ALERT, IF YOU INCREASE THIS NUMBER, YOU NEED TO ADD A HANGMAN ILLUSTRATION FOR EACH ADDITIONAL LIFE
lives = 10
#boolean variable to keep repeating turns until the game is ends.
GameActive = True
#List of letters that have already been guessed
GuessedLettersList = []

#While the game is running
while GameActive == True:
	#at the start of every turn, clear the screen
	clear()
	#put all guessed letters into easy to read string
	GuessedLetters = " ".join(GuessedLettersList)
	print("Hangman")
	print("Lives Remaining {0}.".format(lives))
	#shows current stage of hangman relative to lives remaining
	print(hangman_pics[lives])
	#displays all letters already guessed
	print("Guessed Letters: {0}\n".format(GuessedLetters))
	#displays the current state of the word guess, with blanks for unknowns and the letters substituted for correct guesses.
	print(textdisplay)
	#Starts guess procedure
	GuessActive = True
	while GuessActive == True:
		guess = input("\nGuess a Letter: ").upper()
		#compares input to letters already guessed
		if guess in GuessedLettersList:
			print("Already Guessed {0}, please choose another letter".format(guess))
		#compares input to valid input characters
		elif guess not in validinput:
			print("Invalid Input, please try again.")
		#if the guess is correct
		elif guess in wordletters:
			GuessActive = False
			#add to guessed letters list
			GuessedLettersList.append(guess)
			#search through word for guessed letter
			for l in range(0,len(wordletters)):
				if guess == wordletters[l]:
					#replace blanks with correct guess
					display[l] = guess
					textdisplay =" ".join(display)
		#if guess incorrect
		elif guess not in wordletters:
			GuessActive = False
			#remove life
			lives = lives - 1
			#add to guessed letters list
			GuessedLettersList.append(guess)

	#if the word is complete
	if display == wordletters:
		clear()
		#show winning screen, calculate score based on lives remaining
		print("Hangman")
		print("\n"+textdisplay)
		print("YOU WIN! Your score is {0}".format(lives))
		GameActive = False
	#if player lost all lives
	if lives == 0:
		clear()
		print("Hangman")
		print("Lives Remaining {0}.".format(lives))
		#display final hangman picture
		print(hangman_pics[lives])
		print("Guessed Letters: {0}\n".format(GuessedLetters))
		print(textdisplay)
		#display game over and the word they were trying to guess.
		print("\nGame Over! The word was {0}.".format(word))
		GameActive = False

input("\nPRESS ENTER TO EXIT")