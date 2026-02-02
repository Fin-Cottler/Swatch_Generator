from PIL import Image
from PIL import ImageDraw
import colorsys
import math
import os


class Colorswatch:

    colors_list = []

    @classmethod
    def hex_to_hsv(cls, hex_code: str):
        r_hex = int(hex_code[0:2], 16)
        g_hex = int(hex_code[2:4], 16)
        b_hex = int(hex_code[4:6], 16)

        r_norm = r_hex / 255.0
        g_norm = g_hex / 255.0
        b_norm = b_hex / 255.0

        h_norm, s_norm, v_norm = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)

        hue = h_norm * 360
        saturation = s_norm * 100
        value = v_norm * 100
        
        return (hue, saturation, value)
    
    @classmethod
    def hsv_to_rgb(cls, hsv):
        hue = hsv[0]
        saturation = hsv[1]
        value = hsv[2]

        hue /= 360
        saturation /= 100
        value /= 100

        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

        r = int(round(r * 255))
        g = int(round(g * 255))
        b = int(round(b * 255))

        return (r,g,b)
    
    @classmethod
    def populate_colors_list(cls, hex_code: str, other_hex_code: str, colors_count: int):
        hsv = Colorswatch.hex_to_hsv(hex_code)
        other_hsv = Colorswatch.hex_to_hsv(other_hex_code)

        hue = hsv[0]
        other_hue = other_hsv[0]

        hue_step = (abs(other_hue - hue)) / colors_count

        if hue < other_hue:
            rgb = Colorswatch.hsv_to_rgb((hue,100,100))

            for color in range(colors_count):
                Colorswatch.colors_list.append(rgb)
                hue += hue_step
                rgb = Colorswatch.hsv_to_rgb((hue,100,100))
                
        else:
            rgb = Colorswatch.hsv_to_rgb((other_hue,100,100))

            for color in range(colors_count):
                Colorswatch.colors_list.append(rgb)
                other_hue += hue_step
                rgb = Colorswatch.hsv_to_rgb((other_hue,100,100))

    @classmethod
    def generate_colored_square(cls, color, directory: str, swatch_id):
        filename = f"swatch_{swatch_id}.png"
        filepath = os.path.join(directory, filename)

        img = Image.new('RGB', (25, 25), color=color)
        img.save(filepath)

    @classmethod
    def populate_swatches(cls, hex_code: str, other_hex_code: str, colors_count: int, directory: str):
        Colorswatch.populate_colors_list(hex_code, other_hex_code, colors_count)

        for swatch_id in range(len(Colorswatch.colors_list)):
            Colorswatch.generate_colored_square(Colorswatch.colors_list[swatch_id], directory, swatch_id + 1)

            




            
        

