Color={
    "black":"#000000",
    "dimgray":"#696969",
    "gray":"#808080",
    "darkgray":"#a9a9a9",
    "silver":"#c0c0c0",
    "lightgray":"#d3d3d3",
    "gainsboro":"#dcdcdc",
    "whitesmoke":"#f5f5f5",
    "white":"#ffffff",
    "snow":"#fffafa",
    "ghostwhite":"#f8f8ff",
    "floralwhite":"#fffaf0",
    "linen":"#faf0e6",
    "antiquewhite":"#faebd7",
    "papayawhip":"#ffefd5",
    "blanchedalmond":"#ffebcd",
    "bisque":"#ffe4c4",
    "moccasin":"#ffe4b5",
    "navajowhite":"#ffdead",
    "peachpuff":"#ffdab9",
    "mistyrose":"#ffe4e1",
    "lavenderblush":"#fff0f5",
    "seashell":"#fff5ee",
    "oldlace":"#fdf5e6",
    "ivory":"#fffff0",
    "honeydew":"#f0fff0",
    "mintcream":"#f5fffa",
    "azure":"#f0ffff",
    "aliceblue":"#f0f8ff",
    "lavender":"#e6e6fa",
    "lightsteelblue":"#b0c4de",
    "lightslategray":"#778899",
    "slategray":"#708090",
    "steelblue":"4682b4",
    "royalblue":"#4169e1",
    "midnightblue":"#191970",
    "navy":"#000080",
    "darkblue":"#00008b",
    "mediumblue":"#0000cd",
    "blue":"#0000ff",
    "dodgerblue":"#1e90ff",
    "cornflowerblue":"#1e90ff",
    "deepslyblue":"#00bfff",
    "lightskyblue":"#87cefa",
    "skyblue":"#87ceeb",
    "lightblue":"#add8e6",
    "powderblue":"#b0e0e6",
    "paleturquoise":"#afeeee",
    "lightcyan":"#e0ffff",
    "cyan":"#00ffff",
    "aqua":"#00ffff",
    "turquoise":"#40e0d0",
    "mediumturquoise":"#48d1cc",
    "darkturquoise":"#00ced1",
    "lightseagreen":"#20b2aa",
    "cadetblue":"#5f9ea0",
    "darkcyan":"#008b8b",
    "teal":"#008080",
    "darkslategray":"#2f4f4f",
    "darkgreen":"#006400",
    "green":"#008000",
    "forestgreen":"#228b22",
    "seagreen":"#2e8b57",
    "mediumseagreen":"#3cb371",
    "mediumaquamarine":"#66cdaa",
    "darkseagreen":"#8fbc8f",
    "aquamarine":"#7fffd4",
    "palegreen":"#98fb98",
    "lightgreen":"#90ee90",
    "springgreen":"#00ff7f",
    "mediumspringgreen":"#00ff7f",
    "lawngreen":"#7cfc00",
    "chartreuse":"#7fff00",
    "greenyellow":"#adff2f",
    "lime":"#32cd32",
    "limegreen":"#9acd32",
    "yellowgreen":"#9acd32",
    "darkolivegreen":"#556b2f",
    "olivedrab":"#6b8e23",
    "olive":"#808000",
    "darkkhaki":"#bdb76b",
    "palegoldenrod":"#eee8aa",
    "cornsilk":"#fff8dc",
    "beige":"#f5f5dc",
    "lightyellow":"#ffffe0",
    "lightgoldenrodyellow":"#fafad2",
    "lemonchiffon":"#fffacd",
    "wheat":"#f5deb3",
    "burlywood":"#deb887",
    "tan":"#d2b48c",
    "khaki":"#f0e68c",
    "yellow":"#ffff00",
    "gold":"#ffd700",
    "orange":"#ffa500",
    "sandybrown":"#f4a460",
    "darkorange":"#ff8c00",
    "goldenrod":"#daa520",
    "peru":"#cd853f",
    "darkgoldenrod":"#b8860b",
    "chocolate":"#d2691e",
    "sienna":"#a0522d",
    "saddlebrown":"#8b4513",
    "maroon":"#800000",
    "darkred":"#8b0000",
    "brown":"#a52a2a",
    "firebrick":"#b22222",
    "indianred":"#cd5c5c",
    "rosybrown":"#bc8f8f",
    "darksalmon":"#e9967a",
    "lightcoral":"#f08080",
    "salmon":"#fa8072",
    "lightsalmon":"#ffa07a",
    "coral":"#ff7f50",
    "tomato":"#ff6247",
    "orangered":"#ff4500",
    "red":"#ff0000",
    "crimson":"#dc143c",
    "mediumvioletred":"#c71585",
    "deeppink":"#ff1493",
    "hotpink":"#ff69b4",
    "paleviolet":"#db7093",
    "pink":"#ffc0cb",
    "lightpink":"#ffb6c1",
    "thistle":"#d8bfd8",
    "magenta":"#ff00ff",
    "fuchsia":"#ff00ff",
    "violet":"#ee82ee",
    "plum":"#dda0dd",
    "orchid":"#da70d6",
    "mediumorchid":"#ba55d3",
    "darkorchid":"#9932cc",
    "darkviolet":"#9400d3",
    "darkmagenta":"#8b008b",
    "purple":"#800080",
    "indigo":"#4b0082",
    "darkslateblue":"#483d8b",
    "blueviolet":"#8a2be2",
    "mediumpurple":"#9370db",
    "slateblue":"#6a5acd",
    "mediumslateblue":"#7b68ee"
}

def __Cget(colorName):
    return Color.get(colorName.lower())

def Name2RGB(colorName):
    tmp = __Cget(colorName)
    if(tmp !=None):
        return (int(tmp[1:3],16), int(tmp[3:5],16), int(tmp[5:7],16))
    else:
        return None

def Code2RGB(colorCode):
    if(colorCode.startswith('#')):
        return (int(colorCode[1:3],16), int(colorCode[3:5],16), int(colorCode[5:7],16))
    else:
        return (int(colorCode[0:2],16), int(colorCode[2:4],16), int(colorCode[4:6],16))

def NoSharp(colorName):
    tmp = __Cget(colorName)
    if(tmp !=None):
        return tmp[1:7]
    else:
        return None