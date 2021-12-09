#边界匹配
import re
qq = '100000001'
# qq号位数是否符合4-8位
r = re.findall('000',qq)
print(r)