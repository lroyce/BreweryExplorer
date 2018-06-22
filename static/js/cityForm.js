$(document).ready(function(){

////////http://jsfiddle.net/kbwood/DLprk/////////
//for loading iframe on button click ///////////
  // $('#load').click(function() {
  //   $('#display').attr('src', $('#url').val());
  // });

//class on all the buttons
//grab the id of the url
//and then fill the iframe src

$('.form-button-map').click(function() {
    const a = $(this).attr("id");
    $('#display').attr('src', (a));
  });


  // $load.click(function() {
  //   $('#display').attr('src', $('#url').val());
  // });




})
