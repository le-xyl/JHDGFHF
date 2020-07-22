from K_means import k_means
import numpy as np
data=np.array([[1,1],[1,2],[2,1],[4,5],[5,5],[5,4],[2,2],[4,4],[1.5,1.5],[4.5,4.5],[3,3]])
mykmean=k_means(data,2)
mycenter=mykmean .init_center()
print('mycenter=')
print(mycenter)
mydist=mykmean .get_distance()
print('mydistance=')
print(mydist )
myclu=mykmean .get_cluster()
print('myclu=')
print(myclu)
newcenter=mykmean .get_center()
print('newcenter=')
print(newcenter)

