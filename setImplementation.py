seta={2,3,4,5,6,7,8}
setb={6,7,8,9,10,11,12}
#add
seta.add(9)
setb.add(13)
print(seta)
print(setb)
#union
setc=seta.union(setb)
print(setc)
setd=seta.intersection(setb)
print(setd)
sete=seta.difference(setb)
print(sete)
print(setb.isdisjoint(seta))
setb.discard(13)
print(setb)
seta.difference_update(setb)
print(seta)
print(setb.isdisjoint(seta))
setb.discard(13)
print(setb)

a=set(range(15)) 
print(a)#it prints data from 0 to 14
b=set(range(10))
sd=b.symmetric_difference(a)
print(sd)

dup={2,3,4,5,6,7,4,5,6}
print(set(dup))

empty_dict={}
integerkey_dict={1:"mango",2:"banana"}