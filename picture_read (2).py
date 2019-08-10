#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,re
from PIL import Image,ImageDraw,ImageFont
from PIL import JpegImagePlugin
class CurtainI():
    def __init__(self,path):
        if os.path.exists(path):
            self.path=path
        else:
            self.path=None
        try:
            self.name=os.path.basename(self.path)
        except:
            print('图案不存在非法图案路径')
            self.name=None
        self.simplename=self.simple()
        self.image=self.C_Image()
    def C_Image(self):
        try:
            aImage=Image.open(self.path)
            
        except:
            print('图案不存在非法图案路径')
        return aImage
    def simple(self):
        try:
            a=re.findall('(.*)宽\d{2,3}.\d{2,3}',self.name)
            b=re.findall('(.*)\d{2,3}X\d{2,3}',self.name)
            if a:
                return a[0]
            else:
                if b:
                    return b[0]
                else:
                    return '非标准门帘图案名称'
        except:
            print('图案不存在非法图案路径')
    def save(self,newpath):
        try:
            aImage=Image.open(self.path)
            
        except:
            print('图案不存在非法图案路径')
    def pixelsize(self):
        try:
            aImage=Image.open(self.path)
            return aImage.size
        except:
            print('图案不存在非法图案路径')
            
    def resize(self,width,hight):
        try:
            aImage=Image.open(self.path)
            w,h=aImage.size
            bImage=aImage.resize((int(72/2.54*width/w),int(72/2.54*hight/h)))
            bImage.save(self.name+'.jpg')
        except:
            print('图案不存在非法图案路径')
    def drawframe(self):
        if not os.path.exists('./画框'):
                os.makedirs('./画框')
        try:
            aImage=Image.open(self.path)
            m,n=aImage.size
            if '纸巾袋' in self.name or '抽纸袋' in self.name or '纸巾盒' in self.name or '挂画' in self.name:
                m1,n1=(int(m+5/2.54*72)+1,int(n+5/2.54*72)+1)
                b=Image.new('CMYK',(m1,n1),(0,0,0,100))
                b1=Image.new('CMYK',(m1-2,n1-2),(0,0,0,0))
                b2=Image.new('CMYK',(m+2,n+2),(127,127,127,255))
                b.paste(b1,(1,1))
                b.paste(b2,(71,71))
                b.paste(aImage,(72,72))
                b.save('./画框/'+self.name)
            else:
                m1,n1=(int(m+5/2.54*72)+1,int(n+8.5/2.54*72)+1)
                b=Image.new('CMYK',(m1,n1),(0,0,0,0))
                b1=Image.new('CMYK',(m1,n1-100),(127,127,127,255))##71,212，142是与分辨率有关的常数
                b2=Image.new('CMYK',(m1-2,n1-102),(0,0,0,0))
                b3=Image.new('CMYK',(m+2,n+2),(127,127,127,255))
##                b0=Image.open('E:/小程序/排版/裁缝LOGO.jpg')
                b.paste(b1,(0,100))
                b.paste(b2,(1,101))
                b.paste(b3,(71,170))
                b.paste(aImage,(72,171))
                y=int(n/5+6/2.54*72)
                y2=int(n/10+6/2.54*72)
                for x in range(20):
                    b.putpixel((x,y),(0,255,249,25))
                    b.putpixel((x,y2),(0,255,249,25))
                for x in range(m1-20,m1):
                    b.putpixel((x,y),(0,255,249,25))
                    b.putpixel((x,y2),(0,255,249,25))
                for x in range(72,m1-72):
                    b.putpixel((x,100),(0,0,0,0))
                for x in range(m1):
                    b.putpixel((x,0),(51,0,0,0))
                    b.putpixel((x,29),(0,0,0,100))
                    
