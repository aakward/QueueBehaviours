import matplotlib.pyplot as plt
import random
import math
def main():
    
    m1=input("Enter the service rate of type I passenger: ")
    l1=input("Enter the arrival rate of type I passenger: ")
    m2=input("Enter the service rate of type II passenger: ")
    l2=input("Enter the arrival rate of type II passenger: ")
    tau1=input("Enter tolerance level of a customer of type I (in mins.): ")
    tau2=input("Enter tolerance level of a customer of type II (in mins.): ")
    C=[]
    prop=l1/(l1+l2)
    AW=[]
    for j in range(365):
        T=[]
        T1=[]
        T2=[]
        WQ1=[]
        WQ2=[]
        S1=[0]
        S2=[0]
        ct=0
        sum=0
        for i in  range(5000):
            r1=random.random()
            r2=random.random()
            r=random.random()
            t=(-1.0/(l1+l2))*math.log(1-r1)
            if(len(T)==0):
                T.append(t)
            else:
                T.append(T[len(T)-1]+t)
            if r<prop:
                s=(-1.0/m1)*math.log(1-r2)
                k=0
                while(k==0):
                    if(S1[0]==0):
                        break;
                    elif(T[i]>=S1[0]):
                        S1=S1[1:]
                    else:
                        k=1
                k=0
                while(k==0):
                    if(S2[0]==0):
                        break;
                    elif(T[i]>=S2[0]):
                        S2=S2[1:]
                    else:
                        k=1
                if(len(S1)<=len(S2)):
                    T1.append(T[i])
                    if(len(S1)==0):
                        WQ1.append(0)
                        S1.append(T1[len(T1)-1]+s)
                    else:
                        WQ1.append(max(0,S1[len(S1)-1]-T1[len(T1)-1]))
                        S1.append(T1[len(T1)-1]+WQ1[len(WQ1)-1]+s)
                    if(WQ1[len(WQ1)-1]>tau1):
                        ct=ct+1
                    sum=sum+WQ1[len(WQ1)-1]
                else:
                    T2.append(T[i])
                    if(len(S2)==0):
                        WQ2.append(0)
                        S2.append(T2[len(T2)-1]+s)
                    else:
                        WQ2.append(max(0,S2[len(S2)-1]-T2[len(T2)-1]))
                        S2.append(T2[len(T2)-1]+WQ2[len(WQ2)-1]+s)
                    if(WQ2[len(WQ2)-1]>tau1):
                        ct=ct+1
                    sum=sum+WQ2[len(WQ2)-1]
            else:
                s=(-1.0/m2)*math.log(1-r2)
                k=0
                while(k==0):
                    if(S1[0]==0):
                        break;
                    elif(T[i]>=S1[0]):
                        S1=S1[1:]
                    else:
                        k=1
                k=0
                while(k==0):
                    if(S2[0]==0):
                        break;
                    elif(T[i]>=S2[0]):
                        S2=S2[1:]
                    else:
                        k=1
                if(len(S1)<=len(S2)):
                    T1.append(T[i])
                    if(len(S1)==0):
                        WQ1.append(0)
                        S1.append(T1[len(T1)-1]+s)
                    else:
                        WQ1.append(max(0,S1[len(S1)-1]-T1[len(T1)-1]))
                        S1.append(T1[len(T1)-1]+WQ1[len(WQ1)-1]+s)
                    if(WQ1[len(WQ1)-1]>tau2):
                        ct=ct+1
                    sum=sum+WQ1[len(WQ1)-1]
                else:
                    T2.append(T[i])
                    if(len(S2)==0):
                        WQ2.append(0)
                        S2.append(T2[len(T2)-1]+s)
                    else:
                        WQ2.append(max(0,S2[len(S2)-1]-T2[len(T2)-1]))
                        S2.append(T2[len(T2)-1]+WQ2[len(WQ2)-1]+s)
                    if(WQ2[len(WQ2)-1]>tau2):
                        ct=ct+1
                    sum=sum+WQ1[len(WQ1)-1]
        AW.append(sum/5000.0)
        C.append(ct/5000.0)  
    saw=0
    sc=0
    for i in range(365):
        saw=saw+AW[i]
        sc=sc+C[i]
    print "the average waiting time with two independent queue over a year ", (saw/365.0)
    print "the probability that average waiting time in the two queues exceeds tolerance level of the customer is ", (sc/365.0) 
    plt.plot(AW)
    plt.xlabel("Days")
    plt.ylabel("Average waiting times")
    plt.title("Average waiting time per day over a year")
    plt.savefig("AVG_2.pdf")
    plt.clf()
    plt.plot(C)
    plt.xlabel("days")
    plt.ylabel("probability") 
    plt.title("Probabilitty of average waiting time exceeding tolerance level of customer")
    plt.savefig("prob_2.pdf")
                    
                
main()
                
                    
                
                
            