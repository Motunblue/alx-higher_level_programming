#!/usr/bin/node
const argv = +(process.argv)[2];
if (isNaN(argv)) {
  console.log('Missing size');
} else {
  console.log('X'.repeat(argv));
}
