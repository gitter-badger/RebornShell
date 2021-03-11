class Color:
    def __init__(self, color=34, bold=21, underline=24, blink=25, framed=54,
                 overlined=55):
        self.col, self.bold, self.uline = color, bold, underline
        self.blk, self.frame, self.oline = blink, framed, overlined

    def getCode(self):
        return f"\033[{self.col};{self.bold};{self.uline};{self.blk};{self.frame};{self.oline}m"


# preset colors
foreground_presets = {
    "black": Color(color=30),
    "red": Color(color=31),
    "green": Color(color=32),
    "yellow": Color(color=33),
    "blue": Color(color=34),
    "magenta": Color(color=35),
    "cyan": Color(color=36),
    "white": Color(color=37)
}

background_presets = {
    "black": Color(color=40),
    "red": Color(color=41),
    "green": Color(color=42),
    "yellow": Color(color=43),
    "blue": Color(color=44),
    "magenta": Color(color=45),
    "cyan": Color(color=46),
    "white": Color(color=47)
}


# reset everything
reset = "\033[0m"
