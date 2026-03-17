"use strict";
//Function Declaration Method

function ask1(question, yes, no) {
  if (confirm(question)) yes();
  else no();
}

ask1(
  "Do you agree?",
  function() { alert("You agreed."); },
  function() { alert("You canceled the execution."); }
);

//Arrow Function Method
let ask2 = (question, yes, no) => (confirm(question))?yes():no();
ask2(
  "Do you agree?",
  function() { alert("You agreed."); },
  function() { alert("You canceled the execution."); }
);