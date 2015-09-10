#!/usr/bin/env python

from configparser import SafeConfigParser
from os import environ, path

class Configuration:

	conf_dir = environ['HOME'] + '/.config/'
	conf_file = conf_dir + 'pactray.conf'

	conf_options = {'global' : {
					'update_interval': '360',
					'notification_timeout': '10',
					'icon_file': (path.join(path.abspath(path.curdir),"archlogo.png")),
					'update_cmd': '/usr/bin/xterm -e "sudo pacman -Syu"'
					}}
					# pacman_check_cmd ["/usr/bin/checkupdates"]
					# aur_check_cmd ["/usr/bin/cower","-u"]

	def read(self):
		parser = SafeConfigParser()
		parser.read_dict(self.conf_options)
		parser.read(self.conf_file)
		return parser

