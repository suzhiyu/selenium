# print("   *\n  ***\n ****\n******\n ****\n  ***\n   *\n")

#
# def inputtype(self):
#  print(type(self))
#
#
# if __name__ == '__main__':
#     x=input('请输入任何内容显示的你数据类型')
#     inputtype(x)

# pi=3.1415926
#转换成整数
# print(int(pi))
# print(type(int(pi)))
#转换字符串
# print(str(pi))
# print(type(str(pi)))
# price=float(input('输入商品价格'))
# pay=price*0.88
# print('您需要付款'+str(pay)+'元')
#
# print('您需要付款{0:.6}元'.format(pay))
# #保留5位小数
# print('您需要付款{0:.5}元'.format(pay))
# #四舍五入
# print('您需要付款{0:.2f}元'.format(pay))
# #前导0 可以省略
# print('您需要付款{:.2f}元'.format(pay))
#
# print('您需要付款{:2.2f}元'.format(1/999))

#
# print('您需要付款{}元'.format(19999999/999))
#
# print('您需要付款{0:015.3f}元'.format(19999999/999))
#
# print('您需要付款{0:015.3%}元'.format(19999999/999))
#
# print('您需要付款{0:015.3E}元'.format(19999999/999))
#
# print('您需要付款{0:015.3e}元'.format(19999999/999))


file=open('fuxuan.html',encoding='utf-8')
print(file.read())
file.close()


file =open('txt.txt','w',encoding='utf-8')
file.write('我的新鞋的文件 \n 换行')
file.close()







