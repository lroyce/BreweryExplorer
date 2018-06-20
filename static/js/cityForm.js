$(document).ready(function(){
  const $city = $('#city-search').val();


  $("button").click(function(){
    $.post("demo_test.asp", function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });
});




  // $form.submit(function(e) {
  //   e.preventDefault(); // do not submit form
  //
  //   $.POST('/save/', {brewery_city: $city})
  //
  // });
}
