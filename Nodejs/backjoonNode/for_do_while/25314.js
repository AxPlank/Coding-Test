/**
 * 백준 25314번 : 코딩은 체육과목입니다.
 * https://www.acmicpc.net/problem/25314
 */

/**
 * Sol 1
 */
var fs = require('fs');
var N = parseInt(fs.readFileSync('../inputt.txt')) / 4;

let output = Array.from({length : N}, (v, i) => "long");

console.log(`${output.join(" ")} int`);

/**
 * Sol 2
 */
var fs = require('fs');
var N = parseInt(fs.readFileSync('/dev/stdin')) / 4;

let longs = "";
for (let i = 0; i < N; i++) {
    longs += "long ";
}

console.log(`${longs}int`);