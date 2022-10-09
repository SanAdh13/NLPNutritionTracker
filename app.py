import os
from flask import Flask,render_template,request,url_for,redirect,flash
from flaskext.markdown import Markdown

import SpeechToText as sp2Txt
import NER as ner



app = Flask(__name__)
app.secret_key = 'dd hh' #the secret_key can be anything
app.config["UPLOAD_FOLDER"] = 'C:\\Users\\samad\\Documents\\DISSERTATION\\temp'
Markdown(app)



#landing page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addFood")
def addFood():
    return render_template("addFood.html")


@app.route("/save",methods=['POST'])
def record():
    f = request.files['audio_data']
    with open('temp/audio.wav','wb') as audio:
        f.save(audio)

    #pass the audio recording to speech2text to convert to text
    text = sp2Txt.speech()

    # we use the text gained on the ner model we have and return 
    displacy, dataForDB = ner.ner(text)


    #TODO: add this to the 
     
    return ("Response: "+ displacy) 



@app.route("/track")
def track():
    return render_template("track.html")

if __name__ == "__main__":
    app.run(debug=True)