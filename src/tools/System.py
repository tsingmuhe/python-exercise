import psutil
import requests

def memissue():
    print('内存信息：')
    mem = psutil.virtual_memory()
    print(mem)

def cuplist():
    print('磁盘信息：')
    disk = psutil.disk_partitions()
    diskuse = psutil.disk_usage('/')
    print(disk)
    print(diskuse)

memissue()
print('*******************')
cuplist()