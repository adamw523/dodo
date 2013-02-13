#######################################################################
# Copyright (c) 2013 Adam Wisniewski, http://adamw523.com
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from setuptools import setup
import dodo

version = dodo.VERSION

setup(  name='dodo',
        version=version,
        description='DigitalOcean Library and Command Line tools',
        author='Adam Wisniewski',
        author_email='adamw@tbcn.ca',
        license='MIT',
        install_requires=['requests >= 1.1.0'],
        packages=['dodo'],
        include_package_data=True,
        scripts=['bin/dodo'],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Information Technology",
            "License :: OSI Approved :: MIT License",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Utilities"
        ]
    )

