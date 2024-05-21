#!/usr/bin/node
const request = require('request');
const movieId = parseInt(process.argv[2]);
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

request(movieUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (const characterUrl of characters) {
      request(characterUrl, function (error, response, body) {
        if (!error) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.log(error);
        }
      });
    }
  } else {
    console.log(error);
  }
});
