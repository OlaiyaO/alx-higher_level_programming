#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((_, index) => list[list.length - index - 1]);
};
