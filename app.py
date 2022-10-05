from flask import Flask,render_template,request,url_for
from flaskext.markdown import Markdown
from flask_modals import Modal 

from spacy import displacy

import SpeechToText as sp2Txt
import NER as ner


app = Flask(__name__)
Markdown(app)
#landing page
@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/addFood")
# def food():
#     return render_template("addFood.html")

@app.route('/getVoiceRecording',methods=['GET','POST'])
def getVoiceRecording():
    if request.method == 'POST':
        ''' 
            TODO: we will take the voice clip recorded via JS
            and pass it for speech.speech() in order to get {text}  
            and then usse ner.ner({text})
            use displacy to show the extracted ENT
            and then add the relevant ents to db         
        '''


@app.route("/track")
def track():
    return render_template("track.html")

if __name__ == "__main__":
    app.run(debug=True)