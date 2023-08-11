#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

axios.get(apiUrl)
  .then(response => {
    const characters = response.data.characters;
    printCharacters(characters, 0);
  })
  .catch(error => {
    console.error('Error:', error.message);
  });

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  axios.get(characters[index])
    .then(charResponse => {
      const characterName = charResponse.data.name;
      console.log(characterName);
      printCharacters(characters, index + 1);
    })
    .catch(charError => {
      console.error('Error fetching character:', charError.message);
    });
}