##                if '左'in self.name:
##                    b.paste(b0,(36,108))
##                elif '右' in self.name:
##                    b.paste(b0,(m1-72,108))
##                else:
##                    b.paste(b0,(36,108))
##                    b.paste(b0,(m1-72,108))
                b.save('./画框/'+self.name)
        except:
            print('图案不存在非法图案路径')
    def cut(self):                            #裁图 俩开 三开
        try:
            aImage=Image.open(self.path)
            if not os.path.exists('./切割'):
                os.makedirs('./切割')
            m,n=aImage.size
            if '一体'in self.name or '整片' in self.name:
                aImage.save('./切割/'+self.name)
            elif '半开'in self.name or '全开' in self.name or '对开' in self.name:
                croppeda=aImage.crop((0,0,int(m/2)+2,n))
                croppeda.save('./切割/'+self.name[:-4]+'左.jpg')
                croppedb=aImage.crop((int(m/2)+1,0,m,n))
                croppedb.save('./切割/'+self.name[:-4]+'右.jpg')
            elif '三开' in self.name:
                cropped1=aImage.crop((0,0,int(m/3)+1,n))
                cropped1.save('./切割/'+self.name[:-4]+'左.jpg')
                cropped2=aImage.crop((int(m/3)+1,0,int(m*2/3)+1,n))
                cropped2.save('./切割/'+self.name[:-4]+'中.jpg')
                cropped3=aImage.crop((int(m*2/3)+1,0,m,n))
                cropped3.save('./切割/'+self.name[:-4]+'右.jpg')
            else:
                print('目前仅支持三开')
        except:
            print('图案不存在非法图案路径')
    def rotate(self,angle=90):
        if not os.path.exists('./旋转'):
                os.makedirs('./旋转')
        try:
            aImage=Image.open(self.path)
            if aImage.size[1]>151*72/2.54:
                angle=0
            bImage=aImage.rotate(angle,expand=True)
            bImage.save('./旋转/'+self.name[:-4]+'_'+str(angle)+'.jpg')
        except:
            print('图案不存在非法图案路径')
    def write(self):
        if not os.path.exists('./标注'):
                os.makedirs('./标注')
        try:
            aImage=Image.open(self.path)
            font = ImageFont.truetype('simsun.ttc',12)
            draw = ImageDraw.Draw(aImage)
            draw.text( (0,0), self.name,(0,0,0),font=font)
            aImage.save('./标注/'+self.name)
        except:
            print('图案不存在非法图案路径')
        
        
    def spacelen(self,x):
         m2,n2=self.pixelsize()
         spacelist=[]
         aImage=self.C_Image()
         for m in range(m2):
              if similar(aImage.getpixel((m,x)))==(0,0,0,0):
                   spacelist+=[1]
              else:
                   spacelist+=[-1]
         i=0
         try:
              while 1:
##          print(spacelist)
                   if spacelist[i]*spacelist[i+1]>0:
                        spacelist[i+1]+=spacelist[i]
                        del spacelist[i]
                        i=0
                   i+=1
         except:
              try:
                   if spacelist[0]*spacelist[1]>0:
                        spacelist[1]+=spacelist[0]
                        del spacelist[0]
                   return spacelist
              except:
                   return spacelist
    
        
def similar(x):
     if x[0]*x[0]+x[1]*x[1]+x[2]*x[2]+x[3]*x[3]<40000:
        x=(0,0,0,0)
     else:
          x=(255,255,255,255)
     return x
    
        
def main():
    workdir=input('请输入图片文件夹地址')
    for filename in os.listdir(workdir):
        if filename.endswith('jpg'):
            x=CurtainI(workdir+'/'+filename)
            x.cut()
    for filename2 in os.listdir('./切割'):
        y=CurtainI('./切割'+'/'+filename2)
        y.drawframe()
    for filename2 in os.listdir('./画框'):
        y=CurtainI('./画框'+'/'+filename2)
        y.rotate()
    for filename2 in os.listdir('./旋转'):
        y=CurtainI('./旋转'+'/'+filename2)
        y.write()

if __name__=='__main__':
    main()
    #9.1布料伸缩常数148.5/151.5,98.5/100
        
        
