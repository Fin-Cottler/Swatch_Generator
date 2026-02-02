from PIL import Image
from PIL import ImageDraw
import colorsys
import random
import os
import shutil

class Colorswatch:

    def clear_folder(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            os.unlink(file_path)


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
        
        return hue, saturation, value
    
    @classmethod
    def hsv_to_rgb(cls, hue, saturation, value):
        hue /= 360
        saturation /= 100
        value /= 100

        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

        r = int(round(r * 255))
        g = int(round(g * 255))
        b = int(round(b * 255))

        return (r,g,b)

    @classmethod
    def generate_color(cls, hex_code: str, variance_percentage: int):
        hue, saturation, value = Colorswatch.hex_to_hsv(hex_code)

        if variance_percentage > 0:
            variance_percentage -= 1
        
        saturation -= random.randint(0, variance_percentage)
        value -= random.randint(0, variance_percentage)

        color = Colorswatch.hsv_to_rgb(hue,saturation,value)
        return (color)

    @classmethod
    def generate_color_with_hueflex(cls, hex_code: str, variance_percentage: int):
        hue, saturation, value = Colorswatch.hex_to_hsv(hex_code)
    
        if variance_percentage > 0:
            variance_percentage -= 1

        max_hueflex = int(360 * (variance_percentage/100))

        hue_shift = random.randint(0, max_hueflex)
        rand = random.randint(1, 2)
        if rand == 1:
            hue += hue_shift
        else:
            hue -= hue_shift
        
        saturation -= random.randint(0, variance_percentage)
        value -= random.randint(0, variance_percentage)

        color = Colorswatch.hsv_to_rgb(hue,saturation,value)
        return (color)
    

    def generate_colored_square(color, directory: str, swatch_id: int):
        filename = f"swatch_{swatch_id}.png"
        filepath = os.path.join(directory, filename)

        img = Image.new('RGB', (25, 25), color=color)
        img.save(filepath)

    def populate_swatches(hex_code: str, variance: int, directory: str, swatch_count: int):
        for swatch_id in range(swatch_count):
            color = Colorswatch.generate_color(hex_code, variance)
            print(color)
            Colorswatch.generate_colored_square(color, directory, swatch_id)

    def populate_swatches_hueflex(hex_code: str, variance: int, directory: str, swatch_count: int):        
        for swatch_id in range(swatch_count):
            color = Colorswatch.generate_color_with_hueflex(hex_code, variance)
            Colorswatch.generate_colored_square(color, directory, swatch_id)
            




            
        