"use strict";
let age = 12;
//with !
if(!(age >=14 && age <=90)){
    alert("Age is NOT between 14 and 90 inclusively.")
}

//without !
if (age <14 || age > 90){
    alert("Age is NOT between 14 and 90 inclusively.")
}