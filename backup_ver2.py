# -*- coding:utf8 -*-
import os
import time

print('黄锋')
source = ['/Users/huangfeng/swa/notes']

target_dir = '/Users/huangfeng/swa/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir+os.sep+time.strftime('%Y%m%d')

now = time.strftime('%H%m%s')

target = today+os.sep+ now+'.zip'
if not os.path.exists(today):
    os.mkdir(today)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running')
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup Failed')
