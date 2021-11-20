from PIL import Image, ImageDraw
import PIL
import matplotlib.pyplot as plt
from matplotlib.pyplot import bar

im0 = PIL.Image.open('filename.PNG')
width,height=im0.size
matr=[]

for x in range(width):
    for y in range(height):
        matr.append(im0.getpixel((x,y))[0])
matr0=[]
for i in matr:
    f=i
    if f in matr0:
        pass
    else:
        matr0.append(f)
matr0.sort()
lst0=[i for i in range(len(matr0))]
lst1=[matr.count(i) for i in matr0]
barlist=plt.bar(lst0, lst1)
for i in range(len(lst0)):
    c=matr0[i]/255
    barlist[i].set_color((c,c,c,1))

plt.show()
