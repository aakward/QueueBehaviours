import matplotlib.pyplot as plt
import random
import math
def main():
    
    m1=input("Enter the service rate of type I passenger: ")
    l1=input("Enter the arrival rate of type I passenger: ")
    m2=input("Enter the service rate of type II passenger: ")
    l2=input("Enter the arrival rate of type II passenger: ")
    tau=input("Enter tolerance level of a customer(in sec.): ")
    C=[]
    prop=l1/(l1+l2)
    AW=[]
    for j in range(365):
        T=[]
        WQ=[]
        ST=[]
        TYPE=[]
        S1=[]
        S2=[]  
        ct=0
        sum=0
        for i in range(5000):
            r1=random.random()
            r2=random.random()
            r=random.random()
            t=(-1.0/(l1+l2))*math.log(1-r1)      
            if(r<prop):
                TYPE.append(0)
                s=(-1.0/m1)*math.log(1-r2)
                ST.append(s)
                if(len(T)==0):    
                    T.append(t)
                else:
                    T.append(T[len(T)-1]+t)
            else:
                TYPE.append(1)
                s=(-1.0/m2)*math.log(1-r2)
                ST.append(s)
                if(len(T)==0):    
                    T.append(t)
                else:
                    T.append(T[len(T)-1]+t)
            if(len(T)==1):
                WQ.append(0)
                S1.append(s+t)
            elif(len(T)==2):
                WQ.append(0)
                S2.append(s+T[1])
            else:
                WQ.append(max(0,(min(S1[len(S1)-1],S2[len(S2)-1])-T[i])))
                if S1[len(S1)-1]<S2[len(S2)-1]:
                    S1.append(S1[len(S1)-1]+s)
                else:
                    S2.append(S2[len(S2)-1]+s)
            if(WQ[i]>tau):
                ct=ct+1
            sum=sum+WQ[i]
        AW.append(sum/5000.0)
        C.append(ct/5000.0)
    saw=0
    sc=0
    for i in range(365):
        saw=saw+AW[i]
        sc=sc+C[i]
    print "the average waiting time in the queue over a year ", (saw/365.0)
    print "the probability that average waiting time in the queue exceeds tolerance level of the customer is ", (sc/365.0) 
    plt.plot(AW)
    plt.xlabel("Days")
    plt.ylabel("Average waiting times")
    plt.title("Average waiting time per day over a year")
    plt.savefig("AVG.pdf")
    plt.clf()
    plt.plot(C)
    plt.xlabel("days")
    plt.ylabel("probability") 
    plt.title("Probabilitty of average waiting time exceeding tolerance level of customer")
    plt.savefig("prob.pdf")

                
    
main()