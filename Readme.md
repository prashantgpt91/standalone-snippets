# Standalone-snippets
This repo will contain standalone snippets.


> `Total count of snippets | 15`

 1.  snippet takes a gif image as an input and return a png image as output.
 
 2.  snippet uses [github access token](https://github.com/settings/tokens) and downloads at once all public repositories from any github account.
 
 3.  snippet will take epoch time as an input and datetime as output. Read more about epoch time [here](https://en.wikipedia.org/wiki/Unix_time)

 4.  snippet will download the latest added/modified file in a S3 bucket.
 
 5.  snippet will download all files from a given S3 bucket folder.
 
 6.  snippet will return file name of the most recent file.
 
 7.  snippet will download the file, given a URL.
 
 8.  snippet will count total objects in S3 bucket.

 9.  snippet will rename files in a particular folder serially starting from `1`. 

 10.  snippet will delete all the files from your slack team account. Good for free users, who usually get file storage warning. [Get Slack Legacy token from here](https://api.slack.com/custom-integrations/legacy-tokens).
 
 11.  snippet will get the file size before downloading it. Run it like this `python snippet.py url`
 
 12.  snippet will convert newline separated entries into python list.
 
 13.  snippet will convert list to json format, assuming key values must be suuplied to script.

 14. snippet will fetch complete details of your aws account in the form of json. To run the script, simply install `awscli` using `pip install awscli` in a virtualenv and run `aws configure`. To see the list of regions go [here](https://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region). To get access key and access secret key go [here](https://console.aws.amazon.com/iam/home?region=us-east-2#/users), select the user against which has permission to access all services, issue a key against it and use in `aws configure` command.


15.  snippet will draw bounding box over an image in the format of x1,y1,width, height.

16. snippet will iterate over all files in a folder recursively.

17. snippet will connect to aws account using access key, secret key and token.


 
 ## Meta

**License**

The code snippets are dedicated to the public domain. Use it as you please with no restrictions whatsoever.

**Questions? Comments?**

Post them to the [Repository Issues](https://github.com/x0v/standalone-snippets/issues/new). Thanks!

