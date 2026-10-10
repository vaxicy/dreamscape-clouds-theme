"""Generate the single transparent 128px cloud mark with antialiased edges."""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SCALE = 4
im = Image.new('RGBA', (128*SCALE, 128*SCALE))
d = ImageDraw.Draw(im)

def ellipse(box, fill):
    d.ellipse(tuple(int(v*SCALE) for v in box), fill=fill)

def rounded(box, radius, fill):
    d.rounded_rectangle(tuple(int(v*SCALE) for v in box), radius=radius*SCALE, fill=fill)

def cloud(x, y, w, h, fill):
    ellipse((x, y+h*.35, x+w*.43, y+h), fill)
    ellipse((x+w*.2, y, x+w*.7, y+h*.82), fill)
    ellipse((x+w*.58, y+h*.25, x+w, y+h), fill)
    rounded((x+w*.12, y+h*.5, x+w*.87, y+h), int(h*.22), fill)

# Tall crescent silhouette, open towards the stars, over a low cloud bank.
ellipse((13, 10, 107, 108), '#CDC6ED')
ellipse((42, 2, 120, 85), (0, 0, 0, 0))
cloud(43, 77, 77, 29, '#C5DAF6')
rounded((31, 108, 94, 112), 2, '#C5DAF6')
rounded((50, 118, 103, 122), 2, '#E2CFF4')
d.polygon([(x*SCALE,y*SCALE) for x,y in [(91,27),(95,38),(106,42),(95,46),(91,57),(87,46),(76,42),(87,38)]], fill='#B6C7EF')
ellipse((65, 17, 71, 23), '#DAB1F0')
ellipse((110, 61, 115, 66), '#CDC6ED')
im = im.resize((128,128), Image.Resampling.LANCZOS)
target = ROOT/'logo/logo128.png'
target.parent.mkdir(parents=True, exist_ok=True)
im.save(target)
assert im.size == (128,128) and im.mode == 'RGBA'
print(f'Generated {target}: 128x128 RGBA')

