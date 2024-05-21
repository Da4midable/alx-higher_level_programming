#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL as the first argument');
  process.exit(1);
}

const wedgeAntillesId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(response.statusCode);
    process.exit(1);
  }

  const data = JSON.parse(body);

  let wedgeMoviesCount = 0;

  data.results.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
      wedgeMoviesCount++;
    }
  });

  console.log(wedgeMoviesCount);
});
