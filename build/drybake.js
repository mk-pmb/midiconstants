/*jslint indent: 2, maxlen: 80, continue: false, unparam: false, node: true */
/* -*- tab-width: 2 -*- */
'use strict';
var fs = require('fs'), dry = require('dry-id-table-pmb');
fs.readFile(process.argv[2], 'UTF-8', function (err, tbl) {
  if (err) { throw err; }
  tbl = dry(tbl);
  function tabulate(row) { return row.join(';'); }
  console.log(tbl.map(tabulate).join('\n'));
});
