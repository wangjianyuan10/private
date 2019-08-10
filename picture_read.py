#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os,re,datetime
from PIL import Image,ImageDraw,ImageFont,JpegImagePlugin
class CurtainI(JpegImagePlugin.JpegImageFile):
    @property
    def name(self):
        _,x=os.path.split(self.filename)
        return x
    @property
    def sizename(self):
        _,self.name=os.path.split(self.filename)
        try:
            a=re.findall('(宽\d{2,3}高\d{2,3})',self.name)
            b=re.findall('(\d{2,3}x\d{2,3})',self.name)
            if a:
                return a[0]
            else:
                if b:
                    return b[0]
                else:
                    return '非标准门帘图案名称'
        except:
            print('图案不存在非法图案路径')
    def drawframe(self):
        if not os.path.exists('./frame'):
                os.makedirs('./frame')
        try:
            m,n=self.size
            if '纸巾袋' in self.name or '抽纸袋' in self.name or '纸巾盒' in self.name or '挂画' in self.name:
                m1,n1=(int(m+5/2.54*72)+1,int(n+5/2.54*72)+1)
                b=Image.new('CMYK',(m1,n1),(0,0,0,100))
                b1=Image.new('CMYK',(m1-2,n1-2),(0,0,0,0))
                b2=Image.new('CMYK',(m+2,n+2),(0,0,0,100))
                b.paste(b1,(1,1))
                b.paste(b2,(71,71))
                b.paste(self,(72,72))
                y=int(n/3+2.5/2.54*72)
                y2=int(n/3*2+2.5/2.54*72)
                for x in range(10):
                    b.putpixel((x,y),(0,255,249,25))
                    b.putpixel((x,y2),(0,255,249,25))
                for x in range(m1-10,m1):
                    b.putpixel((x,y),(0,255,249,25))
                    b.putpixel((x,y2),(0,255,249,25))
                x0=int(m1/2-1.5/2.54*72)
                x1=int(m1/2+1.5/2.54*72)
                for y in range(24,48):
                    b.putpixel((x0,y),(0,255,249,25))
                    b.putpixel((x1,y),(0,255,249,25))
                for y in range(n1-48,n1-24):
                    b.putpixel((x0,y),(0,255,249,25))
                    b.putpixel((x1,y),(0,255,249,25))
                b.save('./frame/'+self.name)
            elif '魔术贴' in self.name:
                m1,n1=(int(m+6/2.54*72)+1,int(n+6/2.54*72)+1)
                b=Image.new('CMYK',(m1,n1),(0,0,0,100))
                b1=Image.new('CMYK',(m1-2,n1-2),(0,0,0,0))
                b2=Image.new('CMYK',(m+2,n+2),(0,0,0,100))
                b.paste(b1,(1,1))
                b.paste(b2,(85,85))
                b.paste(self,(86,86))
                y=int(n/5+3/2.54*72)
                y2=int(n/10+3/2.54*72)
                for x in range(10):
                    b.putpixel((x,y),(0,255,249,25))
                    b.putpixel((x,y2),(0,255,249,25))
                for x in range(m1-10,m1):
                    b.putpixel((x,y),(0,255,249,25))
                    b.putpixel((x,y2),(0,255,249,25))
                b.save('./frame/'+self.name)
                
                
            else:
                m1,n1=(int(m+5/2.54*72)+1,int(n+8.5/2.54*72)+1)
                b=Image.new('CMYK',(m1,n1),(0,0,0,0))
                b1=Image.new('CMYK',(m1,n1-100),(127,127,127,255))##71,212，142是与分辨率有关的常数
                b2=Image.new('CMYK',(m1-2,n1-102),(0,0,0,0))
                b3=Image.new('CMYK',(m+2,n+2),(0,0,0,100))
                b.paste(b1,(0,100))
                b.paste(b2,(1,101))
                b.paste(b3,(71,170))
                b.paste(self,(72,171))
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
                    b.putpixel((x,0),(0,0,0,100))
                    b.putpixel((x,29),(51,0,0,0))
                    
                b.save('./frame/'+self.name)
        except:
            print('图案不存在非法图案路径')
    def cut(self):                            #裁图 俩开 三开
        try:
            if not os.path.exists('./cut'):
                os.makedirs('./cut')
            m,n=self.size
            if '一体'in self.name or '整片' in self.name:
                self.save('./cut/'+self.name)
            elif '半开'in self.name or '全开' in self.name or '对开' in self.name:
                croppeda=self.crop((0,0,int(m/2)+2,n))
                croppeda.save('./cut/'+self.name[:-4]+'左.jpg')
                croppedb=self.crop((int(m/2)+1,0,m,n))
                croppedb.save('./cut/'+self.name[:-4]+'右.jpg')
            elif '三开' in self.name:
                cropped1=self.crop((0,0,int(m/3)+2,n))
                cropped1.save('./cut/'+self.name[:-4]+'左.jpg')
                cropped2=self.crop((int(m/3)+2,0,int(m*2/3)+2,n))
                cropped2.save('./cut/2'+self.name[:-4]+'中.jpg')
                cropped3=self.crop((int(m*2/3)+2,0,m,n))
                cropped3.save('./cut/'+self.name[:-4]+'右.jpg')
            else:
                print('目前仅支持三开')
        except:
            print('图案不存在非法图案路径')
    def write(self):
        if not os.path.exists('./write'):
                os.makedirs('./write')
        try:
            font = ImageFont.truetype('simsun.ttc',25)
            draw = ImageDraw.Draw(self)
            draw.text( (0,0),self.sizename,fill='black',font=font)
            self.save('./write/'+self.name)
        except:
            print('图案不存在非法图案路径')
    def _rotate(self,angle=90):
        if not os.path.exists('./rotate'):
                os.makedirs('./rotate')
        try:
            if self.size[1]>151*72/2.54:
                angle=0
            bImage=self.rotate(angle,expand=True)
            bImage.save('./rotate/'+self.name[:-4]+'_'+str(angle)+'.jpg')
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
    
    @staticmethod
    def similar(x):
        if x[0]*x[0]+x[1]*x[1]+x[2]*x[2]+x[3]*x[3]<40000:
            x=(0,0,0,0)
        else:
          x=(255,255,255,255)
        return x

def searchfilepath():
    timenow=datetime.datetime.now()
    y,m,d=(timenow.year,timenow.month,timenow.day)
    if os.path.exists('./%s'%(str(y)+str(m)+str(d))):
        return './%s'%(str(y)+str(m)+str(d))
    elif os.path.exists('./打过的图/%s'%(str(y)+str(m)+str(d))):
        return './打过的图/%s'%(str(y)+str(m)+str(d))
    else:
        return None
##def main():
##    if searchfilepath():
##        workdir=searchfilepath()
##    else:
##        workdir=input('请输入图片文件夹地址')
##    for filename in os.listdir(workdir):
##        if filename.endswith('jpg'):
##            x=CurtainI(workdir+'/'+filename)
##            x.cut()
##    for filename in os.listdir('./cut'):
##        if filename.endswith('jpg'):
##            y=CurtainI('./cut'+'/'+filename)
##            y.drawframe()
##    for filename in os.listdir('./frame'):
##        if filename.endswith('jpg'):
##            y=CurtainI('./frame'+'/'+filename)
##            y._rotate()
##    for filename in os.listdir('./rotate'):
##        if filename.endswith('jpg'):
##            y=CurtainI('./rotate'+'/'+filename)
##            y.write()
##
##if __name__=='__main__':
##    main()
##    #9.1布料伸缩常数148.5/151.5,98.5/100
