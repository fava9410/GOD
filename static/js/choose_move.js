$( document ).ready(function() {
  table_match_detail = $('#match_detail').DataTable({
    destroy: true,
    ajax:"/rsp/match_detail/"+$("#match").text().split("#")[1]+"/?format=datatables",
    serverSide:true,
    searching: false
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
