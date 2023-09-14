/*
백준 10807: 개수 세기
https://www.acmicpc.net/problem/10807
*/

const fs = require('fs');

const input = fs.readFileSync("../inputt.txt").toString().trim().split("\r\n");

const N = parseInt(input[0]);
let Arr = input[1].split(" ").map(e => parseInt(e));
const v = parseInt(input[2]);

Arr = Arr.filter(e => v === e);
console.log(Arr.length);