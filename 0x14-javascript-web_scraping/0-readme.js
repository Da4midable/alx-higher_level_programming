#!/usr/bin/node

const fs = require('node:fs')

console.log('readFile called')

const fileText = process.argv[2]

if (!fileText) {
  console.error('Please provide a file name as an argument')
  process.exit(1)
}

fs.readFile(fileText, 'utf8', function (data) {
  console.log(data)
})
