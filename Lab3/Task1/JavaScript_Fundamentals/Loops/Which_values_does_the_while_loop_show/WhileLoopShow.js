"use strict";
let i = 0;
while (++i < 5) alert( i );//1 2 3 4
i = 0;
while (i++ < 5) alert( i );//1 2 3 4 5 because i is old value and in 5th incrementation it is 4<5 so it implements