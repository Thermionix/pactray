#!/usr/bin/env python

import os
import sys
from gi.repository import Gtk, GLib
from pactray.updates import UpdateChecker
from pactray.tray import TrayIcon
from pactray.conf import Configuration

def main(args=None):
	import signal
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	trayIcon = TrayIcon()
	checker = UpdateChecker()

	update_interval = int(Configuration().read().get('global', 'update_interval')) * 60

	def check():
		checker.run_check(trayIcon)
		return True

	check()
	GLib.timeout_add_seconds(update_interval, check)

	Gtk.main()

if __name__ == '__main__':
	main()
