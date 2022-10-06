import os
from flask import Flask,render_template,request,url_for,redirect,flash
from flaskext.markdown import Markdown
from flask_modals import Modal 

from spacy import displacy

import SpeechToText as sp2Txt
import NER as ner



app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = 'C:\\Users\\samad\\Documents\\DISSERTATION\\temp'
Markdown(app)

# import speech_recognition as sr
# r = sr.Recognizer()
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
    #TODO: lets see if i can transcribe it in real time when the user presses stop record
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    file_name = "temp.mp3"
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(full_file_name)
    
    return '<h1>Success</h1>'


@app.route("/track")
def track():
    return render_template("track.html")

if __name__ == "__main__":
    app.run(debug=True)