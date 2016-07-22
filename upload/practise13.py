#coding=utf-8
x=int(raw_input('put in a number'))
print '%d\n'%x,id(x),type(x)
y=x
del x
print y
#print x
#在python里一切都是对象，包括输入的一个数字，都是对象，而且只要是相同的
#数字就会被认为是同一个对象，在内存中，一个对象会保存引用计数，这里的
#在执行了y=x之后，对象的引用计数就加1，而在执行了del x 这一行只有，x这个
#引用就被删除，但是对象本身并不会被删除，因为还有y在引用这个数字对象，如果y
#也被del掉了，那这个对象就真的被回收掉了