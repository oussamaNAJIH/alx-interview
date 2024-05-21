#!/usr/bin/node
const request = require('request');

function getData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Request failed with status code: ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function main () {
  const movieId = parseInt(process.argv[2]);
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  try {
    const data = await getData(movieUrl);
    const characters = data.characters;
    const characterPromises = characters.map(characterUrl => getData(characterUrl));

    const characterData = await Promise.all(characterPromises);
    characterData.forEach(character => {
      if (character) {
        console.log(character.name);
      }
    });
  } catch (error) {
    console.error(error);
  }
}

main();
