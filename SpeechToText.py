# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

# Python program to translate
# speech to text and text to speech
from unicodedata import name
import speech_recognition as sr
import Database as db

def speech(r,mic):
		# use the microphone as source for input.
	with sr.Microphone() as source:

		#TODO implement error handling for speechrecog	
			
		# except sr.RequestError as e:
		# 	print("Could not request results; {0}".format(e))
			
		# except sr.UnknownValueError:
		# 	print("unknown error occured")
		
		r.adjust_for_ambient_noise(source)
		
		#listens for the user's input
		audio2 = r.listen(source)
		
		# Using google to recognize audio
		text = r.recognize_google(audio2)
		text = text.lower()

		print("Did you say '"+text+" '")
		userConfirm = input("Yes/No: ")

		if(userConfirm.lower() == "yes" or userConfirm.lower() == "y"):
			print("Success")
			
			# # #db.addTextToTrainingData(text) # # # 
			
		else:
			print("Try again")
			speech(r,mic)  #recursion yay 😵‍💫


# Initialise
r = sr.Recognizer()
mic = sr.Microphone()

speech(r,mic)







	



