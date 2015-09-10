#!/usr/bin/env python

from gi.repository import Gtk, Notify
from conf import Configuration

class Notifications():
	def __init__(self):
		Notify.init("pactray")

	def Show(self, updatesList):
		updateCount = len(updatesList)
		title = str(updateCount) + " Updates Available"
		body = "\n".join(updatesList)
		new_notification = Notify.Notification.new(title, body, Configuration().read().get('global', 'icon_file'))
		new_notification.set_timeout(int(Configuration().read().get('global', 'notification_timeout')) * 1000)
		new_notification.show()

class TrayIcon():
	updatesList=[]

	def __init__(self):
		self.status_icon = Gtk.StatusIcon()
		self.status_icon.set_from_file(Configuration().read().get('global', 'icon_file'))
		self.status_icon.connect('popup-menu', self.on_right_click)
		self.status_icon.connect('activate', self.on_left_click)
		self.status_icon.set_visible(False)

	def on_right_click(self, icon, button, time):
		update_cmd=Configuration().read().get('global', 'update_cmd')
		if update_cmd:
			print("executing " + update_cmd)
			# subprocess launch update_cmd
			self.status_icon.set_visible(False)
			# pause check_updates till subprocess exits?
			# run check_updates once subprocess exits?

	def on_left_click(self, event):
		notification = Notifications()
		notification.Show(self.updatesList)

	def update_status_icon(self, updatesList):
		self.updatesList=updatesList
		if len(updatesList) > 0: 
			self.status_icon.set_visible(True)
			updateCount = len(self.updatesList)
			self.status_icon.set_tooltip_text(str(updateCount) + " Updates Available")
		else:
			self.status_icon.set_visible(False)

