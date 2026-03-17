"use strict";
let i = 0;
while (i != 10) {
  i += 0.2;
}//this loop would never end because of js precision
//it would approximately equal 9.999923231312313446787897 and so it goes up to 10+ and never ends