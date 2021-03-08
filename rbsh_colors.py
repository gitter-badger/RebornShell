class Color:
    # the main color
    # many... many values
    color = 34
    # 1 = on / 21 = off
    bold = 21
    # 4 = on / 24 = off
    underline = 24
    # 5 = slow blink, 6 = fast blink / 25 = blink off
    blink = 25
    # 51 = framed, 52 = encircled / 54 = not framed or
    # encircled
    framed = 54
    # 53 = on / 55 = off
    overlined = 55

    def __init__(self, color=34, bold=21, underline=24, blink=25, framed=54, overlined=55):
        self.color, self.bold, self.underline, self.blink, self.framed, self.overlined = color, bold, underline, blink, framed, overlined

    def getCode(self):
        return f"\033[{self.color};{self.bold};{self.underline};{self.blink};{self.framed}m"


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
reset = Color()
reset.color = 0
reset.bold = 21
reset.underline = 24
reset.blink = 25
reset.framed = 55
