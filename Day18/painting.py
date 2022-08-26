import colorgram

def extract_colors(filename, color_count):
    colors = colorgram.extract(filename, color_count)
    color_list = []
    for color in colors:
        color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return color_list


color_palette = extract_colors('./damienhirst1.jpg', 10)
print(type(color_palette[0]))