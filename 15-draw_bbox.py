import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import cv2


im = np.array(Image.open('C:\\Users\\pgupta5\\Pictures\\397.png'), dtype=np.uint8)
draw = im.copy()
draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# Create a Rectangle patch
rect = patches.Rectangle((4,762),1020,203,linewidth=2,edgecolor='g',facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect)
plt.figure(figsize=(15, 15))
plt.axis('off')
plt.imshow(draw)
plt.show()
