#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-
#
# Copyright 2017 Torbjörn Rathsman
#
# Redistribution and use in source and binary forms, with or without modification, are permitted
# provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions
#    and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
#    and the following disclaimer in the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
# IMPLIED WARRANTIES, INCLUDING, BUTNOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import csv
import sys
import string
import os
import time
import operator

file_template=string.Template('''/*This file has been generated from $filename by
$srcfile on $date.
Any changes to this file may be overwritten during compilation.
*/

#ifndef MIDICONSTANTS_${FILENAME_NO_EXT}_HPP
#define MIDICONSTANTS_${FILENAME_NO_EXT}_HPP

#include <utility>

namespace MIDIConstants
	{
	enum class $FilenameNoExt:int
		{
		 $constants
		};

	constexpr std::pair<$FilenameNoExt,const char*> ${FILENAME_NO_EXT}_VALUE_NAME[]=
		{
		 {$value_name}
		};

	constexpr std::pair<const char*,$FilenameNoExt> ${FILENAME_NO_EXT}_NAME_VALUE[]=
		{
		 {$name_value}
		};
	}

#endif
''')

const_template=string.Template('''${IDENTIFIER}=$value    /**<$description*/''')
name_template=string.Template('''$FilenameNoExt::${IDENTIFIER},"$description"''')
name_inv_template=string.Template('''"$description",$FilenameNoExt::${IDENTIFIER}''')

module_dir = os.path.dirname(__file__)

def write_error(*args, **kwargs):
	print(*args,file=sys.stderr,**kwargs)

def getidx(list, idx, dflt=None):
	if len(list) > idx:
		return list[idx]
	return dflt

def compile(filename):
	cli_args = sys.argv[1:]
	if getidx(cli_args, 0) == '--': cli_args.pop(0)
	try:
		target_dir=getidx(cli_args, 0)
		if target_dir is None:
			raise RuntimeError('missing CLI arg: target_dir')
		in_dir=getidx(cli_args, 1, module_dir)

		IDENTIFIER=0
		VALUE=1
		DESCRIPTION=2
		substitutes=dict()

		(basefn, infile_fext) = os.path.splitext(os.path.basename(filename))
		fnwords = basefn.split('_')
		header_basefn = ''.join(fnwords) + '.hpp'
		substitutes['FILENAME_NO_EXT']=''.join([w.upper() for w in fnwords])
		substitutes['FilenameNoExt']=''.join([w.capitalize() for w in fnwords])
		substitutes['filename']=filename
		substitutes['date']=time.strftime('%Y-%m-%d %H:%M %Z')
		substitutes['srcfile']=sys.argv[0]
		with open(filename, encoding='utf-8') as src:
			reader=csv.reader(src,delimiter=';')
			table=list(reader)
			table_parsed=list()
			for row in table:
				table_parsed.append((row[IDENTIFIER],int(row[VALUE],0),row[DESCRIPTION]))

			constants=list()
			names=list()
			constant=dict()
			constant['FilenameNoExt']=substitutes['FilenameNoExt']
			for row in sorted(table_parsed,key=operator.itemgetter(VALUE)):
				constant['IDENTIFIER']=row[IDENTIFIER]
				constant['value']=row[VALUE]
				constant['description']=row[DESCRIPTION]
				constants.append(const_template.substitute(constant))
				names.append(name_template.substitute(constant))
			substitutes['constants']='\n\t\t\t,'.join(constants)
			substitutes['value_name']='}\n\t\t\t,{'.join(names)

			names.clear()
			for row in sorted(table_parsed,key=operator.itemgetter(DESCRIPTION)):
				constant['IDENTIFIER']=row[IDENTIFIER]
				constant['description']=row[DESCRIPTION]
				names.append(name_inv_template.substitute(constant))
			substitutes['name_value']='}\n\t\t\t,{'.join(names)

		with open(os.path.join(target_dir, header_basefn), 'wb') as output:
			output.write(file_template.substitute(substitutes).encode('utf-8'))
		sys.exit(0)
	except Exception:
		write_error('%s:%d: error: %s\n'%(sys.argv[0],sys.exc_info()[2].tb_lineno,sys.exc_info()[1]))
		sys.exit(-1)
