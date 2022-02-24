var demoBtn = ".nav-link.demo";
var aboutBtn = ".nav-link.about";
var hidden = "hidden";

var aboutDivRightPanel = ".about-div-right";
var aboutDivLeftPanel = ".about-div-left";

var demoDivLeftPanel = ".demo-div-left";
var demoDivRightPanel = ".demo-div-right";

var handleSubmitBtn = "#userHandleSubmitBtn";

var overlay = ".overlay";
var spinner = ".spinner";

// if demo button clicked, hide about
$(demoBtn).click(function() {
  $(aboutDivRightPanel).addClass(hidden);
  $(aboutDivLeftPanel).addClass(hidden);

  $(demoDivLeftPanel).removeClass(hidden);
  $(demoDivRightPanel).removeClass(hidden);

});

// if about button click, hide demo
$(aboutBtn).click(function() {
  $(aboutDivRightPanel).removeClass(hidden);
  $(aboutDivLeftPanel).removeClass(hidden);

  $(demoDivLeftPanel).addClass(hidden);
  $(demoDivRightPanel).addClass(hidden);
});

$(handleSubmitBtn).click(function (e) {
  e.preventDefault();
  
  $(overlay).removeClass("hide-overlay");
  $(spinner).removeClass(hidden);

  var twitterHandleVal = $("#userHandleInputField").val();

  $.ajax({
    url: "/",
    type: "POST",
    data: {
      "user_handle": twitterHandleVal
    },
    success: function(response) {
      // hide overlay + spinner
      $(overlay).addClass("hide-overlay");
      $(spinner).addClass(hidden);

      // show visualization here:

    },
    error: function(err) {
      console.log("err ==>", err);
    },
    timeout: 10000
  });

  $("#userHandleInputField").val("");

});
