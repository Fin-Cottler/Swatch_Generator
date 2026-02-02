from colorSwatch import *

'''
The populate swatches methods take 4 parameters:
    hex_code (str): This is the hex code of the initial color that varients will be generated from.
                    This must be 6 characters only and exclude the '#' prefix of the hex code
                    THIS MUST BE A 100% Saturation and 100% value color.

    variance (int): This is a integer 0-100 representing how random the color selection.
                    For hueflex, hue has a range of +/- 20*(variation/100). 
                    20 degrees maximum varience in hue ensures that all colors appear similar.

    directory (str (raw string on windows)): This is the full path to the folder color swatches should be put into. 
                                            IT MUST EXIST BEFORE RUNNING CODE! PROGRAM DOES NOT CREATE A FOLDER IF ONE DOES NOT EXIST!

    swatch_count (int): Number of swatches that should be created           
'''
Colorswatch.populate_swatches(
    "001aff",
    50,
    r"C:\Users\gelat\OneDrive\Desktop\Work\Color_Swatch_Generator\swatches",
    100
)

# Colorswatch.populate_swatches_hueflex(
#     "006eff",
#     100,
#     r"C:\Users\gelat\OneDrive\Desktop\Work\Color_Swatch_Generator\swatches",
#     100
# )
