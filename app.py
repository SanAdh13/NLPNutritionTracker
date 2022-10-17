from datetime import datetime
from flask import Flask, jsonify, render_template,request
from itsdangerous import json

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
    # with open('temp/audio.wav','wb') as audio:
    #     f.save(audio)

    #pass the audio recording to speech2text to convert to text
    text = sp2Txt.speech(f)

    # we use the text gained on the ner model we have and return 
    displacy, dataForDB = ner.ner(text)

    db.addToFoodTable(dataForDB)

    return ("""<p>The following detected response has been added to the database</p>
    <p> Response:  """+ displacy) 

#for daily we will have it for the past 5 days , for weekly; for the past 5 weeks , for monthly past 6 months and yearly is gonna be all possible years
data = [{'option':'select option'},
        {'option':'daily'},
        {'option':'weekly'},
        {'option':'monthly'}]
@app.route("/track")
def track():
    return render_template("track.html",data=data)

@app.route("/getGrouped", methods=['POST'])
def getSelection():
    selected = request.form.get('data').lower()

    vals = 0
    if(selected != "select option"):
        if(selected == "daily"):
            vals = db.getFood(5) #last 5 day
        elif(selected == "weekly"):
            vals = db.getFood(3) #last 3 weeks
        elif selected == 'monthly':
            vals = db.getFood(2)    
    return jsonify(vals)

@app.route('/getDates', methods=['POST'])
def getSelectionByDate():
    start = request.form.get('from')
    end = request.form.get('to')
    
    # convert the string into the datetime format 
    format = "%Y-%m-%d"
    startDatObj,endDatObj = datetime.strptime(start,format) , datetime.strptime(end,format)
    
    vals = db.getFoodByDateRange(startDatObj.date(),endDatObj.date())
    
    return jsonify(vals)



@app.route('/deleteUser')
def delUser():
    db.deleteUserData() 
    return render_template("index.html")

  
if __name__ == "__main__":
    app.run(debug=True)