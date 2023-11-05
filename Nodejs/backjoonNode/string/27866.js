/*
백준 27866: 문자와 문자열
https://www.acmicpc.net/problem/27866
*/

const fs = require('fs');
let [strInput, strIdx] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

console.log(strInput[parseInt(strIdx)-1]);