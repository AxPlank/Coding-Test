/*
백준 10813: 바구니 뒤집기
https://www.acmicpc.net/problem/10811
*/

const fs = require('fs');
const input = fs.readFileSync("../inputt.txt").toString().trim().split("\r\n");

const [N, M] = input[0].split(" ").map(e => parseInt(e));
let MArr =  input.slice(1).map(e => e.split(" ").map(el => parseInt(el)));
let Boxes = Array(N).fill(0).map((e, i) => {return i+1;});
let tmp;

for (let i = 0; i < M; i++) {
    if (MArr[i][0] != MArr[i][1]) {
        tmp = Boxes.slice(MArr[i][0]-1, MArr[i][1]).reverse();
        Boxes = Boxes.map((e, idx) => {
            if (idx >= MArr[i][0]-1 && idx < MArr[i][1]) {
                return tmp[idx-MArr[i][0]+1];
            } else {
                return e;
            }
        });
    }
}

console.log(...Boxes);