# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
def speak(mytext):
    #mytext = 'Welcome to geeksforgeeks!'
    # Language in which you want to convert
    language = 'en'
  
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)
  
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("temp.mp3")
  
    # Playing the converted file
    os.system("omxplayer temp.mp3")
    os.system("rm temp.mp3")
    exit()

def pr(text):
    print(text)
    exit()
