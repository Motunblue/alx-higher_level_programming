#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const jsonres = JSON.parse(body);
    const results = jsonres.results;
    const charId18 = results.filter((result) => {
      const character = result.characters;
      const c = character.filter((char) => {
        return (char.endsWith('18/'));
      });
      return (c.length > 0);
    });
    console.log(charId18.length);
  } else {
    console.log('code:', res.statusCode);
  }
});
