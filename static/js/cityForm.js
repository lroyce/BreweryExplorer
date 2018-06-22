$(document).ready(function(){

////////http://jsfiddle.net/kbwood/DLprk/////////
//for loading iframe on button click ///////////


$('.form-button-map').click(function() {
    const a = $(this).attr("id");
    $('#display').attr('src', (a));
  });



})
