#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function getCharacter (character) {
  request(character, (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
    }
  });
}

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;
    for (const character of characters) {
      getCharacter(character);
    }
  } else {
    console.log('code:', res.statusCode);
  }
});
