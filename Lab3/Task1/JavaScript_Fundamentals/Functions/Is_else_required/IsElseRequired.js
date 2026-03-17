"use strict";
function checkAge1(age) {
  if (age > 18) {
    return true;
  } else {
    // Work same
    return confirm('Did parents allow you?');
  }
}
function checkAge2(age) {
  if (age > 18) {
    return true;
  }
  // Work same
  return confirm('Did parents allow you?');
}
checkAge1(null);
checkAge2(undefined);