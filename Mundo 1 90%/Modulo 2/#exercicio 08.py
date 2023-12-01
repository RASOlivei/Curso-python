#Conversor

m = float(input('\nQual metragem deseja converter (metros): '))

dm = m * 10
c = m * 100
ml = m * 1000 
#=================
dam = m / 10
hm  = m / 100
km  = m / 1000

print('\nO valor de {:.2f}m\n{:.2f} dm\n{:.2f} cm\n{:.2f} mm'.format(m, dm, c, ml))
print('\nO valor de {:.2f}m\n{:.3f} dam\n{:.3f} hm\n{:.3f} km'.format(m, dam, hm, km))