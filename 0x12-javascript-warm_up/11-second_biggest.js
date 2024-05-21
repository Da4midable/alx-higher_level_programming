#!/usr/bin/node

const args = process.argv.slice(2).map(arg => parseInt(arg));

if (process.argv.length < 4) {
  console.log(0);
} else {
  let maxNumber = Math.max(...args);
  const newArray = args.filter(element => element !== maxNumber);
  maxNumber = Math.max(...newArray);
  console.log(maxNumber);
}
