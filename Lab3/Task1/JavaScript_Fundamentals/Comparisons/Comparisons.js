"use strict";
let output1 = 5 > 4;// true
let output2 = "apple" > "pineapple";//false
let output3 = "2" > "12";// true
let output4 = undefined == null;// true
let output5 = undefined === null;// false
let output6 = null == "\n0\n";// false
let output7 = null === +"\n0\n";// false
null === +"\n0\n"
alert("Outputs:\n1: " + output1 + "\n" +
      "2: " + output2 + "\n" +
      "3: " + output3 + "\n" +
      "4: " + output4 + "\n" +
      "5: " + output5 + "\n" +
      "6: " + output6 + "\n" +
      "7: " + output7);