#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from tkinter import Tk,Button
from tkinter.messagebox import showinfo
from tkinter import filedialog,PhotoImage,Label
import os
import logging
import picture_read,picture_print
#logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

 
class Mainpage(object):
  def __init__(self,root):
      self.root=root#定义内部变量root
      self.root.geometry('%dx%d' % (600, 400)) #设置窗口大小
      self.root.title('图形处理排版1.0')
      self.createPage()
 
  def createPage(self):
      a=Button(self.root, text='提示'.center(44,' '),command=self.Notice)
      a.grid(row=1,column=2)
      photo=PhotoImage(file="裁缝LOGO.png")
      label=Label(image=photo)
      label.image=photo
      label.grid(row=0,column=4,rowspan=1,columnspan=1)
  #a.grid_forget()
      Button(self.root, text='切图画框'.center(40,' '),command=self.pic_read).grid(row=2,column=3,columnspan=2,pady=10)
      Button(self.root, text='图形RIP'.center(42,' '), command=self.pic_print).grid(row=3,column=3,columnspan=2,pady=10)
      Button(self.root, text='切图画框_图形RIP'.center(34,' '), command=self.pic_read_and_print).grid(row=4,column=3,columnspan=2,pady=10)
      Button(self.root, text='退出'.center(44,' '), command=self.root.quit).grid(row=5,column=3,columnspan=2,pady=10)
  def Notice(self):
    showinfo('提示','请务必保证图片格式，整片半开对开全开标注清晰！')
 
  def pic_read(self):
    filepath=filedialog.askdirectory(initialdir='./打过的图',title='请选择文件夹')
    for filename in os.listdir(filepath):
        if filename.endswith('jpg'):
            x=picture_read.CurtainI(filepath+'/'+filename)
            x.cut()
    for filename2 in os.listdir('./切割'):
        y=picture_read.CurtainI('./切割'+'/'+filename2)
        y.drawframe()
    for filename2 in os.listdir('./画框'):
        y=picture_read.CurtainI('./画框'+'/'+filename2)
        y.rotate()
    showinfo('提示','切图任务完成！')
  def pic_print(self):
    filepath=filedialog.askdirectory(initialdir='./排版',title='请选择文件夹')
    picture_print.picture_print(filepath)
  def pic_read_and_print(self):
    filepath=filedialog.askdirectory(initialdir='./打过的图',title='请选择文件夹')
    for filename in os.listdir(filepath):
      if filename.endswith('jpg'):
        x=picture_read.CurtainI(filepath+'/'+filename)
        x.cut()
    for filename2 in os.listdir('./切割'):
        y=picture_read.CurtainI('./切割'+'/'+filename2)
        y.drawframe()
    for filename2 in os.listdir('./画框'):
        y=picture_read.CurtainI('./画框'+'/'+filename2)
        y.rotate()
    showinfo('提示','切图任务完成！')
    picture_print.picture_print('./旋转')
    showinfo('提示','RIP任务完成！')
      
      
def main():
  root=Tk()
  root.iconbitmap('裁缝LOGO.ico')
  Mainpage(root)
  root.mainloop()
  root.destroy()
if __name__=='__main__':
  main()
