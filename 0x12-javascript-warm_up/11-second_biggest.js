#!/usr/bin/node
const argv = process.argv;
if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log(0);
} else {
  let largest = argv[2];
  let secondLargest = argv[3];
  argv.forEach((val) => {
    if (val > largest) {
      secondLargest = largest;
      largest = val;
    }
  });
  console.log(secondLargest);
}
