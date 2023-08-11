#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie information:', response.statusCode);
    return;
  }

  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (charError, charResponse, charBody) => {
    if (charError) {
      console.error('Error fetching character:', charError);
      return;
    }

    if (charResponse.statusCode !== 200) {
      console.error('Failed to retrieve character information:', charResponse.statusCode);
      return;
    }

    const characterName = JSON.parse(charBody).name;
    console.log(characterName);
    printCharacters(characters, index + 1);
  });
}