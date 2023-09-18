/*
백준 10810: 공 넣기
https://www.acmicpc.net/problem/10810
*/

const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\r");

const [N, M] = input[0].split(" ").map(e => parseInt(e));
const MArr = input.slice(1).map(e => e.split(" ").map(el => parseInt(el)));
let Box = Array(N).fill(0);

for (let i = 0; i < M; i++) {
    if (MArr[i][0] === MArr[i][1]) {
        Box[MArr[i][0]-1] = MArr[i][2];
    } else {
        Box.fill(MArr[i][2], MArr[i][0]-1, MArr[i][1]);
    }
}

console.log(...Box);