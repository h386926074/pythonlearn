# -*- coding:utf8 -*-
import os
import time

# 中文
source = ['/Users/huangfeng/swa/notes']

target_dir = '/Users/huangfeng/swa/backup'


target = target_dir + os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')

if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')
