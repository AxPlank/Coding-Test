/*
백준 11718번: 그대로 출력하기
https://www.acmicpc.net/problem/11718
*/

// Sol 1
var fs = require('fs');

var stringList = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

for (let i = 0; i < stringList.length; i++) {
    console.log(stringList[i]);
}

// Sol 2
var fs = require('fs');

var stringList = fs.readFileSync("/dev/stdin").toString().trim().split('\n')
    .map(e => console.log(e));