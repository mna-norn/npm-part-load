'use strict';

// Author: Nikolay A. Merezhko (norn)
//
// Script for load list of NPM packages

const NpmApi = require('npm-api');
const wget   = require('node-wget');
const fs     = require('fs');
const uuid   = require('uuid');

async function getPackageList(){
  //const fname = uuid.v4();
  const fname = 'npm-all';
  const PACKAGE_LIST_PATH = `/tmp/npm-choice-${fname}.json`;
  const options = {
    'url'     : 'https://replicate.npmjs.com/_all_docs',
    'dest'    : PACKAGE_LIST_PATH,
    'timeout' : 86400000
  };

  console.debug(`temporary store path: ${PACKAGE_LIST_PATH}`);

  return new Promise((resolve, reject) => {
    wget(options, (err, res, body) => {
      if(err) reject(err);
      console.log(`store data at ${PACKAGE_LIST_PATH}`); 
      resolve(body);
    });
  });
}

async function main(){
  let list = await getPackageList().catch((err) => { console.error(err); });
  console.debug(`received list: ${list}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

