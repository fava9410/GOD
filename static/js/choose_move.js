$("#playes_choice").steps({
    headerTag: "h3",
    bodyTag: "section",
    transitionEffect: "slideLeft",
    autoFocus: true,
    onFinished: function (event, currentIndex) {
      $("#playes_choice_form").submit();
    }
});
