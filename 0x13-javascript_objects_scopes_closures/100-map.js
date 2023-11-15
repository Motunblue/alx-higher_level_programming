#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map((cv, idx) => {
  return cv * idx;
});

console.log(list);
console.log(newList);
