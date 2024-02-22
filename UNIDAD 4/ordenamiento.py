desorden=[5,6,8,1,2,10]
print(desorden)
n = len(desorden)
for i in range(n-1):
    for j in range(0, n-i-1):
        if desorden[j] > desorden[j+1]:
            temporal=desorden[j]
            desorden[j]=desorden[j+1]
            desorden[j+1]=temporal
            #para no usar el temporal
            #desorden[j], desorden[j+1] = desorden[j+1], desorden[j]
print(desorden)