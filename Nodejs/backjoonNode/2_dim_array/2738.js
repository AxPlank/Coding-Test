/*
백준 2738번: 2차원 배열
https://www.acmicpc.net/problem/2738
*/

const fs = require('fs');
const table = fs.readFileSync('/dev/stdin').toString().trim().split("\n")
    .map(e => e.split(" ").map(el => parseInt(el)));

const N = table[0][0];
let ret = table.slice(1, 1 + N).map((e, i) => {
    return e.map((el, idx) => {
        return el + table[1+i+N][idx];
    }).join(" ");
}).join("\n");

console.log(ret);