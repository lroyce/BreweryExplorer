const $form = $('#my-form');
const $favorite = $('#favorite').val();
$(document).ready(function(){
////////http://jsfiddle.net/kbwood/DLprk/////////
//for loading iframe on button click ///////////
  $('#load').click(function() {
    $('#display').attr('src', $('#url').val());
  });



  $('#favorite').click(function() {
    alert($favorite)
    // if ($favorite.val() === 'False') {
    //   $favorite.val('Not Starred')
    }

  })
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
