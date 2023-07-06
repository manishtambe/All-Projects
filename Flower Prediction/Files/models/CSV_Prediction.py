from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score


def User_K_Neighbors_Classifier(Sepal_Length, Sepal_Width, Petal_Length, Petal_Width):
    
    print(Sepal_Length, Sepal_Width, Petal_Length, Petal_Width)
    
    Sepal_Length = float(Sepal_Length)
    Sepal_Width = float(Sepal_Width)
    Petal_Length = float(Petal_Length)
    Petal_Width = float(Petal_Width)
    
    Data_User_Test = list()
    temp = list()
    
    temp.append(Sepal_Length)
    temp.append(Sepal_Width)
    temp.append(Petal_Length)
    temp.append(Petal_Width)
    
    Data_User_Test.append(temp)
    
    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    Data_Train, Data_Test, Target_Train, Target_Test = train_test_split(Data, Target, test_size=0.7)

    Classifier = KNeighborsClassifier()
    
    print(Data_Train, Target_Train)

    Classifier.fit(Data_Train, Target_Train)
    Predictions1 = Classifier.predict(Data_Test)


    Predictions = Classifier.predict(Data_User_Test)
    
    
    Accuracy = accuracy_score(Target_Test, Predictions1)
    
    print(Predictions[0], Accuracy)

    return Predictions[0],Accuracy

