from sklearn import tree
from pandas import *
data = read_table('/home/liuwensui/Documents/data/credit_count.txt', sep = ',')
Y = data[data.CARDHLDR == 1].BAD
X = data[data.CARDHLDR == 1][['AGE', 'ADEPCNT', 'MAJORDRG', 'MINORDRG', 'INCOME', 'OWNRENT']]
clf = tree.DecisionTreeClassifier(min_samples_leaf = 500)
clf = clf.fit(X, Y)
from StringIO import StringIO
out = StringIO()
out = tree.export_graphviz(clf, out_file = out)
# OUTPUT DOT LANGUAGE SCRIPTS
print out.getvalue()
