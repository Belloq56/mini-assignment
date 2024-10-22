from matplotlib import pyplot as pp

x = []
y = []
count = 0
f = open('fismflux20020824.dat','r')
for line in f:
    if count == 0:
        count+=1
    else:
        irrad = line.split()
        y.append(float(irrad[63])) 
        x.append(count-1)
        count+=1

f.close()

pp.plot(x,y)
pp.xlabel('Index')
pp.ylabel('EUV (W/m^2/nm')
