#!/usr/bin/node
const fs = require('fs');

const argv = process.argv;

fs.readFile(argv[2], 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${argv[2]}: ${err}`);
    return;
  }
  fs.readFile(argv[3], 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${argv[3]}: ${err}`);
      return;
    }
    const concat = data1 + data2;
    fs.writeFile(argv[4], concat, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${argv[4]}: ${err}`);
      }
    });
  });
});
