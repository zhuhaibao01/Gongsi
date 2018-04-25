from tkinter import *
root=Tk()
# print(type(root))
root.title("我是创建的第一个窗口")
# x=Label(root,text='我是一个label')            # 一个空白的label
# x=Label(root,bitmap='warning')                # 一个图片 warnIng
# x=Label(root,fg='red',bg='blue',text='xinxing') # fg 前景色，bg后景色，可以看出标签的宽度和高度
# x=Label(root,fg='red',bg='blue',text='xinxing',width=30,height=5) # 设置标签的宽度和高度
# def xin():
#     print('aaa')
# x=Button(root,text='clickme',command=xin)      # button点击触发事件
# def x1():
#     print("print 01")
# def x2(event):
#     print(event.time,event.type)
# b1=Button(root,text='button1',command=x1)
# b1.pack()
# b2=Button(root,text='button2')
# b2.bind("<Enter>",x2)
# b2.pack()                                                    # 默认点击后执行相关的函数
# Entry(root,text='input your name',fg='red',bg='blue',show='*').pack()   # 输入框,*为密码框
# e=Entry(root)
# e.pack()
# def kk():
#     x=e.get()
#     print(x)
# b=Button(root,text='getmessage',command=kk)
# b.pack()                                                    # 单击按钮，能获取输入框内容
# xmenu=Menu(root)       # 新建一个菜单
# root["menu"]=xmenu      # 将菜单的属性设置为生成的属性
# print(type(xmenu))
# def xin():
#     print( 'cai dan 01 ')
#
# for i in ('java','app','c','php'):
#     xmenu.add_command(label=i,command=xin)
# def xin():
#     print('can dan 01')
# menubar=Menu(root)
# xmenu=Menu(menubar,tearoff=0)
# # for i  in ['zhu','hai','bao']:
#     # menubar.add_command(label=i,command=xin)
# # for i  in ['java','app','c','php']:
# #     xmenu.add_command(label=i,command=xin)
# menubar.add_cascade(label='progame',menu=xmenu)
# root['menu']=menubar                                     #二级菜单
def xin():
    print( 'cai dan 01 ')
xmenu=Menu(root)
xxmenu=Menu(xmenu,tearoff=0)
root['menu']=xmenu
xmenu.add_cascade(label='我是一级菜单',menu=xxmenu)
xxmenu.add_command(label='我是二级菜单')
root.mainloop()                                            #最简单的二级菜单