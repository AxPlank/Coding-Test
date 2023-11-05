/*
백준 9086: 문자열
https://www.acmicpc.net/problem/1152
*/

const fs = require('fs');
const input = fs.readFileSync("../inputt.txt").toString().trim().split('\r\n');

const T = praseInt(input[0]);
const strArr = input.slice(1);

for (let i = 0; i < T; i++) {
    console.log(`${strArr[i][0]}${strArr[i][strArr[i].length-1]}`);
}