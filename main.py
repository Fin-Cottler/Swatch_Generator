from colorSwatch import *
'''
populate_swatches generates png files (25px x 25px) of maximum saturation and value colors between two hex code colors
populate_swatches takes 4 parameters:

    hex_code (str): this is one of the two color end points. It must be a hexcode without its prefix '#'
    
    other_hex_code (str): this is the second of the two color end points. It must be a hexcode without its prefix '#'
    
    colors_count (int): this is the number of swatches that should be generated
    
    directory (str NOTE: must be raw string on windows by prefixing string with 'r'): this is the full path to folder where swatches will be placed
        IMPORTANT NOTE: DIRECTORY MUST ALREADY EXIST (and preferably empty) !!!
'''

'''
Reasoning for maximum saturation and value:

    No matter the saturation of the two input colors, the saturation and value will be increased to their maximum, only preserving their hue data.
    This isolates hue as a single parameter for evaluation
'''

Colorswatch.populate_swatches(
    "3270a6",
    "455e4c",
    20,
    r"C:\Users\gelat\Downloads\Swatch_Generator-main\Swatch_Generator-main\swatches"
)


