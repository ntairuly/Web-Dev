"use strict";
function min(a,b){
    if(a<b){
        return a;
    }
    return b;
}
alert(min(2, 5) == 2);
alert(min(3, -1) == -1);
alert(min(1, 1) == 1);