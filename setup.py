#!/usr/bin/env python

from distutils.core import setup

setup(name='pactray',
      version='0.1',
      license='GPL3',
      description='a systray application that notifies that user about new updates for Arch Linux',
      author=['Thermionix'],
      author_email=['thermionix@gmail.com'],
      url='https://github.com/Thermionix/pactray',
      package_dir={'pactray':'src/lib/'},
      packages=['pactray'],
      data_files=[('share/pactray/', ['src/share/archlogo.png', 'src/share/archlogo.svg']),
                  ('share/applications', ['src/pactray.desktop'])]
)

