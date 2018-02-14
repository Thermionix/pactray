#!/usr/bin/env python

import subprocess
import os
from pactray.conf import Configuration

class UpdateChecker:
	updatesList=[]

	def check_pacman(self):
		pacman_output = subprocess.check_output(["/usr/bin/checkupdates"])
		self.append_to_list(pacman_output)

	def check_auracle(self):
		try:
			ps = subprocess.Popen(["/usr/bin/auracle","sync"], stdout=subprocess.PIPE)
			auracle_output = ps.communicate()[0]
			self.append_to_list(auracle_output)
		except OSError as e:
			if not e.errno == os.errno.ENOENT:
				raise

	def append_to_list(self, command_output):
		output_lines=(command_output).decode().splitlines()
		if len(output_lines) > 0:
			self.updatesList.extend(output_lines)

	def run_check(self, trayIcon):
		self.updatesList=[]
		self.check_pacman()
		self.check_auracle()
		print("pactray updates count: " + str(len(self.updatesList)))
		trayIcon.update_status(self.updatesList)

