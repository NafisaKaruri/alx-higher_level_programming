#!/usr/bin/node

const dict = require('./101-data.js').dict;
const d = {};
for (const key in dict) {
  if (d[dict[key]] === undefined) {
    d[dict[key]] = [key];
  } else {
    d[dict[key]].push(key);
  }
}

console.log(d);
