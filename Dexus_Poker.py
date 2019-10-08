# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:20:01 2019

@author: Spirit-Amos

德州扑克窗口
"""

import tkinter as tk
import time
import random
from PIL import Image,ImageTk
import numpy as np
from collections import Counter

window = tk.Tk()
window.title('德州扑克Dexus Poker Game')
window.geometry('1200x700')

image00 =Image.open('background.jpg')
background_image = ImageTk.PhotoImage(image00)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

image02 =Image.open('sex03.jpg')
image02_1=image02.resize((340,130),Image.ANTIALIAS)
image03 =Image.open('sex02.jpg')
image03_1=image03.resize((120,130),Image.ANTIALIAS)
image_sex1 = ImageTk.PhotoImage(image02_1)
label5 = tk.Label(window, image=image_sex1)
label5.place(x=0,y=0,width=340,height=130)
image_sex2 = ImageTk.PhotoImage(image03_1)
label7 = tk.Label(window, image=image_sex2)
label7.place(x=350,y=0,width=120,height=130)

list = []
for i in range(1,53):
    list.append(i)

Var = tk.StringVar() 
Var2 = tk.StringVar()  
Var3 = tk.StringVar()  
def Dexus_Judge(list):
    a=(list[3],list[4],list[5],list[7],list[9],list[0],list[1])
    b=sorted(a)
    king=0
    if b[4]-b[0]==4 and b[4]%13>=4:
        king=1
    if b[5]-b[1]==4 and b[5]%13>=4:
        king=1
    if b[6]-b[2]==4 and b[6]%13>=4:
        king=1
    if b[0]%13==1 and b[3]-b[0]==12 and b[1]-b[0]==9:
        king=1
    if b[1]%13==1 and b[4]-b[1]==12 and b[2]-b[1]==9:
        king=1
    if b[2]%13==1 and b[5]-b[2]==12 and b[3]-b[2]==9:
        king=1   
    #判断是否存在同花
    sameflower=0
    if (b[4]-b[0]+b[0]%13) < 14 and b[0]%13!=0:
        sameflower=1
    if b[5]-b[1]+b[1]%13 < 14 and b[1]%13!=0:
        sameflower=1
    if b[6]-b[2]+b[2]%13 < 14 and b[2]%13!=0:
        sameflower=1
    #判断是否存在顺子牌型
    shunzi=0
    bb=sorted(a)
    c=[]
    for i in range(0,7):
        bb[i]=bb[i]%13
        if bb[i]==0:
            bb[i]=13
    Sort_b=sorted(bb)
    Set_b=[]
    for d in Sort_b:
        if d not in Set_b:
            Set_b.append(d)   
    if len(Set_b)==7:
        num=[Set_b[1]-Set_b[0],Set_b[2]-Set_b[1],Set_b[3]-Set_b[2],Set_b[4]-Set_b[3],Set_b[5]-Set_b[4],Set_b[6]-Set_b[5]]
        if num[0:4]==[1,1,1,1] or num[1:5]==[1,1,1,1] or num[2:6]==[1,1,1,1]:
            shunzi=1
    if len(Set_b)==6:
        num=[Set_b[1]-Set_b[0],Set_b[2]-Set_b[1],Set_b[3]-Set_b[2],Set_b[4]-Set_b[3],Set_b[5]-Set_b[4]]
        if num[0:4]==[1,1,1,1] or num[1:5]==[1,1,1,1]:
            shunzi=1
    if len(Set_b)==5:
        num=[Set_b[1]-Set_b[0],Set_b[2]-Set_b[1],Set_b[3]-Set_b[2],Set_b[4]-Set_b[3]]
        if num[0:4]==[1,1,1,1]:
            shunzi=1 
    #判断重复牌型
    FourCards=0
    Fullhouse=0
    TriCards=0
    Twopairs=0
    Pairs=0
    high0=0
    high1=0
    bbb=sorted(a)
    for i in range(0,7):
        bbb[i]=bbb[i]%13
        if bbb[i]==0:
            bbb[i]=13
        elif bbb[i]==1:
            bbb[i]=14
    c=Counter(bbb)
    bbb=sorted(bbb)
    if bbb[6]>10:
        high0=1
    x=c.most_common(2)[0][1]
    y=c.most_common(2)[1][1]
    if x==4:
        FourCards=1
    if x==3 and y>=2:
        Fullhouse=1
    if x==3 and y==1:
        TriCards=1
    if x==2 and y==2:
        Twopairs=1
    if x==2 and y==1:
        Pairs=1
    if x==1 and y==1 and high0==1:
        high1=1
    if king==1:
        labelVar1 ="It's Amazing!! 你得到了一个同花顺"
    else:
        if FourCards==1:
            labelVar1 ="It's Amazing!! 你得到了一个金刚"
        else:
            if Fullhouse==1:
                labelVar1 ="It's Amazing!! 你得到了一个葫芦"
            else:
                if sameflower==1:
                    labelVar1 ="It's Amazing!! 你得到了一个同花"
                else:
                    if shunzi==1:
                        labelVar1 ="It's Amazing!! 你得到了一个顺子"
                    else:
                        if TriCards==1:labelVar1 ="It's Excellent!! 你获得了三条"
                        elif Twopairs==1:labelVar1 ="It's Excellent!! 你获得了两对"
                        elif Pairs==1:labelVar1 ="It's Good!! 你获得了一对"
                        elif high1==1:
                            labelVar1 ="It's Good!! 你获得了高牌!!"
                        else:
                            labelVar1 ="It's Fabulous!! 你获得了一副烂牌!!"
    return labelVar1

counter = 0

def XiPai():
    global list
    global counter
    counter+=1
    random.shuffle(list)
    image06=Image.open('Pokerpapers'+'\\'+'55.png')
    image07=Image.open('Pokerpapers'+'\\'+'56.png')
    if counter%2 ==1:
        publics= np.hstack((image06,image06,image06,image06,image06))
        hands = np.hstack((image06,image06))
    else:
        publics= np.hstack((image07,image07,image07,image07,image07))
        hands = np.hstack((image07,image07))
    publics=Image.fromarray(publics)
    hands=Image.fromarray(hands)
    photo1=ImageTk.PhotoImage(publics)
    label2.config(image=photo1)
    label2.image=photo1
    photo2=ImageTk.PhotoImage(hands)
    label3.config(image=photo2)
    label3.image=photo2
    Var.set("已重新洗牌，可以发牌。")
    Var2.set(" ")
    Var3.set('第 '+str(counter)+' 手牌')
    
def FaPai():
    global list
    global counter
    image06=Image.open('Pokerpapers'+'\\'+'55.png')
    image07=Image.open('Pokerpapers'+'\\'+'56.png')
    if counter%2 ==1:
        publics= np.hstack((image06,image06,image06,image06,image06))
    else:
        publics= np.hstack((image07,image07,image07,image07,image07))      
    publics=Image.fromarray(publics)
    image11=Image.open('Pokerpapers'+'\\'+str(list[0])+'.png')
    image12=Image.open('Pokerpapers'+'\\'+str(list[1])+'.png')
    hands = np.hstack((image11,image12))
    hands=Image.fromarray(hands)
    photo1=ImageTk.PhotoImage(publics)
    label2.config(image=photo1)
    label2.image=photo1
    photo2=ImageTk.PhotoImage(hands)
    label3.config(image=photo2)
    label3.image=photo2
    a=(list[3],list[4],list[5],list[7],list[9],list[0],list[1])
    f=open('./files/Poker01.txt','a')
    f.write(str(a) + "\n")
    f.close()
    #Var.set("性感荷官，在线发牌。")
    Var.set("Street 1：翻牌前 preFlop")
    
def Flop():
    global list
    global counter
    image01=Image.open('Pokerpapers'+'\\'+str(list[3])+'.png')
    image02=Image.open('Pokerpapers'+'\\'+str(list[4])+'.png')
    image03=Image.open('Pokerpapers'+'\\'+str(list[5])+'.png')
    image06=Image.open('Pokerpapers'+'\\'+'55.png')
    image07=Image.open('Pokerpapers'+'\\'+'56.png')
    if counter%2 ==1:
        publics= np.hstack((image01,image02,image03,image06,image06))
    else:
        publics= np.hstack((image01,image02,image03,image07,image07)) 
    publics=Image.fromarray(publics)
    photo1=ImageTk.PhotoImage(publics)
    label2.config(image=photo1)
    label2.image=photo1
    Var.set("Street 2：翻牌Flop")

def Turn():
    global list
    global counter
    image01=Image.open('Pokerpapers'+'\\'+str(list[3])+'.png')
    image02=Image.open('Pokerpapers'+'\\'+str(list[4])+'.png')
    image03=Image.open('Pokerpapers'+'\\'+str(list[5])+'.png')
    image04=Image.open('Pokerpapers'+'\\'+str(list[7])+'.png')
    image06=Image.open('Pokerpapers'+'\\'+'55.png')
    image07=Image.open('Pokerpapers'+'\\'+'56.png')
    if counter%2 ==1:
        publics= np.hstack((image01,image02,image03,image04,image06))
    else:
        publics= np.hstack((image01,image02,image03,image04,image07)) 
    publics=Image.fromarray(publics)
    photo1=ImageTk.PhotoImage(publics)
    label2.config(image=photo1)
    label2.image=photo1
    Var.set("Street 3：转牌Turn")

def River():
    global list
    image01=Image.open('Pokerpapers'+'\\'+str(list[3])+'.png')
    image02=Image.open('Pokerpapers'+'\\'+str(list[4])+'.png')
    image03=Image.open('Pokerpapers'+'\\'+str(list[5])+'.png')
    image04=Image.open('Pokerpapers'+'\\'+str(list[7])+'.png')
    image05=Image.open('Pokerpapers'+'\\'+str(list[9])+'.png')
    publics= np.hstack((image01,image02,image03,image04,image05))
    publics=Image.fromarray(publics)
    photo1=ImageTk.PhotoImage(publics)
    label2.config(image=photo1)
    label2.image=photo1
    Var.set("Street 4：河牌River")
    
labelVar1 = tk.StringVar()
def YanPai():
    global list
    labelVar1=Dexus_Judge(list)
    Var2.set(labelVar1)


def eventhandler(event):
    if event.keysym == 'w':
        XiPai()
    elif event.keysym == 'h':
        FaPai()
    elif event.keysym == 'f':
        Flop()
    elif event.keysym == 't':
        Turn()
    elif event.keysym == 'r':
        River()
    elif event.keysym == 'y':
        YanPai() 

label1 = tk.Label(window,
                 textvariable=Var,
                 width=20,bg='orange',fg='black',
                 font=('simfang',22))
label1.place(x=540,y=20,width=380,height=50)
button1 = tk.Button(window,text='洗牌',command=XiPai)
button1.bind_all('<KeyPress>',eventhandler)
button1.place(x=640,y=95,width=40,height=25)
button2 = tk.Button(window,text='发牌',command=FaPai)
button2.bind_all('<KeyPress>',eventhandler)
button2.place(x=700,y=95,width=40,height=25)
button3 = tk.Button(window,text='Flop',command=Flop)
button3.bind_all('<KeyPress>',eventhandler)
button3.place(x=780,y=95,width=40,height=25)
button3 = tk.Button(window,text='Turn',command=Turn)
button3.bind_all('<KeyPress>',eventhandler)
button3.place(x=840,y=95,width=40,height=25)
button3 = tk.Button(window,text='River',command=River)
button3.bind_all('<KeyPress>',eventhandler)
button3.place(x=900,y=95,width=40,height=25)
button3 = tk.Button(window,text='牌力判断',command=YanPai)
button3.bind_all('<KeyPress>',eventhandler)
button3.place(x=1000,y=95,width=80,height=25)

label2 = tk.Label(window,bg='black')
label2.place(x=60,y=145,width=1040,height=250)
label3 = tk.Label(window,bg='black')
label3.place(x=220,y=425,width=400,height=250)

label4 = tk.Label(window,
                 textvariable=Var2,
                 width=20,bg='gray',fg='yellow',
                 font=('simfang',20))
label4.place(x=650,y=470,width=500,height=100)

label6 = tk.Label(window,
                 textvariable=Var3,
                 width=20,bg='yellow',fg='blue')
                 #font=('simfang',24))
label6.place(x=1110,y=0,width=90,height=30)

text =tk.Text(window)
text.place(x=650,y=580,width=500,height=60)
text.insert(tk.END,"多行文本显示测试",'big')

canvas = tk.Canvas(width=320, height=480, bg='black',relief='sunken')
canvas.place(x=20,y=430,width=160,height=240)

sleep_time = 0.025
im = Image.open('sex01.gif')
mode = 'partial'
def process():
    global sleep_time
    global im 
    global mode
    i = 0
    try:
       while True:
           new_frame = Image.new('RGBA', im.size)
           new_frame.paste(im, (0, 0), im.convert('RGBA'))
           new_frame=new_frame.resize((180,240),Image.ANTIALIAS)
           photo1 = ImageTk.PhotoImage(new_frame)
           canvas.create_image(120, 120, image = photo1,tag = "pic") 
           canvas.update()
           time.sleep(0.025)
           canvas.delete("pic")    
           i += 1
           im.seek(im.tell() + 1)   
    except EOFError:
        pass
    im.seek(im.tell() -36)
for j in range(1,5000):
    process()

def menuClick():
    global counter
    #label.config(text='第'+str(counter)+' 次点击')
    counter+=1
    
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label = '文件',menu = filemenu)
filemenu.add_command(label = '新建',command=menuClick)
filemenu.add_command(label = '打开',command=menuClick)
filemenu.add_command(label = '保存',command=menuClick)
filemenu.add_separator()
filemenu.add_command(label = '退出',command=window.quit)

editmenu = tk.Menu(menubar)
menubar.add_cascade(label = '编辑',menu = editmenu)
editmenu.add_command(label = '剪切',command=menuClick)
editmenu.add_command(label = '复制',command=menuClick)
editmenu.add_command(label = '粘贴',command=menuClick)


window.config(menu=menubar)
window.mainloop()


