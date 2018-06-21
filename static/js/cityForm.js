const $form = $('#my-form');
$(document).ready(function(){
////////http://jsfiddle.net/kbwood/DLprk/////////
//for loading iframe on button click ///////////
  $('#load').click(function() {
    $('#display').attr('src', $('#url').val());
  });

const token = $("[name=csrfmiddlewaretoken]").val();
//keeping the city search at the top of the search//


  $('#findcity').click(function(e) {
    // const $city = $(this).attr('name');
    const $city = $('#foo').val();

    // $.post("/brewapi/", function(data, status){
    //   alert("Data: " + data + "Status: " + status);
    //   data: {
    //     csrfmiddlewaretoken: token,
    //     'brewCity': $city,
    //   },
    // })
    const url = $form.attr('action');

    //
    // $.ajax({
    //   url: url,
    //   method: 'POST',
    //   data: {
    //     csrfmiddlewaretoken: token,
    //     brewCity: $city,
    //   },
    //   success: () => {
    //     alert('yay')
    //   },
    //   error: () => {
    //     alert('boo')
    //   }
    // })



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
