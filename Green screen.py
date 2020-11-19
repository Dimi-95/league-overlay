from PIL import Image
import sys
import math

if len(sys.argv) < 3:
    sys.exit('usage: gs.py <input> <output>')

input_filename = sys.argv[1]
output_filename = sys.argv[2]

input_img = Image.open(input_filename)
output_img = Image.new("RGBA", input_img.size)

for y in xrange(input_img.size[1]):
    for x in xrange(input_img.size[0]):
        p = input_img.getpixel((x, y))
        d = math.sqrt(math.pow(p[0], 2) + math.pow((p[1] - 255), 2) + math.pow(p[2], 2))

        if d > 128:
            d = 255

        output_img.putpixel((x, y), (p[0], min(p[2], p[1]), p[2], int(d)))

output_img.save(output_filename, "PNG")