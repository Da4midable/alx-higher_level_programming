#!/usr/bin/node

function factorIt (num) {
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorIt(num - 1);
  }
}

const args = process.argv.slice(2);

const num1 = parseInt(args[0]);

if (isNaN(num1)) {
  console.log(1);
} else {
  const result = factorIt(num1);
  console.log(result);
}
