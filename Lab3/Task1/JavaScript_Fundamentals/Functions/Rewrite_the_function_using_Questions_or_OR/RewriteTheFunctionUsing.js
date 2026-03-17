"use strict";
//With if
function checkAge1(age) {
  if (age > 18) {
    return true;
  } else {
    return confirm('Did parents allow you?');
  }
}
//With ?
function checkAge2(age) {
  return (age>18) ? true : confirm('Did parents allow you?');
}
alert(checkAge2(20));
//With ||
function checkAge2(age) {
  return age>18 || confirm('Did parents allow you?');
}
alert(checkAge2(2));
