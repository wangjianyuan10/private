Global No
No=0
class pic(object):
    def __init__(self,width,lenth,position=(0,0),angle=0,positionlist={}):
        if width<=lenth:
            No+=1
            self.No=No
            self.width=width
            self.lenth=lenth
            self.position=position
            self.angle=angle
            self.positionlist.setdefault(self.No,(self.width,self.lenth,0,0,0))
        else:
            No+=1
            self.No=No
            self.width=lenth
            self.lenth=width
            self.position=position
            self.angle=angle+90
            self.positionlist.setdefault(self.No,(self.width,self.lenth,0,0,0))
    @property
    def size(self):
        return self.width*self.lenth
    def __add__(self,other):  #最大利用率相加
        horizontaladd=pic(self.width+other.width,max(self.lenth,other.lenth))
        verticaladd=pic(self.lenth+other.lenth,max(self.width,other.width))
        if horizontaladd.size<=verticaladd.size:
            return horizontaladd
        else:
            return verticaladd
    def __repr__(self):
        return 'pic(width=%sxlenth=%s,position=%s,angle=%s,positionlist=%s)'%(self.width,self.lenth,self.position,self.angle,self.positionlist)
    def add(self,other1,other2): ##最大利用率相加
        add1=self+other1+other2
        add2=other1+other2+self
        add3=other2+self+other1
        if add1.size==min(add1.size,add2.size,add3.size):
            return add1
        elif add2.size==min(add1.size,add2.size,add3.size):
            return add2
        else:
            return add3
    def filladd(self,other,w):
        filladdlist=sorted([self.width,self.lenth,other.width,other.lenth])
        if self.width,self.lenth==(filladdlist[0],filladdlist[1]):
            add1=pic(self.width+other.width,other.lenth)
            addlist=
            
            
    def filladd3(self,other1,other2,w):
        add1=self.filladd(other1,w).filladd(other2,w)
        add2=other1.filladd(other2,w).filladd(self,w)
        add3=self.filladd(other2,w).filladd(other1,w)
        addlist=sorted([add1,add2,add3],key=lambda x:x.lenth)
        for i in addlist:
            if i.width>w:
                del i
        print(addlist)
        try:
            return addlist[0]
        except:
            return None

                
            
            
        
    
        
    
