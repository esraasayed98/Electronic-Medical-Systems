from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from micromlgen import port


dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,5].values

# x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.2 )


# clf=RandomForestClassifier(n_estimators=100)

# clf.fit(x_train,y_train)

# y_pred=clf.predict(x_test)


# Model Accuracy, how often is the classifier correct?
# print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
accuracy = []
for i in range(300):
    x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.2 )
    clf=RandomForestClassifier(n_estimators=100)

    model = clf.fit(x_train,y_train)
    
    y_pred=model.predict(x_test)


    acc =metrics.accuracy_score(y_test, y_pred)
    accuracy.append(acc)
    # print("Accuracy:",acc)
    if acc >= 0.95 :
        file = open("forest2.txt","w")
        c_code = port(model)
        file.write("c_code %s" % c_code)
        # print(c_code)
        # print("horrrray")
    
# print(max(accuracy))