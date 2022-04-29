from PIL import Image

import os

size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir('.'):
    if f.endswith('.jpeg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save('pngfile/{}.png'.format(fn))
        
        i.thumbail(size_300)
        i.save('300/{}_300{}'.format(fn, fext))

        i.thumbail(size_700)
        i.save('700/{}_700{}'.format(fn, fext))