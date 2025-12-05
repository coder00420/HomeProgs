def stair_variations(cubics, min_cubics = 1, variations = 1):
    if cubics == 1: return variations
    next_layer_cubics = cubics - min_cubics
    while next_layer_cubics > 0 and next_layer_cubics > cubics - next_layer_cubics:
        variations += 1
        variations = stair_variations(next_layer_cubics, cubics - next_layer_cubics + 1, variations)
        next_layer_cubics -= 1
    return variations
res = stair_variations(int(open('INPUT.TXT', 'r').read()))
open('OUTPUT.TXT', 'w').write(str(res))