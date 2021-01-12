import os
from app import *

# 存储test输出洁面的文件夹
if os.path.exists('tmps'):
    os.mkdir('tmps')

# Test1 : 获取一页
result = get_one_page(os.getenv('URL') + '?offset=0')
with open('tmps/test1.html', 'w') as f:
    f.write(result)
