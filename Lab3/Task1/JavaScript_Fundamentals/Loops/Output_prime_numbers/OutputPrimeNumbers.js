"use strict";
let prime = prompt("Prime numbers from to ",10);
Prime:for(let i = 2;i<=prime;i++){
    for(let j = 2;j<i;j++){
        if(!(i%j)){
            continue Prime;
        }
    }
    alert(i);
}