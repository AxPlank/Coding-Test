/*
백준 10813: 공 바꾸기
https://www.acmicpc.net/problem/10813
*/

const fs = require('fs');
const input = fs.readFileSync("../inputt.txt").toString().trim().split("\r\n");

const [N, M] = input[0].split(" ").map(e => parseInt(e));
const MArr = input.slice(1).map(e => e.split(" ").map(el => parseInt(el)));
let Box = Array(N).fill().map((el, idx) => {return idx + 1});
let tmp;

for (let i = 0; i < M; i++) {
    if (MArr[i][0] != MArr[i][1]) {
        tmp = Box[MArr[i][0]-1];
        Box[MArr[i][0]-1] = Box[MArr[i][1]-1];
        Box[MArr[i][1]-1] = tmp;
    }
}

console.log(...Box);