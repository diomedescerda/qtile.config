from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    
    # Switch between windows
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),

    # Move windows between windows.
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
   
    # Change window sizes
    ([mod, "control"], "h", lazy.layout.grow()),
    ([mod, "control"], "l", lazy.layout.shrink()),

    # Toggle between different screens
    ([mod], 'period', lazy.next_screen()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod], "w", lazy.window.kill()),
    (
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
    ),
    ([mod, "control"], "r", lazy.reload_config()),
    ([mod, "control"], "q", lazy.shutdown()),

    ([mod], "Return", lazy.spawn("alacritty")),

    # My programs

    # Menu
    ([mod], "m", lazy.spawn("rofi -show run")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("google-chrome-stable")),

    # VS Code
    ([mod], "c", lazy.spawn("code")),
    
    # Take Screenshots
    ([mod], "s", lazy.spawn("scrot --focused --border -q 100")),
    ([mod, "control"], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
