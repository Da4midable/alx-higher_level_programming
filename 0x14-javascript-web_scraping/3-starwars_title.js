#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];

if (!movieID) {
  console.error('Please provide a movie ID as the first argument');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    process.exit(1);
  }

  const data = JSON.parse(body);

  console.log(data.title);
});
