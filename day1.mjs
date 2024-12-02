import { error } from "node:console";
import { readFile } from "node:fs/promises";

const input = await readFile("inputs/day1.txt", "utf8");
const lines = input.split("\r\n");

let leftList = new Array();
let rightList = new Array();

for (const line of lines) {
  const x = line.split("   ");
  leftList.push(parseInt(x[0]));
  rightList.push(parseInt(x[1]));
}

leftList.sort();
rightList.sort();

function zip(list1, list2) {
  if (!(list1.length == list2.length)) {
    console.log("Lists need to be same length!");
    return error;
  }
  let list3 = new Array();
  for (let i = 0; i < list1.length; i++) {
    list3.push([list1[i], list2[i]]);
  }
  return list3;
}

function count(arr, n) {
  let appearences = 0;
  arr.forEach((x) => {
    if (x == n) {
      appearences += 1;
    }
  });
  return appearences;
}

function partOne() {
  const pairs = zip(leftList, rightList);
  let sum = 0;
  for (const n of pairs) {
    const difference = Math.abs(n[0] - n[1]);
    sum += difference;
  }
  console.log(sum);
}

function partTwo() {
  let sum = 0;
  for (const n of leftList) {
    const appearences = count(rightList, n);
    sum += appearences * n;
  }
  console.log(sum);
}

partOne();
partTwo();
