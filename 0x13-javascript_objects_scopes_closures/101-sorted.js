#!/usr/bin/node
const { dict } = require('./101-data');

const newDict = {};

Object.keys(dict).forEach((key) => {
  const occurrences = dict[key];
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(key);
});

console.log(newDict);
