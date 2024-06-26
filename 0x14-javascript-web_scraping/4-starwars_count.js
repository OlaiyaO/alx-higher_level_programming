#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith(`/${characterId}/`))
        ? count + 1
        : count;
    }, 0));
  }
});
