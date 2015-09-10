# pactray
Pactray is a small notifier for Arch Linux (pacman) updates.

![pactray-1](https://cloud.githubusercontent.com/assets/622615/9778069/f5e037dc-57ae-11e5-87b4-af41c62a75f3.png)

![pactray-2](https://cloud.githubusercontent.com/assets/622615/9778070/f6241ff6-57ae-11e5-886f-84bb84102e6e.png)

sample configuration

`~/.config/pactray.conf`
````
[global]
update_cmd=/usr/bin/mate-terminal --disable-factory -e "pacaur -Syu"
````
