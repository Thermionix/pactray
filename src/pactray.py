#!/usr/bin/env python

import os
from gi.repository import Gtk
from updates import UpdateChecker
from tray import TrayIcon, Notifications
from concurrent import futures
from conf import Configuration

if __name__ == '__main__':
	import signal
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	trayIcon = TrayIcon()

	checker = UpdateChecker()
	checker.run_check(trayIcon)

	Gtk.main()
