// var $iframe = 0;
$(document).ready(function(){
////////http://jsfiddle.net/kbwood/DLprk/////////
//for loading iframe on button click ///////////
  $('#load').click(function() {
    $('#display').attr('src', $('#url').val());
  });

//keeping the city search at the top of the search//
  $('#findcity').click(function(e) {
    // const $city = $(this).attr('name');
    const $city = $('#city-search').val();
    alert($city)
    $('#city-display').val($city)
  })

//   $monster.click(function(e) {
//   var whichMonstClicked = $(this).attr('id');
//   caught(whichMonstClicked);
// });


  // $("button").click(function(){
  //   $.post("demo_test.asp", function(data, status){
  //       alert("Data: " + data + "\nStatus: " + status);
  //   });
  // });

  // $form.submit(function(e) {
  //   e.preventDefault(); // do not submit form
  //
  //   $.POST('/save/', {brewery_city: $city})
  //
  // });
})
