#!/usr/bin/node
const argv = +(process.argv)[2];
let output = ''
if (isNaN(argv)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv; i++) {
    output += 'X';
  }
  console.log(output);
}
