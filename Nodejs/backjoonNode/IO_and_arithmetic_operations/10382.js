/*
백준 10382번: 꼬마 정민
https://www.acmicpc.net/problem/10382
*/

const fs = require('fs');
const [A, B, C] = fs.readFileSync('/dev/stdin').toString().trim().split(" ").map(e => parseInt(e));

console.log(A + B + C);