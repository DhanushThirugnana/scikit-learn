README:

Find the attached sample file 'user.data' for input.

Please find the code written under:
sklearn->mycode->mycode.py
 
Function to be called:
cmeans(<pd.Dataframe>, int,int)

Output:
Centroids<list>, Clusters<list>

Usage:
set path to sklearn and then

import mycode
data = pd.read_csv('user.data,delimiter=',')
centroid1, cluster1 = mycode.MyCMeans().cmeans(data,3,5)
