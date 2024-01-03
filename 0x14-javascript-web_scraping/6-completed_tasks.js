#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const tasks = JSON.parse(body);
    const taskList = {};
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (taskList[task.userId] === undefined) {
          taskList[task.userId] = 1;
        } else {
          taskList[task.userId]++;
        }
      }
    }
    console.log(taskList);
  } else {
    console.log('code:', res.statusCode);
  }
});
