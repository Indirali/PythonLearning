print(abs(-20))#绝对值
#print(abs('12'))#提示类型错误，只能接收一个参数

print(max(1,2,3,4,5,6,7,8,9,0))#求最大值，可以接受多个参数

int('123')#把其他数据类型转化成整数
int(123.43)
float('12.34')
str(123)
bool(1)#True
bool('')#False

#函数名就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个'别名'
a = abs #变量a指向abs函数
a(-1) #也可以通过a调用abs函数

#测试
n1 = 255
n2 = 1000

print(hex(n1),hex(n2))

