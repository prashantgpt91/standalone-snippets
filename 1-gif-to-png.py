import Image,glob,os

files = glob.glob("22.gif")

for imageFile in files:
    filepath,filename = os.path.split(imageFile)
    filterame,exts = os.path.splitext(filename)
    print "Processing: " + imageFile,filterame
    im = Image.open(imageFile)
    im.save( filterame+ '.png','PNG')
