# -*- coding: utf-8 -*-
import qrcode;
import codecs;
import getpass;
import sys;

qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3,
        border=4,
        )

qr.add_data(getpass.getuser());
qr.make(fit=True);

f = sys.stdout # codecs.open("test.txt", "w", encoding='utf8');

img = qr.make_image();
scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`. "
image = img.load();
W, H = img.size[0], img.size[1]

for i in range(H):
    for j in range(W):
        pixel = image[i, j]
        block = u'█';
        block = block + block;
        f.write((block if pixel == 255 else '  ').encode('utf-8'));
    f.write("\n");
