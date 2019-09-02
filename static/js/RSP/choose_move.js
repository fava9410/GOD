$( document ).ready(function() {

  table_match_detail = $('#match_detail').DataTable({
    destroy: true,
    ajax:"/rsp/match_detail/"+$("#match").text().split("#")[1]+"/?format=datatables",
    serverSide:true,
    searching: false
  });

  $('#match_detail').on('error.dt',function(e, settings, techNote, message) {
    alert("Something happened, you will be redirect to the main page, sorry");
    window.location="/home";
  });

  $("#playes_choice").steps({
      headerTag: "h3",
      bodyTag: "section",
      transitionEffect: "slideLeft",
      autoFocus: true,
      onFinished: function (event, currentIndex) {
        $("#playes_choice_form").submit();
      }
  });
});
