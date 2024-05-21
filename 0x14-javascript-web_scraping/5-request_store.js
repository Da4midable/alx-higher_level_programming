#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const apiUrl = process.argv[2];
const filePath = process.argv[3];

if (!apiUrl || !filePath) {
  console.error(`Usage: ./5-request_store.js ${apiUrl} ${filePath}`);
  process.exit(1);
}

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
