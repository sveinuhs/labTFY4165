# Dataanalyse frå labaktivitet 2 - Termisk fytsikk
import matplotlib.pyplot as plt
import numpy as np
import math
def linear_regresjon(x,y): #funksjon for lineær regresjon
    N=0
    for items in x:
        N+=1
        
    Sx=np.sum(x)
    Sy=np.sum(y)
    Sxx=(np.linalg.norm(x))**2
    Sxy=np.dot(x,y)
    Delta=N*Sxx-Sx**2
    
    a0=(Sy*Sxx-Sx*Sxy)/Delta
    a1=(N*Sxy-Sx*Sy)/Delta
    
    ny=a0+a1*x
    Dy=y-ny
    S=(np.linalg.norm(Dy))**2
    Da0=math.sqrt((1/(N-2))*((S*Sxx)/Delta))
    Da1=math.sqrt((N/(N-2))*(S/Delta))
    return(a0,a1,Da0,Da1)
    
#Legg inn alle eksperimentelle data og gjer dei om til arrays
T1=[0,60,120,180,240,300]
T1=np.array(T1)
M1=[59.142,56.963,54.868,52.782,50.761,48.90]
M1=np.array(M1)
T2=[480,540,600,660,720]
T2=np.array(T2)
M2=[44.762,43.128,41.5,39.928,38.396]
M2=np.array(M2)-6.04


#Lagar ein array som kan brukast til lineær regresjon
TR=[0,60,120,180,240,300,360,420,480,540,600,660,720]
TR=np.array(TR)


#Køyrer lineær regresjon på tala
(a0,a1,Da0,Da1) = linear_regresjon(T1,M1)
N1=a0+TR*a1

(b0,b1,Db0,Db1) = linear_regresjon(T2,M2)
N2=b0+TR*b1

#plottar eksperimentelle data og regrerte data i same graf
plt.plot(T1,M1,'ro',label="masse før aluminiumsbit")
plt.plot(TR,N1,'k')
plt.plot(T2,M2,'bs',label="masse etter aluminiumsbit")
plt.plot(TR,N2,'k')
plt.title('Masse til nitrogen som funksjon av tid')
plt.xlabel('tid/s')
plt.ylabel('masse til nitrogen/g')
plt.legend()

plt.show()

#lagar ein funksjon som returnerar deltam
def deltam(A0,A1,B0,B1,T1,T2):
    DT=(T1+T2)/2
    m1=A0+A1*DT
    m2=B0+B1*DT
    print(abs(m1-m2))
deltam(a0,a1,b0,b1,360,4)
