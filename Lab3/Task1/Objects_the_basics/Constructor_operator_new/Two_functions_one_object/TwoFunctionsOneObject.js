"use strict";
//yes it is possible to create functions A and B so that new A() == new B()
//because we just created new object and than just referenced it in this 2 functions 
//in other other words we gave 2 same links to object
let obj = {};
function A() { 
    return obj;
 }
function B() { 
    return obj;
 }

let a = new A();
let b = new B();

alert( a == b ); // true 