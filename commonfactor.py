def CommonFactor(a,b):
    fact1=[]
    Commonfact=[]


    for i in range(1,10):
        if a%i==0:
            fact1.append(i)

    for j in range(1,10):
        if b%j==0:
            fact1.append(j)
    size=len(fact1)
    for i in range(size):
        k=i+1
        for j in range(k,size):
            if fact1[i]==fact1[j] and fact1[i] not in Commonfact:
                Commonfact.append(fact1[i])
                number_of_elements=len(Commonfact)
    return number_of_elements
a=0
b=1
print(CommonFactor(a,b))
