/*
백준 2444번: 별 찍기-7
https://www.acmicpc.net/problem/2444
*/

const fs = require('fs');
const N = parseInt(fs.readFileSync('/dev/stdin').toString().trim());

for (let i = 1; i <= N; i++) {
    console.log(' '.repeat(N - i) + '*'.repeat(i * 2 - 1));
}

for (let i = N-1; i > 0; i--) {
    console.log(' '.repeat(N - i) + '*'.repeat(i * 2 - 1));
}