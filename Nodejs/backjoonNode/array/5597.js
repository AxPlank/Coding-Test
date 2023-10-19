/*
백준 4344: 평균은 넘겠지
https://www.acmicpc.net/problem/4344
*/

// Sol 1
var fs = require('fs');
var input = fs.readFileSync("../inputt.txt").toString().trim().split('\r\n')
    .map(e => parseInt(e));

let HWnotArr = [];

for (let i = 1; i < 31; i++) {
    if (!input.includes(i)) {
        HWnotArr.push(i);

        if (HWnotArr.length === 2) {
            console.log(HWnotArr.join("\n"));

            break;
        }
    }
}

// Sol 2
var fs = require('fs');
var input = fs.readFileSync("/dev/stdin").toString().trim().split("\n").map(e => parseInt(e));

let cnt = 0;

for (let i = 1; i < 31; i++) {
    if (!input.includes(i)) {
        console.log(i);
        cnt++;
        
        if (cnt === 2) break;
    }
}