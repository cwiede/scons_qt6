#!/usr/bin/env python
#
# Copyright (c) 2001-2010,2011,2012 The SCons Foundation
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


"""
Test the QT5_CLEAN_TS option, which removes .ts files
on a 'scons -c'.
"""

import TestSCons

test = TestSCons.TestSCons()
test.dir_fixture("image")
test.file_fixture('../../qtenv.py')
test.file_fixture('../../../__init__.py','site_scons/site_tools/qt6/__init__.py')
test.run(stderr=None)

test.must_exist(test.workpath('my_en.ts'))
test.must_contain(test.workpath('my_en.ts'),'SCons rocks!')
test.must_exist(test.workpath('my_en.qm'))

test.run(options = '-c')

test.must_not_exist(test.workpath('my_en.ts'))
test.must_not_exist(test.workpath('my_en.qm'))

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
