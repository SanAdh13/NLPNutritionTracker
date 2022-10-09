// https://blog.addpipe.com/using-recorder-js-to-capture-wav-audio-in-your-html5-web-site/
URL = window.URL || window.webkitURL;
var gumStream;                      //stream from getUserMedia()
var rec;                            //Recorder.js object
var input;                          //MediaStreamAudioSourceNode we'll be recording

// shim for AudioContext when it's not avb. 
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext //audio context to help us record


//edit: removed pause button and added submit button
var recordButton = document.getElementById("recordButton");
var stopButton = document.getElementById("stopButton");
var cancelButton = document.getElementById("cancelButton");
var submitButton = document.getElementById("submitButton")
// var pauseButton = document.getElementById('pauseButton')

//adding eventlisteners
recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);
cancelButton.addEventListener("click",cancelRecording)
// submitButton.addEventListener("click",submitRecording)
// pauseButton.addEventListener("click",pauseRecording)

function startRecording() { 

    rec = null;
    // recordButton.src = "/static/img/188-microphone-recording-flat.gif"
    console.log("recordButton clicked");
    /* Simple constraints object, for more advanced audio features see
    https://addpipe.com/blog/audio-constraints-getusermedia/ */

    var constraints = {
        audio: true,
        // video: false
    } 
    /* Disable the record button until we get a success or fail from getUserMedia() */

    // when we start recording disable record and submit 
    // all other buttons are enabled
    recordButton.disabled = true;
    stopButton.disabled = false;
    submitButton.disabled = true;
    // pauseButton.disabled = false;
    cancelButton.disabled = false;

    /* We're using the standard promise based getUserMedia()

    https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia */

    navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
        console.log("getUserMedia() success, stream created, initializing Recorder.js ..."); 
        /* assign to gumStream for later use */
        audioContext = new AudioContext();

		//update the format 
		// document.getElementById("formats").innerHTML="Format: 1 channel pcm @ "+audioContext.sampleRate/1000+"kHz"

        gumStream = stream;
        /* use the stream */
        input = audioContext.createMediaStreamSource(stream);
        /* Create the Recorder object and configure to record mono sound (1 channel) Recording 2 channels will double the file size */
        rec = new Recorder(input, {
            numChannels: 1
        }) 


        //start the recorder too 
        start();

        //start the recording process 
        rec.record()
        console.log("Recording started");
    }).catch(function(err) {
        //enable the record button if getUserMedia() fails 
        recordButton.disabled = false;
        stopButton.disabled = true;
    });

}

function stopRecording() {
    // recordButton.src = "/static/img/188-microphone-recording.svg"
    console.log("stopButton clicked");
    //disable the stop button, enable the record too allow for new recordings 
    stopButton.disabled = true;
    recordButton.disabled = false;
    submitButton.disabled = false;

    //tell the recorder to stop the recording 
    if (rec){
        rec.stop(); //stop microphone access 
        gumStream.getAudioTracks()[0].stop();
        rec.exportWAV(submitRecording);
    }
    //stop the timer
    stop()    
}   

function cancelRecording(){
    // recordButton.src = "/static/img/188-microphone-recording.svg"
    // console.log("cancelButton clicked");

    //this method is called if either the recording is cancelled via pressing the X button 
    // or the modal is closed by clicking outside the box
    if (rec) {
        submitButton.disabled = true;
        stopButton.disabled = true;
        rec.stop();
        gumStream.getAudioTracks()[0].stop();
        rec.clear();
        rec = null;
        console.log(rec)
    }
    //reset timer
    reset();
    document.getElementById("speechToText").innerHTML = "";
}

function submitRecording(blob){
    submitButton.addEventListener("click", function(event) {

        //reset timer
        reset();
        document.getElementById("speechToText").innerHTML = "fetching result: This may take some time";


        //once submitted disable the submit button
        submitButton.disabled=true; 
        var form = new FormData();
        form.append("audio_data",blob,'audio')
        $.ajax({
            type: 'POST',
            url: '/save',
            data: form,
            cache: false,
            processData: false,
            contentType: false
        }).done(function(data) { 

            //this updates the span with the returned text from speechToText
            //TODO: use displacy to show the entities
        document.getElementById("speechToText").innerHTML = data;});
    })

}

function timeToString(time) {
    let diffInHrs = time / 3600000;
    let hh = Math.floor(diffInHrs);
  
    let diffInMin = (diffInHrs - hh) * 60;
    let mm = Math.floor(diffInMin);
  
    let diffInSec = (diffInMin - mm) * 60;
    let ss = Math.floor(diffInSec);
  
    let diffInMs = (diffInSec - ss) * 100;
    let ms = Math.floor(diffInMs);
  
    let formattedMM = mm.toString().padStart(2, "0");
    let formattedSS = ss.toString().padStart(2, "0");
    let formattedMS = ms.toString().padStart(2, "0");
  
    return `${formattedMM}:${formattedSS}:${formattedMS}`;
  }

let startTime;
let elapsedTime = 0;
let timerInterval;
function print(txt) {
    document.getElementById("display").innerHTML = txt;
}
function start() {
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(function printTime() {
    elapsedTime = Date.now() - startTime;
    print(timeToString(elapsedTime));
    }, 10);
}

function stop(){
    clearInterval(timerInterval);
}
function reset(){
    clearInterval(timerInterval);
    print("00:00:00");
    elapsedTime = 0;
}

  