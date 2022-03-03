import random
from replit import db

def wordlist():
  return [
    "ALITA","AMANO","ANGEL","APRIL",
    "ASOGI","ATMEY","AUCHI",
    "BADGE","BAROK","BASIL","BENCH","BERRY",
    "BLOOD","BLUFF","BYRDE","BYRNE",
    "CAMMY","CASES","CHIEF","CINDY",
    "COURT","CRIME","CYKES",
    "DAMON","DARKE","DEATH","DIEGO",
    "ELISE","ENOCH","FILCH","FRANK","FURIO",
    "GAVEL","GAVIN","GLASS",
    "GODOT","GOURD","GRAPE","GUILT",
    "HOTTI","INPAX","JUDGE","JUNIE","JUROR",
    "LANCE","LARRY","LEGAL",
    "LOCKS","LOGIC","LOTTA","LUNCH",
    "KARMA","KLINT","KNIFE",
    "MACHI","MAGIC","MANNY","MASON",
    "MEANS","METIS",
    "MILES","MINEY","MISTY",
    "PAYNE","PEARL","PENNY",
    "PHOTO","PIANO","POLLY","PONCO","PRINT",
    "RHODA","ROBIN",
    "SCENE","SHADI","SHOOT","SIMON","SITHE",
    "SORIN","SPARK","SPEAR",
    "STAGE","STAND","STARR","STEEL",
    "TENMA","TERRY","THENA","THIEF",
    "TIALA","TIGRE","TRIAL","TRUCY",
    "UNCLE","VIGIL","VIOLA",
    "WENDY","WOCKY","WOODS","YANNI","YUJIN"
  ]

def reset():
  word=random.choice(wordlist())
  db["aceattordle"]=[word,0]
  return word

def processGuess(guess):
  guess = guess.strip().upper()
  if len(guess)<5:
    return "Guess a 5-letter word."

  #expecting db["aceattordle"] = [word,guesses]
  if "aceattordle" in db.keys():
    word = db["aceattordle"][0]
  else:
    word=reset()

  solved=1
  msg=""
  for i in range(5):
    if guess[i]==word[i]: msg=msg+":green_square:"
    elif guess[i] in word: 
      msg=msg+":yellow_square:"
      solved=0
    else: 
      msg=msg+":black_large_square:"
      solved=0

  guesses = db["aceattordle"][1]+1
  if solved==1:
    msg = msg+"\nCongratulations!"
    msg = msg+"\nGuesses: "+ str(guesses)
    reset()
  else:
    msg = msg+"\nGuesses: "+ str(guesses)
    db["aceattordle"]=[word,guesses]

  #print(word,guesses)

  return msg

  
  
  