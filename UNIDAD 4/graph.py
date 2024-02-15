import os

lista = [[10,20,30,40,50,60,70],[1,2,3,4,5,6,7],[11,22,33,44,55,66,77]]
Archi = open("Matriz.dot","w")
Archi.write('digraph G {')
Archi.write('layout=dot\nlabelloc = "t"')
Archi.write('edge [weight=1000 style=dashed color=dimgrey]\n')
for i in lista:
    Archi.write("rank=same {")
    for j in i:
        Archi.write("X{}->".format(j))
    Archi.write('"FIN{}"\n'.format(i[1]))
    Archi.write('}')
Archi.write('}')
Archi.close()
os.system('dot -Tpng Matriz.dot -o MatrizG.png')