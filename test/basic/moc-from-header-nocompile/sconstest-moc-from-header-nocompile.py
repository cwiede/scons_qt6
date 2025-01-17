#!/usr/bin/env python
#
# Copyright (c) 2001-2010 The SCons Foundation
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
Create a moc file from a header file, but don't
compile it to an Object because the moc'ed output gets directly
included to the CXX file.
"""

import TestSCons

test = TestSCons.TestSCons()
test.dir_fixture('image')
test.file_fixture('../../qtenv.py')
test.file_fixture('../../../__init__.py','site_scons/site_tools/qt6/__init__.py')

aaa_exe = 'aaa' + TestSCons._exe
build_aaa_exe = test.workpath('build', aaa_exe)
moc = 'moc_aaa.cc'
moc_obj = 'moc_aaa' + TestSCons._obj

test.run()

# Ensure that the object file for the MOC output wasn't generated
test.must_not_exist(moc_obj)

test.up_to_date(options = '-n', arguments=aaa_exe)
test.up_to_date(options = '-n', arguments=aaa_exe)

test.write('aaa.h', r"""
#include <QObject>

// Introducing a change...
class aaa : public QObject
{
  Q_OBJECT

public:
  aaa() {};
};
""")

test.not_up_to_date(options='-n', arguments = moc)

test.run(arguments = "variant_dir=1 " + build_aaa_exe)

test.run(arguments = "variant_dir=1 chdir=1 " + build_aaa_exe)

test.must_exist(test.workpath('build', moc))
test.must_not_exist(test.workpath('build', moc_obj))

test.run(options='-c')

test.run(arguments = "variant_dir=1 chdir=1 dup=0 " +
                     test.workpath('build_dup0', aaa_exe) )

test.must_exist(test.workpath('build_dup0', moc))
test.must_not_exist(moc_obj)
test.must_not_exist(test.workpath('build_dup0', moc_obj))

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
