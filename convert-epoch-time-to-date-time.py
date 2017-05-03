import datetime

def convert_time(self):
    tsepoch = float(self.split(".")[0])
    return str(datetime.datetime.fromtimestamp(tsepoch)).split('.')[0]


print convert_time('1456427378.000002')

