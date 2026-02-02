
     ______     .-./`)   .-_'''-.  .-./`) ,---------.    ____      .---.                 _______      ,-----.      .---.       ,-----.    .-------.     
    |    _ `''. \ .-.') '_( )_   \ \ .-.')\          \ .'  __ `.   | ,_|                /   __  \   .'  .-,  '.    | ,_|     .'  .-,  '.  |  _ _   \    
    | _ | ) _  \/ `-' \|(_ o _)|  '/ `-' \ `--.  ,---'/   '  \  \,-./  )               | ,_/  \__) / ,-.|  \ _ \ ,-./  )    / ,-.|  \ _ \ | ( ' )  |    
    |( ''_'  ) | `-'`"`. (_,_)/___| `-'`"`    |   \   |___|  /  |\  '_ '`)           ,-./  )      ;  \  '_ /  | :\  '_ '`) ;  \  '_ /  | :|(_ o _) /    
    | . (_) `. | .---. |  |  .-----..---.     :_ _:      _.-`   | > (_)  )           \  '_ '`)    |  _`,/ \ _/  | > (_)  ) |  _`,/ \ _/  || (_,_).' __  
    |(_    ._) ' |   | '  \  '-   .'|   |     (_I_)   .'   _    |(  .  .-'            > (_)  )  __: (  '\_/ \   ;(  .  .-' : (  '\_/ \   ;|  |\ \  |  | 
    |  (_.\.' /  |   |  \  `-'`   | |   |    (_(=)_)  |  _( )_  | `-'`-'|___         (  .  .-'_/  )\ `"/  \  ) /  `-'`-'|___\ `"/  \  ) / |  | \ `'   / 
    |       .'   |   |   \        / |   |     (_I_)   \ (_ o _) /  |        \         `-'`-'     /  '. \_/``".'    |        \'. \_/``".'  |  |  \    /  
    '-----'`     '---'    `'-...-'  '---'     '---'    '.(_,_).'   `--------`           `._____.'     '-----'      `--------`  '-----'    ''-'   `'-'   
                                                                                                                                                    

    Color modes are essential to the digital display of data. There are many ways to express color and none of them work the same. Enumerated below are 4 different color modes that you may use in your programming.

### RGB(A)

    RGB stands for Red-Green-Blue. These are the 3 primary colors of the additive color wheel. When we mix varying intensities of light in these colors, we can produce any color visible to the human eye. Because light is the medium of this color wheel, it is the color mode used with computer screens. Every pixel on a screen has very small red, green, and blue lights which turn on with different intensities.

    RGB color mode also has a 4th optional parameter: alpha. This represents the opacity of the color. 

    Typically all values range from 0-255
### CMYK

    CMYK stands for Cyan-Magenta-Yellow-Black. The colors cyan, magenta, and yellow are the primary colors of the subtractive color wheel. While this color mode can be used digitally, its main application is in the physical world. Printers use these colors in the form of ink to achieve all colors visible to the human eye. Unlike RGB color, CMYK does not work with light as a medium, rather colored substances are mixed to generate the colors (like the ink in the printer). It is still possible to use digitally but much less common. 

## HSV

    HSV stands for Hue-Saturation-Value. This is another common digital color mode. A hue (out of 360 degrees) is specified which correlates to a rotation around an RGB color wheel. Saturation dictates how white the color. this moves the point on the color wheel inward (less saturated) or outward (more saturated). Finally, value adds a 3rd dimension downards. This specifies how dark the color is.

    Hue is typically measured in degrees out of 360
    Saturation and Value are typically measured in percentages out of 100%
### Hex


    Hex color is actually just another way of expressing RGB color. It is comprised of 6 characters which represent red, green, and blue values with the base-16 hexadecimal system (0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f). The first 2 characters represent the amount of red expressed, the second 2 correlates to green, and the last 2 correlate to blue.
