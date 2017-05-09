import boto
from functools import cmp_to_key

# return latest added/modified file in AWS S3 bucket

def s3_latest_file():
    bucket_name = 'cloudadic'
    conn = boto.connect_s3('Access key ID', 'Secret access key')
    bucket = conn.get_bucket(bucket_name)
    l = [(k.last_modified, k) for k in bucket]
    key = sorted(l, key=cmp_to_key(lambda x, y: (x[0] > y[0]) - (x[0] < y[0])))[-1][1]
    res = key.get_contents_to_filename('123.jpg')



if __name__ == "__main__":
    s3_latest_file()


