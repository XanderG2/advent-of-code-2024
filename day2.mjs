import { readFile } from "node:fs/promises";

const input = await readFile("inputs/day2.txt", "utf8");
const lines = input.split("\r\n");

function everyLine(line) {
  const reports = line
    .split(" ")
    .filter((x) => x.trim() !== "")
    .map(Number);
  let previousReport = null;
  let increase = null;
  let safe = true;
  let safeDampened = 0;

  for (const report of reports) {
    if (increase === null) {
      if (previousReport !== null) {
        if (previousReport > report) {
          increase = false;
        } else if (previousReport === report) {
          safe = false;
          safeDampened++;
        } else {
          increase = true;
        }
      }
    }

    if (previousReport !== null && increase !== null) {
      if (
        (previousReport > report && increase === true) ||
        (previousReport < report && increase === false) ||
        previousReport === report ||
        (increase && previousReport <= report - 4) ||
        (!increase && previousReport >= report + 4)
      ) {
        safe = false;
      }
    }

    previousReport = report;
  }

  return safe;
}

function partOne() {
  let safeTotal = 0;
  for (const line of lines) {
    if (everyLine(line)) {
      safeTotal++;
    }
  }
  console.log(safeTotal);
}

function partTwo() {
  let safeTotal = 0;
  for (const line of lines) {
    if (everyLine(line)) {
      safeTotal++;
      continue;
    }
    for (let i = 0; i < line.split(" ").length; i++) {
      const modifiedLine = line
        .split(" ")
        .filter((_, index) => index !== i)
        .join(" ");
      if (everyLine(modifiedLine)) {
        safeTotal++;
        break;
      }
    }
  }
  console.log(safeTotal);
}

partOne();
partTwo();
