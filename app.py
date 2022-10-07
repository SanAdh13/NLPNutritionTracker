import os
from flask import Flask,render_template,request,url_for,redirect,flash
from flaskext.markdown import Markdown
from mimetypes import guess_extension


from spacy import displacy
import SpeechToText as sp2Txt
import NER as ner



app = Flask(__name__)
app.secret_key = 'dd hh' #the secret_key can be anything
app.config["UPLOAD_FOLDER"] = 'C:\\Users\\samad\\Documents\\DISSERTATION\\temp'
Markdown(app)

''' 
TODO: we will take the voice clip recorded via JS
and pass it for speech.speech() in order to get {text}  
and then usse ner.ner({text})
use displacy to show the extracted ENT
and then add the relevant ents to db         
'''

#landing page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addFood")
def addFood():
    return render_template("addFood.html")


@app.route("/save",methods=['POST'])
def record():
    if 'file' in request.files:
        file = request.files['file']
        # with open('temp/audio.wav','wb') as audio:
        #     file.save(audio)
        
        # TODO: send this file straight to speechRecog and get converted text
        sp2Txt.speech(file)


    
    return '<h1>Success</h1>'


@app.route("/track")
def track():
    return render_template("track.html")

if __name__ == "__main__":
    app.run(debug=True)