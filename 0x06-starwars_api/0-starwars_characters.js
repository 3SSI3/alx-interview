#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const options = {
  url: `https://swapi.dev/api/films/${movieId}/`,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (!error) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    printCharacters(characters, 0);
  } else {
    console.error('Error:', error);
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], function (charError, charResponse, charBody) {
    if (!charError) {
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      printCharacters(characters, index + 1);
    } else {
      console.error('Error fetching character:', charError);
    }
  });
}