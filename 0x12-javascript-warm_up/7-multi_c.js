#!/usr/bin/node

const language = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrence');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(language);
  }
}
