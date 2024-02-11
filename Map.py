print(list(map(lambda *a: a, range(3)))) # wrapping in list and mapping 0,1,2… 
print(list(map(lambda *a: a, range(3),'abc'))) #mapping string to 0,1,2, -> 2 iterables 
print(list(map(lambda *a: a, range(3),'abc',range(4,7)))) # 3 iterables 
print(list(map(lambda *a: a, (), 'abc'))) # empty tuple is shortest 
print(list(map(lambda *a: a, (1, 2), 'abc'))) # (1, 2) shortest 
print(list(map(lambda *a: a, (1, 2, 3, 4), 'abc')))  # 'abc' is shortest

#Next

students = [ 
dict(name='Ram', credits=dict(math=90, physics=64, history=75)), 
dict(name='Harendra', credits=dict(math=66, physics=70, latin=80)), 
dict(name='Rahul', credits=dict(history=80, physics=90, chemistry=70)), 
dict(name="Shyam", credits=dict(math=59, physics=55, geography=70)), 
]
def decorate(student):
    return (sum(student['credits'].values()),student)
students = sorted(map(decorate,students))
print(students)
first_data=list(map(lambda x: x[0],students))
print(first_data)
topper=max(first_data)
print("highest marks=",topper)


#Zip
students = ["Harendra", "Hitesh", "Surendra", "Mahendra", "Narendra"] 
percentage = [78, 86, 75, 67, 87] 
zippedlist = list(zip(students, percentage)) 
# same as 
mappedlist = list(map(lambda *x: x, students, percentage)) 
print("\n zippedlist=",zippedlist, "\n mappedlist=", mappedlist) 