l1=[1,7,10,11]
l2=[2,4,6,8]
print("listas 1: " ,l1)
print("listas 2: " ,l2)
union= l1 +l2
aux=None
print("listas unidas: " ,union)
tamaño=len(union) -1
for i in range(tamaño):
    for j in range( tamaño -i) :
     if union[j] > union[j+1]:
      aux=union[j]
      union[j] = union[j+1]
      union[j+1] = aux
print("Lista ordenada: " , union)

