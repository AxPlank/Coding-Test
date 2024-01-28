/*
백준 10988번: 팰린드롬인지 확인하기
https://www.acmicpc.net/problem/10988
*/

const fs = require('fs');
const word = fs.readFileSync('/dev/stdin').toString().trim();
const wordReverse = word.split("").reverse().join("");

console.log(wordReverse === word ? 1 : 0);