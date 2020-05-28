import os

for subdir, dirs, files in os.walk(r'C:\Users\admin'):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".jpg") or filepath.endswith(".png"):
            print (filepath)
