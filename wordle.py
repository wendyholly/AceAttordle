import random
from replit import db

def wordlist():
  return [
    "BEARD","SHOUT","CLINK"
  ]

def reset():
  word=random.choice(wordlist())

  letterAry = [0 for i in range(26)]
  letterStr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in range(5):
    charIndex = letterStr.find(word[i])
    letterAry[charIndex] = letterAry[charIndex]+1
    
  db["aceattordle"]=[word,letterAry]
  db["aceattordleguesses"]=0
  return word

def processGuess(guess):
  guess = guess.strip().upper()
  if len(guess)<5:
    return "Guess a 5-letter word."

  #expecting db["aceattordle"] = [word,guesses]
  if "aceattordle" in db.keys():
    word = db["aceattordle"][0]
  else:
    word = reset()

  solved = 1
  msg = ""

  resultAry = [0 for i in range(5)]
  guessLetterAry = [0 for i in range(26)]
  letterAry = db["aceattordle"][1]
  letterStr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  for i in range(5): #this loop handles perfect matches first
    if guess[i]==word[i]: 
      resultAry[i] = 2
      guessLetterAry = incrementChar(guess[i],guessLetterAry)
      
  for i in range(5): #now look for yellow
    if guess[i]==word[i]: continue #green letters already handled

    #if we've already found all instances of a letter
    charIndex = letterStr.find(guess[i])
    if guessLetterAry[charIndex]>=letterAry[charIndex]: continue 
      
    if guess[i] in word:
      resultAry[i] = 1
      guessLetterAry = incrementChar(guess[i],guessLetterAry)

  for i in range(5):
    if resultAry[i]==2: msg=msg+":green_square:"
    elif resultAry[i]==1: 
      msg = msg + ":yellow_square:"
      solved = 0
    else: 
      msg = msg+":black_large_square:"
      solved = 0

  guesses = db["aceattordleguesses"]+1
  if solved==1:
    msg = msg+"\nCongratulations!"
    msg = msg+"\nGuesses: "+ str(guesses)
    reset()
  else:
    msg = msg+"\nGuesses: "+ str(guesses)
    db["aceattordleguesses"] = guesses

  #print(word,guesses)

  return msg

def incrementChar(letter,letterAry):
  letterStr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  charIndex = letterStr.find(letter)
  letterAry[charIndex] = letterAry[charIndex]+1
  return letterAry
