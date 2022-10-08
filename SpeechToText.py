# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

# Python program to translate
# speech to text and text to speech
from email.mime import audio
import speech_recognition as sr

r = sr.Recognizer()
def speech():
	try:
		with sr.AudioFile('temp/n.wav') as source:
			# r.adjust_for_ambient_noise(source)
			audio2 = r.record(source)
			# print(type(audio2))
			# try:
			text = r.recognize_google(audio2)
			print(text)
			
	except Exception as e: 
		print("exception"+str(e))

if __name__ == "__main__":
	speech()







	



