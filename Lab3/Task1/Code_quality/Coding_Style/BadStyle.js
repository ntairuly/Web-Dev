"use strict";
//Problems:
//1.There is no spaces between (logical and mathematical operators) and variables
//2.There is no space used after ,
//3.There is skipped ; usage
//4.There is enter between (function and if...else) and {}
//5.There is too long string in 1 line
//6(optional).There is no logical block separation between declaration and condition check
//7(optional).There is declared 2 variables in 1 line 
//8(optional). Its obvious functionality of function pow so it should be placed at the end


let x = prompt("x?", '');
let n = prompt("n?", '');

if (n <= 0) {
    alert(`Power ${n} is not supported, please 
        enter an integer number greater than zero`);
} else {
    alert( pow(x, n) );
}

function pow(x, n){
    let result = 1;
    for (let i = 0; i < n; i++){
        result *= x;
    }
    return result;
}