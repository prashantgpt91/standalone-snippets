import boto
import logging


#Let's say files are in a path like this A/B/C/42.png
# download all files from S3 bucket

def s3_download():
    bucket_name = 'A'
    conn = boto.connect_s3('Access key ID', 'Secret access key')
    bucket = conn.get_bucket(bucket_name)

    for key in bucket.list('B/C'):
        try:
            res = key.get_contents_to_filename(key.name)
        except:
            logging.info(key.name + ":" + "FAILED")

if __name__ == "__main__":
    s3_download()


