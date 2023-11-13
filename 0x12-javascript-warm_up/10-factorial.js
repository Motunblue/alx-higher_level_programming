#!/usr/bin/node

function fact (num) {
  if (num === 1) {
    return 1;
  } else {
    return (num * fact(num - 1));
  }
}
const argv = +(process.argv[2]);
if (isNaN(argv)) {
  console.log(1);
} else {
  console.log(fact(argv));
}
