import nltk
from nltk.corpus import wordnet as wn
import itertools as it
import numpy
sen=input("give the string")
ws=sen.split()

synlists=[]

for w in ws:
    synlist=wn.synsets(w)
    synlists.append(synlist)

print(synlists)
#comb=[list(x) for x in numpy.array(numpy.meshgrid(*synlists)).T.reshape(-1,len(synlists))]

comb=list(it.product(*synlists))
print(comb)
sim=[]
for i in comb:
    l=[]
    for t in i:
        l.append(t)
    sim.append(l)
print(sim)
sim_fin=[]
for i in sim:
    nl=[]
    test=list(it.combinations(i, 2))
    p=1
    for t in test:
        s=t[0].wup_similarity(t[1])
        print("s:",s)
        if s==None:
            s=0.001
        p=p*s
    print("p:",p)
    for n in i:
        nl.append(n)
    nl.append(p)
    sim_fin.append(nl)
max_sim=sim_fin[0]
for i in sim_fin:
    if max_sim[3]<i[3]:
        max_sim=i
print("this is the max sim: ",max_sim)

