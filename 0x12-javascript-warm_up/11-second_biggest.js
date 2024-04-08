#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const nums = process.argv.slice(2).map(Number);
  const sortedNums = nums.sort((a, b) => b - a);
  console.log(sortedNums[1]);
}
