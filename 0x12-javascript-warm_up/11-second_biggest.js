#!/usr/bin/node
const argv = process.argv;
if (argv.length <= 3) {
  console.log('0');
} else {
  let largest = +argv[3];
  let secondLargest = +argv[2];
  argv.forEach((val) => {
    if (+val > largest) {
      secondLargest = largest;
      largest = +val;
    }
  });
  console.log(secondLargest);
}
