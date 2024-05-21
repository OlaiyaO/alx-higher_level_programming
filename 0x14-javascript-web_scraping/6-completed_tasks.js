#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId] = 0;
        }
        completedTasksByUser[todo.userId]++;
      }
    });

    console.log(completedTasksByUser);
  } else {
    console.error('Error:', error);
  }
});
