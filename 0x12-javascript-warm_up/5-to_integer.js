#!/usr/bin/node
const number = process.argv[2];
const newNumber = +number;
if (isNaN(newNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${newNumber}`);
}
