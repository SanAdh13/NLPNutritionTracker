//https://codepen.io/Bes7weB/pen/bzbVEd?editors=1011
var $ = jQuery; 
$(document).ready(function(){
    // On modal click, determine where the click occurs and set the variable accordingly
    $('#foodModal').on('click', function (e) {
  
      if ($(e.target).parent().attr("data-bs-dismiss")){
        modalClosingMethod = "by Corner X";
      }
      else{
        modalClosingMethod = "by Background Overlay";
      }
    });
  
    // Modal hidden event fired
    $('#foodModal').on('hidden.bs.modal', function () {
    //   console.log("Modal closed "+modalClosingMethod);
      cancelRecording()
    });
  });

//this js file is just to check if the modal has been closed 
// just for usecase
// if a user starts recording but closes the modal it should count as cancelling the recording hence this  
// from my testing, the cases when this works is
//  when user starts recording -> stops -> closes modal = the audio is removed so modal state is back to default (record and close option  enabled, others disabled)
// when user starts recording -> closes modal = audio deleted (this was the actual reason this was implemented so that it doesnt keep recording in background)
// user starts recording -> stops recording -> submit; should be the only successful case

