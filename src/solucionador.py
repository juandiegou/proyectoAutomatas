import itertools

class solucionador:


    def __init__(self):
        self.estadoI=None
        self.estadoF=None
        self.resultado=None

    def solucionar(self,estadoI,estadoF):
        w,t=[],[]
        k={}
        z=''.join(str(e) for e in estadoI)
        k[z]={}
        for i in range(len(estadoI)):
            
            estadoI[i]=1
            for j in range(len(estadoI)):
                estadoI[j]=1
                temp=estadoI.copy()
                w.append(temp)
                v=self.combinar(temp,len(temp))
                #print(temp,":",v)
                m=''.join(str(e) for e in temp)
                k[z][m]=1
                k=self.crearDic(temp,v,k)
                t.append(v)
                estadoI[j]=0
            estadoI[i]=0
        return k
        
    def combinar(self,lista,r):
        l=itertools.combinations_with_replacement(lista,r)
        l=set(l)
        m=[]
        for e in l:
           m.append(list(e)) 
        return m
    
    def crearDic(self,t,l,d):
        temp=l.copy()
        v=''.join(str(e) for e in t)
        d[v]={}
        for x  in temp:
            z=''.join(str(e) for e in x)
            d[v][z]=1

        return d



    def unir(self,estadoI,I,l):
        a={ }
        temp=l.copy()
        v=''.join(str(e) for e in estadoI)
        a[v]={}
        for x in I:
            z=''.join(str(e) for e in x)
            a[v][z]=1
        #print(a)
        
        for m in a[v].keys():
            a[m]={}
            for w in l:
                z=''.join(str(e) for e in x)
                a[m][z]=1
        print (a)    

#estadoI=[0,0,0,0]
#estadoF=[1,1,1,1]

#s=solucionador()

#d=s.solucionar(estadoI,estadoF)
#print(d)
