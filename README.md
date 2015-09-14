# pactray
Pactray is a small notifier for Arch Linux (pacman) updates.

![pactray-1](https://cloud.githubusercontent.com/assets/622615/9778069/f5e037dc-57ae-11e5-87b4-af41c62a75f3.png)

![pactray-2](https://cloud.githubusercontent.com/assets/622615/9778070/f6241ff6-57ae-11e5-886f-84bb84102e6e.png)

Pactray is a python process which runs in the background, checking system updates with `checkupdates` and `cower -u`

When updates are available an icon is shown in the system tray.

Left clicking the icon will show a notification of the available updates
Right clicking will execute update_cmd (if configured)

default configuration

````
update_interval=120 #minutes between executing checks for updates)
notification_timeout=10 #seconds to show notification popup for)
icon_file=archlogo.png #absolute path to file to use as the icon)
````

sample custom configuration

`~/.config/pactray.conf`
````
[global]
update_cmd=/usr/bin/mate-terminal --disable-factory -e "bash -c 'pacaur -Syu || read -p \"Press [Enter] to continue\"'"
````
