#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = args[0];
const secArg = args[1];
const addedArgs = firstArg + ' is ' + secArg;

console.log(addedArgs);
