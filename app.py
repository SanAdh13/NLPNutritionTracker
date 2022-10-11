from flask import Flask, render_template,request

import SpeechToText as sp2Txt
import NER as ner
import database as db



app = Flask(__name__)
app.secret_key = 'dd hh' #the secret_key can be anything
app.config["UPLOAD_FOLDER"] = 'C:\\Users\\samad\\Documents\\DISSERTATION\\temp'


#landing page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save",methods=['POST'])
def record():
    f = request.files['audio_data']
    with open('temp/audio.wav','wb') as audio:
        f.save(audio)

    #pass the audio recording to speech2text to convert to text
    text = sp2Txt.speech()

    # we use the text gained on the ner model we have and return 
    displacy, dataForDB = ner.ner(text)

    db.addToFoodTable(dataForDB)

    return ("""<p>The following detected response has been added to the database</p>
    <p> Response:  """+ displacy) 

data = [{'option':'daily'},
        {'option':'weekly'},
        {'option':'monthly'},
        {'option':'Yearly'}]
@app.route("/track")
def track():
    #TODO: finish this section of the site



    return render_template("track.html",data=data)

@app.route("/track", methods=['POST'])
def getSelection():
    selected = request.form.get('dateSelection')

    vals = db.getFood()

    return render_template("track.html",data = data, items=vals)

@app.route('/getDates', methods=['POST'])
def getSelectionByDate():
    start = request.form.get('from')
    end = request.form.get('to')

    # get the data within this range from sql and then its returned via ajax
    vals = db.getFoodByDateRange(start,end)

    return "data sent"+start+" "+end
    # return vals

if __name__ == "__main__":
    app.run(debug=True)