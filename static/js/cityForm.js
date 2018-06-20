var $iframe = 0;
const $city = $('#city-search').val();
$(document).ready(function(){


  // $("button").click(function(){
  //   $.post("demo_test.asp", function(data, status){
  //       alert("Data: " + data + "\nStatus: " + status);
  //   });
  // });

////////http://jsfiddle.net/kbwood/DLprk/////////
  $('#load').click(function() {
    $('#display').attr('src', $('#url').val());
});




  // $form.submit(function(e) {
  //   e.preventDefault(); // do not submit form
  //
  //   $.POST('/save/', {brewery_city: $city})
  //
  // });
})
