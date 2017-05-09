import boto

# count number of files in S3 bucket
#Let's say files are in a path like this A/B/C/42.png

def count_objects_in_bucket():
    bucket_name = 'A'
    s3 = boto.connect_s3('Access key ID', 'Secret access key')
    bucket = s3.get_bucket(bucket_name)  # get bucket
    count = 0
    for key in bucket.list('B/C'):  # list objects at a given prefix
        print key.name
        count = count + 1
    print count


if __name__ == "__main__":
    p = count_objects_in_bucket()
    print p
