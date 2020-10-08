import matplotlib.pyplot as plt
import random
import math
def main():
    
    m1=input("Enter the service rate of type I passenger: ")
    l1=input("Enter the arrival rate of type I passenger: ")
    m2=input("Enter the service rate of type II passenger: ")
    l2=input("Enter the arrival rate of type II passenger: ")
    tau1=input("Enter tolerance level of a customer of type I(in mins.): ")
    tau2=input("Enter tolerance level of a customer of type II(in mins.): ")    
    C=[]
    prop=l1/(l1+l2)
    AW=[]
    for j in range(365):
        T1=[]
        T2=[]
        WQ1=[]
        WQ2=[]
        S1=[]
        S2=[]  
        ct1=0
        ct2=0
        sum=0
        for i in range(5000):
            r1=random.random()
            r2=random.random()
            r=random.random()
            if(r<prop):
                t=(-1.0/l1)*math.log(1-r1)
                s=(-1.0/m1)*math.log(1-r2)
                if(len(T1)==0):    
                    T1.append(t)
                    WQ1.append(0)
                    S1.append(s+t)
                else:
                    T1.append(T1[len(T1)-1]+t)
                    WQ1.append(S1[i-1]-min(T1[i],S1[i-1]))
                    S1.append(max(T1[i],S1[i-1]+s))
                if(WQ1[i]>tau1):
                    ct1=ct1+1
                sum=sum+WQ1[i]
            else:
                t=(-1.0/l2)*math.log(1-r1)
                s=(-1.0/m2)*math.log(1-r2)
                if(len(T2)==0):    
                    T2.append(t)
                    WQ2.append(0)
                    S2.append(s+t)
                else:
                    T2.append(T2[len(T2)-1]+t)
                    WQ2.append(S2[i-1]-min(T2[i],S2[i-1]))
                    S2.append(max(T2[i],S2[i-1]+s))
                if(WQ2[i]>tau2):
                    ct2=ct2+1
                sum=sum+WQ2[i]
        AW.append(sum/5000.0)
        C.append((ct1+ct2)/5000.0)
    saw=0
    sc=0
    for i in range(365):
        saw=saw+AW[i]
        sc=sc+C[i]
    print "the average waiting time with two queue over a year ", (saw/365.0)
    print "the probability that average waiting time in the two queues exceeds tolerance level of the customer is ", (sc/365.0) 
    plt.plot(AW)
    plt.xlabel("Days")
    plt.ylabel("Average waiting times")
    plt.title("Average waiting time per day over a year")
    plt.savefig("AVG_3.pdf")
    plt.clf()
    plt.plot(C)
    plt.xlabel("days")
    plt.ylabel("probability") 
    plt.title("Probabilitty of average waiting time exceeding tolerance level of customer")
    plt.savefig("prob_3.pdf")

                
    
main()