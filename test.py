import os
from app import *

# Test1 : 获取一页
result = get_one_page(os.getenv('URL') + '?offset=0')
with open('tmps/test1.html', 'w') as f:
    f.write(result)
