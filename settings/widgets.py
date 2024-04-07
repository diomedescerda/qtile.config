from libqtile import widget

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

arch_icon = widget.TextBox(
    text="",  
    fontsize=20,
    padding=14,
    background ="#0f101a"
)

