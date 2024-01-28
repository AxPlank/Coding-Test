/*
백준 25206번: 너의 평점은
https://www.acmicpc.net/problem/25206
*/

const fs = require('fs');
const table = fs.readFileSync('/dev/stdin').toString().trim().split("\n")
    .map(e => e.split(" "));

var demo = 0;
var nume = 0;
var score = { "A+" : 4.5,
         "A0" : 4.0,
         "B+" : 3.5,
         "B0" : 3.0,
         "C+" : 2.5,
         "C0" : 2.0,
         "D+" : 1.5,
         "D0" : 1.0,
         "F" : 0.0 }

for (var i = 0; i < 20; i++) {
    if (table[i][2] != "P") {
        demo += parseFloat(table[i][1]);
        nume += parseFloat(table[i][1]) * score[table[i][2]];
    }
}

console.log(nume / demo);