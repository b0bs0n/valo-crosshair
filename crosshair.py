from PIL import Image, ImageDraw, ImageOps, PngImagePlugin
import math


class Crosshair:
    COLORS = {'White': (255, 255, 255),
               'Green': (0, 255, 0),
               'Yellow Green': (154, 205, 50),
               'Green Yellow': (173, 255, 47),
               'Yellow': (255, 255, 0),
               'Cyan': (0, 255, 255),
               'Pink': (255, 0, 255),
               'Red': (255, 0, 0)}
    color = 'Green'
    outlines = [False, 1, 1]
    dot = [False, 1, 2]
    inner = [True, 1, 4, 2, 2]
    outer = [False, 1, 2, 2, 6]
    resolutions = [1920, 1080, 1920, 1080]

    def __init__(self):
        self.size = 50
        pass

    def set_color(self, color):
        if color in self.COLORS.keys():
            self.color = color

    def set_outlines(self, outlines):
        self.outlines[0] = outlines

    def set_outline_opacity(self, opacity):
        self.outlines[1] = opacity

    def set_outline_thickness(self, thickness):
        self.outlines[2] = thickness

    def set_dot(self, dot):
        self.dot[0] = dot

    def set_dot_opacity(self, opacity):
        self.dot[1] = opacity

    def set_dot_thickness(self, thickness):
        self.dot[2] = thickness

    def set_inner(self, inner):
        self.inner[0] = inner

    def set_inner_opacity(self, opacity):
        self.inner[1] = opacity

    def set_inner_length(self, length):
        self.inner[2] = length

    def set_inner_thickness(self, thickness):
        self.inner[3] = thickness

    def set_inner_offset(self, offset):
        self.inner[4] = offset

    def set_outer(self, outer):
        self.outer[0] = outer

    def set_outer_opacity(self, opacity):
        self.outer[1] = opacity

    def set_outer_length(self, length):
        self.outer[2] = length

    def set_outer_thickness(self, thickness):
        self.outer[3] = thickness

    def set_outer_offset(self, offset):
        self.outer[4] = offset

    def draw_crosshair(self):
        # Drawing inner Lines
        ct = 25
        ch_tmp = Image.new('RGBA', (50, 50))
        col_outline = (0, 0, 0, int(255 * self.outlines[1]))
        col_inner = self.COLORS[self.color] + (int(255 * self.inner[1]),)
        col_outer = self.COLORS[self.color] + (int(255 * self.outer[1]),)
        col_dot = self.COLORS[self.color] + (int(255 * self.dot[1]),)

        def draw_lines(line, color):
            ch_bg = ch_tmp.copy()
            if line[0] and line[2] and line[3]:
                ch_bg2 = ch_tmp.copy()
                draw = ImageDraw.Draw(ch_bg)
                draw2 = ImageDraw.Draw(ch_bg2)
                offset = line[3] % 2
                if self.outlines[0]:
                    draw.rectangle((ct - line[2] - line[4] - offset - self.outlines[2],
                                    ct - math.ceil((line[3]) / 2) - self.outlines[2],
                                    ct - line[4] - offset + self.outlines[2] - 1,
                                    ct + math.floor((line[3] / 2)) + self.outlines[2] - 1),
                                   fill=col_outline)

                    draw2.rectangle((ct + line[4] - self.outlines[2],
                                     ct + math.floor((line[3] / 2)) + self.outlines[2] - 1,
                                     ct + line[2] + line[4] + self.outlines[2] - 1,
                                     ct - math.ceil((line[3]) / 2) - self.outlines[2]),
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
            if self.dot[0]:
                ch_bg2 = ch_tmp.copy()
                draw = ImageDraw.Draw(ch_bg)
                draw2 = ImageDraw.Draw(ch_bg2)
                offset = self.dot[2] % 2
                width = self.dot[2] // 2
                if self.outlines[0]:
                    draw.rectangle((ct - width - self.outlines[2] - offset,
                                    ct - width - self.outlines[2] - offset,
                                    ct + width + self.outlines[2] - 1,
                                    ct + width + self.outlines[2] - 1),
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

        ch_x = draw_lines(self.inner, col_inner)
        ch_dot = draw_dot()
        ch_outer = draw_lines(self.outer, col_outer)

        ch_x = Image.alpha_composite(ch_x, ch_dot)
        ch_x = Image.alpha_composite(ch_x, ch_outer)
        # Apply screen stretch
        if self.resolutions[:2] != self.resolutions[2:]:
            game = Image.new('RGBA', (self.resolutions[2], self.resolutions[3]))
            coord = (int((self.resolutions[2] - 50) / 2), int((self.resolutions[3] - 50) / 2))
            game.paste(ch_x, coord)
            game = game.resize((self.resolutions[0], self.resolutions[1]), resample=Image.BILINEAR)
            ch_x = game.crop((int(self.resolutions[0] / 2 - 25),
                              int(self.resolutions[1] / 2 - 25),
                              int(self.resolutions[0] / 2 + 25),
                              int(self.resolutions[1] / 2 + 25)))
        return ch_x

    def gen_pnginfo(self):
        def convert(list_in):
            text = ';'.join(str(i) for i in list_in)
            return text

        info = PngImagePlugin.PngInfo()
        info.add_text('software', 'val_crosshair_tool')
        info.add_text('color', self.color)
        info.add_text('outlines', convert(self.outlines))
        info.add_text('dot', convert(self.dot))
        info.add_text('inner', convert(self.inner))
        info.add_text('outer', convert(self.outer))
        info.add_text('resolutions', convert(self.resolutions))
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
            self.color = info['color']
            self.outlines = convert(info['outlines'])
            self.dot = convert(info['dot'])
            self.inner = convert(info['inner'])
            self.outer = convert(info['outer'])
            self.resolutions = convert(info['resolutions'])
        pass


if __name__ == '__main__':
    ch = Crosshair()
    ch.draw_crosshair()
    chx = ch.draw_crosshair()
