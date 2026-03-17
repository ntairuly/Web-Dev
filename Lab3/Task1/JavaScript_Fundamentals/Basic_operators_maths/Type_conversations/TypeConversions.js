"use strict";
let output1 = "" + 1 + 0;//10
let output2 = "" - 1 + 0;//-1
let output3 =true + false;//1
let output4 =6 / "3";//2
let output5 ="2" * "3";//6
let output6 =4 + 5 + "px";//9px
let output7 ="$" + 4 + 5;//$45
let output8 ="4" - 2;//2
let output9 ="4px" - 2;//NaN
let output10 = "  -9  " + 5;//  -9  5
let output11 = "  -9  " - 5;//-14
let output12 = null + 1;//1
let output13 = undefined + 1;//NaN
let output14 = " \t \n" - 2;//-2
alert("Outputs:\n1: " + output1 + "\n" +
      "2: " + output2 + "\n" +
      "3: " + output3 + "\n" +
      "4: " + output4 + "\n" +
      "5: " + output5 + "\n" +
      "6: " + output6 + "\n" +
      "7: " + output7 + "\n" +
      "8: " + output8 + "\n" +
      "9: " + output9 + "\n" +
      "10: " + output10 + "\n" +
      "11: " + output11 + "\n" +
      "12: " + output12 + "\n" +
      "13: " + output13 + "\n" +
      "14: " + output14);