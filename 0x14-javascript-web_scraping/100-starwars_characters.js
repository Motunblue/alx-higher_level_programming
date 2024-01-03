#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;
    for (const character of characters) {
      request(character, (err, res, body) => {
        if (!err) {
          const car = JSON.parse(body);
          console.log(car.name);
        }
      });
    }
  } else {
    console.log('code:', res.statusCode);
  }
});
