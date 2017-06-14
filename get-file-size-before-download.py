#!/usr/bin/python
# display size of a remote file without downloading

from __future__ import print_function
import sys
import requests

# number of bytes in a megabyte
MBFACTOR = float(1 << 20)

response = requests.head(sys.argv[1], allow_redirects=True)

print("\n".join([('{:<40}: {}'.format(k, v)) for k, v in response.headers.items()]))
size = response.headers.get('content-length', 0)
print('{:<40}: {:.2f} MB'.format('FILE SIZE', int(size) / MBFACTOR))

