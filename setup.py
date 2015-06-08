'''
The MIT License (MIT)

Copyright (c) 2015 Sascha Spreitzer, Red Hat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


from setuptools import setup


setup(
    name = "mkhomedirs-ipa-ad",
    version = "0.1",
    author = "Sascha Spreitzer",
    author_email = "sspreitz@redhat.com",
    description = ("Helper script to create home directories from FreeIPA trusted to Active Directory"),
    license = "MIT",
    keywords = "ipa freeipa ad auto.home mkhomedir",
    url = "https://github.com/sspreitzer/mkhomedirs-ipa-ad",
    package_dir = {'': 'src'},
    install_requires=['sid', 'python-ldap'],
    scripts = ['src/mkhomedirs-ipa-ad'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Systems Administration",
    ],
)
