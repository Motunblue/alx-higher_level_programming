#!/usr/bin/node
const argv = process.argv;
if (argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (argv[2] > 0) {
    console.log('C is fun');
    argv[2]--;
  }
}
