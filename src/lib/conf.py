#!/usr/bin/env python

from configparser import SafeConfigParser
from os import environ, path

class Configuration:

	conf_dir = environ['HOME'] + '/.config/'
	conf_file = conf_dir + 'pactray.conf'

	conf_options = {'global' : {
					'update_interval': '120',
					'notification_timeout': '10',
					'icon_file': '/usr/share/pactray/archlogo.png'
					}}
					# (path.join(path.abspath(path.curdir),''))
					# pacman_check_cmd ["/usr/bin/checkupdates"]
					# aur_check_cmd ["/usr/bin/cower","-u"]
					# aur_output_regex

	def read(self):
		parser = SafeConfigParser()
		parser.read_dict(self.conf_options)
		parser.read(self.conf_file)
		return parser

