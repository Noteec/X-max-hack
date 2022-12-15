import numpy as np

def getActValues(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        lines.pop(0)
    values = []
    for line in lines:
        values.append(float(line.split(';')[4]))
    return values

def ActLoose(pp, q, t):
    actValues = getActValues(pp)
    pva = actValues[len(actValues) - 1]
    de = DailyChanges(actValues)
    ep = np.average(de)
    gp = StandartOtklon(actValues) ** 0.5
    return pva * (ep * t - q * gp * (t ** 0.5))

def StandartOtklon(actValues):
    aav = np.average(actValues)
    sum = 0
    for a in actValues:
        sum += a - aav
    return sum/(len(actValues) - 1)

def DailyChanges(actValues):
    changes = []
    for i in range(len(actValues)-1):
        changes.append((actValues[i+1] - actValues[i])/actValues[i] * 100)
    return changes


#example
ppp = ['C:\\Users\\12345\\Downloads\\AFLT_220101_221214.txt', 'C:\\Users\\12345\\Downloads\\VTBR_220101_221214.txt']
q = 2.769
t = 5
for pp in ppp:    
    print(ActLoose(pp, q, t))