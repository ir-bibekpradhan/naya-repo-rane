"use strict";

const os = require("os");

const appName = process.env.APP_NAME || "docker-node";
const appEnv = process.env.APP_ENV || "development";

function main() {
  console.log(`=== ${appName} | env=${appEnv} | node=${process.version} ===`);
  console.log(`Platform: ${os.platform()} ${os.release()} ${os.arch()}`);
  console.log("Installed npm dependencies: none");
}

main();
