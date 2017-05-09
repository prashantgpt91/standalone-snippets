import boto
import os
import urllib
import subprocess

#Given a S3 url, script is used to download a file. This snippet can also be used for general purpose downloading
#Let's say files are in a path like this A/B/C/42.png

def download_using_url(url):
    bucket_name = 'A'
    conn = boto.connect_s3('Access key ID', 'Secret access key')
    print("Downloading image ...")
    img = urllib.urlretrieve(url)
    x = img[0]
    y = os.path.dirname(os.path.abspath(__file__))
    command = 'cp ' + x + ' ' + y
    subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    """
    If want to change name and format of image file to save
    cv2.imwrite(img[0])
    img = cv2.imread(img[0])
    cv2.imwrite("12.tiff", img)
    """

if __name__ == "__main__":
    download_using_url('https://s3.amazonaws.com/XYZ/60.jpg')

