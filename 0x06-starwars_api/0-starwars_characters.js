#!/usr/bin/node
const request = require('request');
const movieId = parseInt(process.argv[2]);
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

request(movieUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;
    let completedRequests = 0;
    const characterNames = [];

    for (const characterUrl of characters) {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          characterNames.push(character.name);
        } else {
          console.error('Error fetching character:', error);
        }

        completedRequests++;
        if (completedRequests === characters.length) {
          // All requests have completed, print character names
          characterNames.forEach(name => console.log(name));
        }
      });
    }
  } else {
    console.error('Error fetching movie:', error);
  }
});
