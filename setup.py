
from __future__ import absolute_import
import subprocess

from setuptools import setup

#try:
#    pandoc = subprocess.Popen(['pandoc', 'README.md', '--to', 'rst'],
#                              stdout=subprocess.PIPE)

#    readme = pandoc.communicate()[0].decode()

#except OSError:
with open('README.md') as f:
    readme = f.read()

setup(
    name="mu-notedown",
    version="2.0.0",
    description="A fork of notedown",
    long_description=readme,
    packages=['notedown'],
    author="Mu Li",
    author_email='muli.cmu@gmail.com',
    license='BSD 2-Clause',
    url='http://github.com/mli/notedown',
    install_requires=['nbformat<=4.4',
                      'nbconvert',
                      'pandoc-attributes',
                      'six'],
    entry_points={'console_scripts': ['notedown = notedown.main:app', ]},
    package_dir={'notedown': 'notedown'},
    package_data={'notedown': ['templates/markdown.tpl',
                               'templates/markdown_outputs.tpl']},
    include_package_data=True,
)
