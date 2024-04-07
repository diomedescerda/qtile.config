from libqtile import bar, widget 
from libqtile.config import Screen
from libqtile.lazy import lazy
from os import path
import subprocess
from .widgets import widget_defaults, extension_defaults, arch_icon

screens = [
    Screen(
        top=bar.Bar(
            [
                arch_icon,
                widget.GroupBox(
                    foreground =['#f1ffff','#f1ffff'],
                    background=['#0f101a', '#0f101a'],
                    font='UbuntuMono Nerd Font',
                    fontsize=17,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=['#f1ffff','#f1ffff'],
                    inactive=['#f1ffff','#f1ffff'],
                    rounded=False,
                    highlight_method='block',
                    this_current_screen_border=['#A77AC4', '#A77AC4'],
                    this_screen_border=['#5c5c5c', '#5c5c5c'],
                    other_current_screen_border=['#0f101a', '#0f101a'],
                    other_screen_border=['#0f101a', '#0f101a']
                ),
                widget.WindowName(
                    foreground =['#A77AC4', '#A77AC4'],
                    background=['#0f101a', '#0f101a'],
                    fontsize=15,
                    font='UbuntuMono Nerd Font Bold',
                    padding=5,
                ),
                widget.Systray(),
                widget.Image(
                    filename = path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'bar1.png')
                ),
                widget.TextBox("Kenma Kozume", name="default", 
                foreground = ['#1e2127','#1e2127'],
                background =['#A77AC4', '#A77AC4'],
                padding = 10,
                font='UbuntuMono Nerd Font Bold',
                ),
                widget.Image(
                    filename = path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'bar2.png')
                ),
                widget.CurrentLayout(
                    foreground = ['#1e2127','#1e2127'],
                    background=['#9b9da0', '#9b9da0'],
                    padding = 15,
                    font='UbuntuMono Nerd Font Bold',
                ),
                widget.Image(
                    filename = path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'bar3.png')
                ),
                widget.Clock(format="%A %H:%M %Y-%m-%d",
                foreground = ['#1e2127','#1e2127'],
                background=['#7197E7', '#7197E7'],
                font='UbuntuMono Nerd Font Bold',
                padding = 10,
                ),
            ],
            24,
            opacity = 0.95
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                arch_icon,
                widget.GroupBox(
                    foreground =['#f1ffff','#f1ffff'],
                    background=['#0f101a', '#0f101a'],
                    font='UbuntuMono Nerd Font',
                    fontsize=17,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=['#f1ffff','#f1ffff'],
                    inactive=['#f1ffff','#f1ffff'],
                    rounded=False,
                    highlight_method='block',
                    this_current_screen_border=['#A77AC4', '#A77AC4'],
                    this_screen_border=['#5c5c5c', '#5c5c5c'],
                    other_current_screen_border=['#0f101a', '#0f101a'],
                    other_screen_border=['#0f101a', '#0f101a']
                ),
                widget.WindowName(
                    foreground =['#A77AC4', '#A77AC4'],
                    background=['#0f101a', '#0f101a'],
                    fontsize=15,
                    font='UbuntuMono Nerd Font Bold',
                    padding=5,
                ),
                widget.Image(
                    filename = path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'bar1.png')
                ),
                widget.TextBox("Kenma Kozume", name="default", 
                foreground = ['#1e2127','#1e2127'],
                background =['#A77AC4', '#A77AC4'],
                padding = 10,
                font='UbuntuMono Nerd Font Bold',
                ),
                widget.Image(
                    filename = path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'bar2.png')
                ),
                widget.CurrentLayout(
                    foreground = ['#1e2127','#1e2127'],
                    background=['#9b9da0', '#9b9da0'],
                    padding = 15,
                    font='UbuntuMono Nerd Font Bold',
                ),
                widget.Image(
                    filename = path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'bar3.png')
                ),
                widget.Clock(format="%A %H:%M %Y-%m-%d",
                foreground = ['#1e2127','#1e2127'],
                background=['#7197E7', '#7197E7'],
                font='UbuntuMono Nerd Font Bold',
                padding = 10,
                ),
            ],
            24,
            opacity = 0.95
        ),
    ),
]

