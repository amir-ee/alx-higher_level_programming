#!/usr/bin/node

const { argv } = require("process");

let argu = argv;
let c = 0;

for (let i = 0; argu[i] != undefined; i++) {
    c++;
}

if (c == 2) {
    console.log("No argument");
}
else if (c == 3) {
    console.log("Argument found");
}
else {
    console.log("Arguments found");
}

