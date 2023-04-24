
# # 一、整数

# 二进制
a = 0b101
print('a的十进制表示：%d' % a)
# 八进制
b = 0o101
print('b的十进制表示：%d' % b)
# 十六进制
c = 0x101
print('c的十进制表示：%d' % c)
# 十进制
d = 101
print('d的十进制表示：%d' % d)

# 二、浮点数
# 由整数和小数部分使用，python中的浮点数是双精度的，每个浮点数占8字节-1.8E308～1.8E308
print(0.1+0.2)

# 三、复数
a = complex(2,4)
b = 6
print(a)
print('a的实数部分是：',a.real,'a的虚部是：',a.imag)
print(complex(b))

# 四、布尔型
bool()
bool('')
bool(0)
bool([])

# 五、运算符
# + - * / //（整数除） %（取余）  **（幂运算）
# 逻辑运算符 与and 或or 非not
#

# 六、时间格式化
t = eval(input())
H=t//3600
t = t%3600
M = t//60
S = t % 60
print("{}:{}:{}".format(H,M,S))

# 七、字符串
s = 'HelloWorld'
s[0]
s[2:6]
s[-5:-2]
s[::-1]