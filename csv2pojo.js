/*jslint indent: 2, maxlen: 80, node: true */
/* -*- tab-width: 2 -*- */
'use strict';
module.exports = require('export-module-csv-files-sync-pmb')({
  module: module,
  pkgName: 'midiconst',
  jsonExportPrefix: 'dist/nonfree/',
  csvOpt: { delimiter: ';' },
});
