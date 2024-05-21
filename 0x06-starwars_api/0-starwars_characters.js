#!/usr/bin/node
const request = require('request');

function getData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(Error('Error encountered fetching data'));
      }
    });
  });
}

function main () {
  const characterURLS = [];
  const movieId = process.argv[2];
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  const movieData = getData(movieUrl).then(result => { return result; });
  for (const characterURL of movieData.characters) {
    characterURLS.push(getData(characterURL));
  }
  const characters = Promise.all(characterURLS).then((values) => {
    return values;
  });
  for (const character of characters) {
    console.log(character.name);
  }
}
main();
