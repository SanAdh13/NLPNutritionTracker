# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

# Python program to translate
# speech to text and text to speech
import speech_recognition as sr

r = sr.Recognizer()
def speech():
	try:
		with sr.AudioFile('temp/audio.wav') as source:
			# r.adjust_for_ambient_noise(source)
			audio2 = r.record(source)
			text = r.recognize_google(audio2)
			return text
			
	except Exception as e: 
		return "Sorry I couldnt catch that"

if __name__ == "__main__":
	speech()





# TODO: look into self implementation of the speechtotext or whisper ai ?

	



