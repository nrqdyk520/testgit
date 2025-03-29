
data=[
    ['张三','男',23,1.56],
    ['李四','男',24,54],
    ['王五','女',12,34]
     ]
print(data)
print(data[0][2])


one,two=34,45
three=one+two
print(three==79)
four=98.78
five=76.35
seven=22.43
six=four-five
print(seven==six,f'预期：{seven}',f'实际：{six}')
print(seven==six,'预期：'%six,'实际：')

s='513030199910270010'
print(s)
print(s[0:6],s[6:6+8],s[-2],s[-1],s[-6:],sep=' ')
print(int(s[-2])%2==1)




three='zhan'
four='san'
five=three+four
five1=f'{three}{four}'
five2='%s%s'%(three,four)
print(five,five1,five2)
six=three*3
print(six)


three,four=int(input('数1：')),int(input('数2：'))
six=three+four
five=f'{three}+{four}={six}'
five1='%d+%d=%d'%(three,four,six)
five2=str(three)+'+'+str(four)+'='+str(six)
print(five,five1,five2,sep='\n')














print "tinydict['Name']: ", tinydict['Name']
print "tinydict['Age']: ", tinydict['Age']

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
tinydict['Age'] = 8 # 更新
tinydict['School'] = "RUNOOB" # 添加
 
 
print "tinydict['Age']: ", tinydict['Age']
print "tinydict['School']: ", tinydict['School']

#!/usr/bin/python
 
tup = ('physics', 'chemistry', 1997, 2000)
 
print tup
del tup
print "After deleting tup : "
print tup

year = int(input("输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print("{0} 不是闰年".format(year))


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
 
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5].



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)