ages = [25, 17, 18, 20, 16, 44]
def canvote(x):
    if (x >= 18):
        return True
    else:
        return False
voters = filter(canvote, ages)
voterlist = []
for x in voters:
    voterlist.append(x)
print(voterlist)


ages = [25, 17, 18, 20, 16, 44] 
print(list(filter(lambda x: x >= 18, ages)))