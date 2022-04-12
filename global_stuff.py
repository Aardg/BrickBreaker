score=0
pos1=[]
pos2 = []

for i in range(9):
    pos1.append((i+4,2*i+4))
    pos1.append((i+4,45-(2*i+4)))
    pos1.append((45-(i+4),2*i+4))
    pos1.append((45-(i+4),45-(2*i+4)))

for i in range(9):
    pos2.append((2*i+4,2*i+4))
    pos2.append((2*i+4,45-(2*i+4)))
    pos2.append((45-(2*i+4),2*i+4))
    pos2.append((45-(2*i+4),45-(2*i+4)))


for i in range(5):
    pos1.append((25,15+4*i))
    pos2.append((25,15+4*i))

pppos1=pos1
pppos2=pos2

onpaddle=1

level = 1

power_duration = [0]*6

