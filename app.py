import barcode
from barcode.writer import ImageWriter
ean = barcode.get('CODE128', '1234567890123456', writer=ImageWriter())
options = {
  'module_width': 1,
  'module_height': 20,
  'quiet_zone': 20,
  'font_size': 40,
  'text_distance': 1
}

filename = ean.save('CODE128', options=options)