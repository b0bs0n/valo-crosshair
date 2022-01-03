from PIL import Image, ImageDraw, ImageOps, PngImagePlugin
import math


class Crosshair:
    _COLORS = {'White': (255, 255, 255),
               'Green': (0, 255, 0),
               'Yellow Green': (154, 205, 50),
               'Green Yellow': (173, 255, 47),
               'Yellow': (255, 255, 0),
               'Cyan': (0, 255, 255),
               'Pink': (255, 0, 255),
               'Red': (255, 0, 0)}
    _color = 'Green'
    _outlines = [False, 1, 1]
    _dot = [False, 1, 2]
    _inner = [True, 1, 4, 2, 2]
    _outer = [False, 1, 2, 2, 6]
    _resolutions = [1920, 1080, 1920, 1080]

    def __init__(self):
        self.size = 50
        pass

    def set_color(self, color):
        if color in self._COLORS.keys():
            self._color = color

    def set_outlines(self, outlines):
        self._outlines[0] = outlines

    def set_outline_opacity(self, opacity):
        self._outlines[1] = opacity

    def set_outline_thickness(self, thickness):
        self._outlines[2] = thickness

    def set_dot(self, dot):
        self._dot[0] = dot

    def set_dot_opacity(self, opacity):
        self._dot[1] = opacity

    def set_dot_thickness(self, thickness):
        self._dot[2] = thickness

    def set_inner(self, inner):
        self._inner[0] = inner

    def set_inner_opacity(self, opacity):
        self._inner[1] = opacity

    def set_inner_length(self, length):
        self._inner[2] = length

    def set_inner_thickness(self, thickness):
        self._inner[3] = thickness

    def set_inner_offset(self, offset):
        self._inner[4] = offset

    def set_outer(self, outer):
        self._outer[0] = outer

    def set_outer_opacity(self, opacity):
        self._outer[1] = opacity

    def set_outer_length(self, length):
        self._outer[2] = length

    def set_outer_thickness(self, thickness):
        self._outer[3] = thickness

    def set_outer_offset(self, offset):
        self._outer[4] = offset

    def draw_crosshair(self):
        # Drawing inner Lines
        ct = 25
        ch_tmp = Image.new('RGBA', (50, 50))
        col_outline = (0, 0, 0, int(255 * self._outlines[1]))
        col_inner = self._COLORS[self._color] + (int(255 * self._inner[1]),)
        col_outer = self._COLORS[self._color] + (int(255 * self._outer[1]),)
        col_dot = self._COLORS[self._color] + (int(255 * self._dot[1]),)

        def draw_lines(line, color):
            ch_bg = ch_tmp.copy()
            if line[0] and line[2] and line[3]:
                ch_bg2 = ch_tmp.copy()
                draw = ImageDraw.Draw(ch_bg)
                draw2 = ImageDraw.Draw(ch_bg2)
                offset = line[3] % 2
                if self._outlines[0]:
                    draw.rectangle((ct - line[2] - line[4] - offset - self._outlines[2],
                                    ct - math.ceil((line[3]) / 2) - self._outlines[2],
                                    ct - line[4] - offset + self._outlines[2] - 1,
                                    ct + math.floor((line[3] / 2)) + self._outlines[2] - 1),
                                   fill=col_outline)

                    draw2.rectangle((ct + line[4] - self._outlines[2],
                                     ct + math.floor((line[3] / 2)) + self._outlines[2] - 1,
                                     ct + line[2] + line[4] + self._outlines[2] - 1,
                                     ct - math.ceil((line[3]) / 2) - self._outlines[2]),
                                    fill=col_outline)

                    draw.rectangle((ct - line[2] - line[4] - offset,
                                    ct - math.ceil(line[3] / 2),
                                    ct - line[4] - 1 - offset,
                                    ct + math.floor(line[3] / 2) - 1),
                                   fill=(0, 0, 0, 0))

                    draw2.rectangle((ct + line[4],
                                     ct - math.ceil(line[3] / 2),
                                     ct + line[2] + line[4] - 1,
                                     ct + math.floor(line[3] / 2) - 1),
                                    fill=(0, 0, 0, 0))

                draw.rectangle((ct - line[2] - line[4] - offset,
                                ct - math.ceil(line[3] / 2),
                                ct - line[4] - 1 - offset,
                                ct + math.floor(line[3] / 2) - 1),
                               fill=color)

                draw2.rectangle((ct + line[4],
                                 ct - math.ceil(line[3] / 2),
                                 ct + line[2] + line[4] - 1,
                                 ct + math.floor(line[3] / 2) - 1),
                                fill=color)
                ch_bg = Image.alpha_composite(ch_bg, ch_bg2)
                ch_bg2 = ch_bg.rotate(-90)
                ch_bg2 = ImageOps.mirror(ch_bg2)
                ch_bg = Image.alpha_composite(ch_bg, ch_bg2)
            return ch_bg

        def draw_dot():
            ch_bg = ch_tmp.copy()
            if self._dot[0]:
                ch_bg2 = ch_tmp.copy()
                draw = ImageDraw.Draw(ch_bg)
                draw2 = ImageDraw.Draw(ch_bg2)
                offset = self._dot[2] % 2
                width = self._dot[2] // 2
                if self._outlines[0]:
                    draw.rectangle((ct - width - self._outlines[2] - offset,
                                    ct - width - self._outlines[2] - offset,
                                    ct + width + self._outlines[2] - 1,
                                    ct + width + self._outlines[2] - 1),
                                   fill=col_outline)
                    draw.rectangle((ct - width - offset,
                                    ct - width - offset,
                                    ct + width - 1,
                                    ct + width - 1),
                                   fill=(0, 0, 0, 0))

                draw2.rectangle((ct - width - offset,
                                 ct - width - offset,
                                 ct + width - 1,
                                 ct + width - 1),
                                fill=col_dot)
                ch_bg = Image.alpha_composite(ch_bg, ch_bg2)
            return ch_bg

        ch_x = draw_lines(self._inner, col_inner)
        ch_dot = draw_dot()
        ch_outer = draw_lines(self._outer, col_outer)

        ch_x = Image.alpha_composite(ch_x, ch_dot)
        ch_x = Image.alpha_composite(ch_x, ch_outer)
        # Apply screen stretch
        if self._resolutions[:2] != self._resolutions[2:]:
            game = Image.new('RGBA', (self._resolutions[2], self._resolutions[3]))
            coord = (int((self._resolutions[2] - 50) / 2), int((self._resolutions[3] - 50) / 2))
            game.paste(ch_x, coord)
            game = game.resize((self._resolutions[0], self._resolutions[1]), resample=Image.BILINEAR)
            ch_x = game.crop((int(self._resolutions[0] / 2 - 25),
                              int(self._resolutions[1] / 2 - 25),
                              int(self._resolutions[0] / 2 + 25),
                              int(self._resolutions[1] / 2 + 25)))
        return ch_x

    def gen_pnginfo(self):
        def convert(list_in):
            text = ';'.join(str(i) for i in list_in)
            return text

        info = PngImagePlugin.PngInfo()
        info.add_text('software', 'val_crosshair_tool')
        info.add_text('color', self._color)
        info.add_text('outlines', convert(self._outlines))
        info.add_text('dot', convert(self._dot))
        info.add_text('inner', convert(self._inner))
        info.add_text('outer', convert(self._outer))
        info.add_text('resolutions', convert(self._resolutions))
        return info

    def save_png(self, path):
        info = self.gen_pnginfo()
        drawn = self.draw_crosshair()
        drawn.save(path, format='png', pnginfo=info)

    def load_png(self, path):
        def convert(inp):
            out = []
            inp = inp.split(';')
            for i in inp:
                if 'True' in i:
                    out.append(True)
                elif 'False' in i:
                    out.append(False)
                else:
                    val = float(i)
                    if val % 1 == 0:
                        val = int(val)
                    out.append(val)
            return out

        with Image.open(path) as png:
            info = png.info
            self._color = info['color']
            self._outlines = convert(info['outlines'])
            self._dot = convert(info['dot'])
            self._inner = convert(info['inner'])
            self._outer = convert(info['outer'])
            self._resolutions = convert(info['resolutions'])
        pass


if __name__ == '__main__':
    ch = Crosshair()
    ch.draw_crosshair()
    chx = ch.draw_crosshair()
