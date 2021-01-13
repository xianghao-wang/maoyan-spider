import os
import json
from helps import *

# 存储test输出洁面的文件夹
if not os.path.exists('tmps'):
    os.mkdir('tmps')

# Test1 : 获取一页
result = get_one_page(os.getenv('URL') + '?offset=0')
with open('tmps/test1.html', 'w') as f:
    f.write(result)

# Test2: 解析html文本和写入文件
result_gen = parse_one_page(result)
for line in result_gen:
    write_to_file(line)
    