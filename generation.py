from PIL import Image
from random import randint

for x in range(540):
    thiscombo = []

    backgndId = randint(0, 14)
    thiscombo.append(backgndId)

    bodyId = randint(0, 3)
    thiscombo.append(bodyId)

    pantId = randint(0, 2)
    thiscombo.append(pantId)

    tuskId = randint(0, 2)
    thiscombo.append(tuskId)

    backgnd = Image.open("C:/Users/aryav/OneDrive/codeshenanigans/gnesh/backgnd/%d.png" % backgndId).convert('RGBA')
    body = Image.open("C:/Users/aryav/OneDrive/codeshenanigans/gnesh/body/%d.png" % bodyId).convert('RGBA')
    pant = Image.open("C:/Users/aryav/OneDrive/codeshenanigans/gnesh/pant/%d.png" % pantId).convert('RGBA')
    tusk = Image.open("C:/Users/aryav/OneDrive/codeshenanigans/gnesh/tusk/%d.png" % tuskId).convert('RGBA')

    backgnd.putalpha(256)
    bodyBackgnd = Image.alpha_composite(backgnd, body)
    bodyPant = Image.alpha_composite(bodyBackgnd, pant)
    final = Image.alpha_composite(bodyPant, tusk)
    print("Saving image number {} with combo {}".format(x, thiscombo))
    final.save("C:/Users/aryav/OneDrive/codeshenanigans/gnesh/results/%d.png" % x)