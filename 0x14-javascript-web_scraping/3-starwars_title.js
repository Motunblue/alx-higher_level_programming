#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const jsonres = JSON.parse(body);
    console.log(jsonres.title);
  } else {
    console.log('code:', res.statusCode);
  }
});
