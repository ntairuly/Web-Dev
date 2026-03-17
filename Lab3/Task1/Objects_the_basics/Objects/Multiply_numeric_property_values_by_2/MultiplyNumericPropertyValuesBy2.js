"use strict";
// before the call
let menu = {
  width: 200,
  height: 300,
  title: "My menu"
};

multiplyNumeric(menu);

// after the call
for (let key in menu){
    alert(menu[key]);
    }

function multiplyNumeric(obj){
    for (let key in obj){
        if (typeof(key) === "number"){
            obj[key] *= 2;
            
        }
        alert("here")
    }
}