#!/usr/bin/env python

import os
from gi.repository import Gtk, GLib
from updates import UpdateChecker
from tray import TrayIcon
from conf import Configuration

if __name__ == '__main__':
	import signal
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	trayIcon = TrayIcon()
	checker = UpdateChecker()

	#update_interval = int(Configuration().read().get('global', 'update_interval')) * 60
	update_interval = 5 * 60

	def check():
		checker.run_check(trayIcon)
		return True

	check()
	GLib.timeout_add_seconds(update_interval, check)

	Gtk.main()
