#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2).map(Number); // Convert arguments to numbers
  console.log(list.sort((a, b) => b - a)[1]); // Get the second largest number
}
