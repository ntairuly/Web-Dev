"use strict";
function pow(x,n){
    let result = 1;
    if(n>=1){
        for(let i = 0 ;i < n;i++){
            result *= x;
        }
        return result;
    }
    return `Power ${n} is not supported, use a positive integer`;
}
let x = prompt("x?","")
let n = prompt("n?","")
alert(pow(x,n));