# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

# Python program to translate
# speech to text and text to speech
import speech_recognition as sr
import Database as db
import NER 
# Initialise
r = sr.Recognizer()

def speech():
		# use the microphone as source for input.

	while(1):
		try:	
			with sr.Microphone() as source:
				r.adjust_for_ambient_noise(source)
				
				#listens for the user's input
				audio2 = r.listen(source)
				
				# Using google to recognize audio
				text = r.recognize_google(audio2)
				text = text.lower()

				print("Did you say '"+text+" '")
				userConfirm = input("Yes/No: ")

				if(userConfirm.lower() == "yes" or userConfirm.lower() == "y"):
					# print("Success")
					NER.ner(text)
				else:
					# print("Try again")
					speech()  #recursion yay 😵‍💫
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
			
		except sr.UnknownValueError:
			print("unknown error occured")
if __name__ == "__main__":
	speech()







	



