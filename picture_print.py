#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os,re,send2trash
from PIL import Image
##from picture_read import *
##import threading
##global printThreads
##printThreads=[]
class ImageSeries():
    def __init__(self,length):
        self.length=length
        self.size=(4253,length)
        Image_series=[]
        x,y=(length//28347,length%28347)
        for i in range(x):
            Image_series+=[Image.new('CMYK',(4253,28347),(0,0,0,0))]
##            Image_series[-1].save('print'+str(i)+'.jpg')
        Image_series+=[Image.new('CMYK',(4253,length%28347),(0,0,0,0))]
##        Image_series[-1].save('print'+str(x)+'.jpg')
        self.Image_series=Image_series
    def save(self):
        for i in range(len(self.Image_series)):
            self.Image_series[i].save('print'+str(i)+'.jpg')
    def spacelen(self,x):
        x1,x2=(x//28347,x%28347)
        m2,n2=self.size
        spacelist=[]
        aImage=self.Image_series[x1]
        for m in range(m2):
            if similar(aImage.getpixel((m,x2)))==(0,0,0,0):
                spacelist+=[1]
            else:
                spacelist+=[-1]
        i=0
        try:
            while 1:
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
    def paste(self,xImage,coordinate):
        m0,n0=xImage.size
        x0,y0=coordinate
        if y0//28347==(y0+n0)//28347:
            i0,j0=(y0//28347,y0%28347)
            self.Image_series[i0].paste(xImage,(x0,j0))
##            self.Image_series[i0].save('print'+str(i0)+'.jpg')
        else:
            i0,j0=(y0//28347,y0%28347)
            i1,j1=((y0+n0)//28347,(y0+n0)%28347)
            xImage_0=xImage.crop((0,0,m0,28347-j0))
            xImage_1=xImage.crop((0,28347-j0,m0,n0))
            self.Image_series[i0].paste(xImage_0,(x0,j0))
##            self.Image_series[i0].save('print'+str(i0)+'.jpg')
            self.Image_series[i1].paste(xImage_1,(x0,0))
##            self.Image_series[i1].save('print'+str(i1)+'.jpg')
def list_coordinate(x):
    i3,j3=(x//28347,x%28347)
    return (i3,j3)
            
def similar(x):
     if x[0]*x[0]+x[1]*x[1]+x[2]*x[2]+x[3]*x[3]<40000:
        x=(0,0,0,0)
     else:
          x=(255,255,255,255)
     return x
        
def picture_print(filepath):
    if not os.path.exists('./print'):
        os.makedirs('./print')
    picturename_list=[]
    for filename in os.listdir(filepath):
        if filename.endswith('.jpg'):
            picturename_list+=[filename]
    picture_list=[]
    size_list=[]
    picture_list=[Image.open(filepath+'/'+picturename) for picturename in picturename_list]
    size_list=[Image.open(filepath+'/'+picturename).size for picturename in picturename_list]
    size_dic={}
    size_big_dic={}
    size_small_dic={}
    length_0=0
    for i in range(len(size_list)):
        size_dic.setdefault(i,size_list[i])
        if size_list[i][0]>4259 or size_list[i][1]>4259:
            length_0+=max(size_list[i][0],size_list[i][1])
            size_big_dic.setdefault(i,size_list[i])
        else:
            length_0+=min(size_list[i][0],size_list[i][1])
            size_small_dic.setdefault(i,size_list[i])
    iMage_0=ImageSeries(length_0)
    a=iMage_0.Image_series
    i=0
    j=0
    length_1=[0]
    coordinate_dic={}
    size_dic_copy=size_dic.copy()
    size_choosen=[]
    while length_1[i]<length_0:
        if set(size_dic_copy.values())=={(0,0)}:
            break
        spacelisti=iMage_0.spacelen(length_1[i])
        if spacelisti[j]>0:
            choice=choose(spacelisti[j],size_dic_copy)
            try:
                cx,cy=size_dic_copy[choice]
                if max(cx,cy)<=spacelisti[j]:
                    b1=Image.new('CMYK',(max(cx,cy),min(cx,cy)),(255,255,255,255))
                    if max(cx,cy)==cx:
                        coordinate=((listfor(j,spacelisti),length_1[i]),0)
                    else:
                        coordinate=((listfor(j,spacelisti),length_1[i]),90)
                    coordinate_dic.setdefault(choice,coordinate)
                    size_dic_copy[choice]=(0,0)
                    iMage_0.paste(b1,coordinate[0])
                    j=0
                    length_1+=[length_1[i]+min(cx,cy)]
                    length_1=sorted(length_1)
                else:
                    b1=Image.new('CMYK',(min(cx,cy),max(cx,cy)),(255,255,255,255))
                    if max(cx,cy)==cy:
                        coordinate=((listfor(j,spacelisti),length_1[i]),0)
                    else:
                        coordinate=((listfor(j,spacelisti),length_1[i]),90)
                    coordinate_dic.setdefault(choice,coordinate)
                    size_dic_copy[choice]=(0,0)
                    iMage_0.paste(b1,coordinate[0])
                    j=0
                    length_1+=[length_1[i]+max(cx,cy)]
                    length_1=sorted(length_1)
            except:
                if j==len(spacelisti)-1:
                    i=i+1
                    j=0
                    continue
                else:
                    j=j+1
                    continue
                    
                     
        else:
            if j==len(spacelisti)-1:
                if i==len(length_1)-1:
                        break
                i=i+1
                j=0
                continue
            else:
                j=j+1
    for i in range(len(size_list)):
        iMage_0.paste(picture_list[i].rotate(coordinate_dic[i][1],expand=True),coordinate_dic[i][0])
    for i in iMage_0.Image_series:
        i.save('print'+str(iMage_0.Image_series.index(i))+'.jpg')
    x3,y3=list_coordinate(length_1[-1])
    a[x3]=a[x3].crop((0,0,4253,y3))
    a[x3].save('print'+str(x3)+'.jpg')
    try:
        for w in range(x3+1,len(a)):
            send2trash.send2trash('print'+str(w)+'.jpg')
    except:
        pass
def size_rate():
    pass
    
                
def choose(x,sizedic):
    sizesuit={}
    for m in sizedic.keys():
        if sizedic[m][0]<=x or sizedic[m][1]<=x and sizedic[m][0]*sizedic[m][1]!=0:
            sizesuit.setdefault(m,sizedic[m])
    if not sizesuit:
        return None
    return maxsize(sizesuit)
        
        
def maxsize(sizesuit):
    max_0=0
    max_key=None
    for n in sizesuit.keys():
        if sizesuit[n][0]*sizesuit[n][1]>max_0:
            max_key=n
            max_0=sizesuit[n][0]*sizesuit[n][1]
    return max_key
    
def listfor(j,li):
    list_add=0
    for i2 in range(j):
        list_add+=abs(li[i2])
    return list_add
            
            
    
        
            
def main():
    picture_print('./write')

if __name__=='__main__':
    main()
        
        
