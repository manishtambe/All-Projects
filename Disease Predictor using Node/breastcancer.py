import numpy as np
import pandas as pd
import sys
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier

INPUT_PATH = "breast-cancer-wisconsin.data"
OUTPUT_PATH = "breast-cancer-wisconsin.csv"

HEADERS = ["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithelialCellSize","BareNuclei",
        "BlandChromatin","NormalNucleoli","Mitoses","CancerType"]

def read_data(path):
    data = pd.read_csv(path)
    return data

def get_headers(dataset):
    return dataset.columns.values

def add_headers(dataset, headers):
    dataset.columns = headers
    return dataset

def data_file_to_csv():
    headers = ["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithelialCellSize","BareNuclei",
            "BlandChromatin","NormalNucleoli","Mitoses","CancerType"]

    dataset = read_data(INPUT_PATH)
    dataset = add_headers(dataset, headers)
    dataset.to_csv(OUTPUT_PATH,index=False)
    #print("File Saved")
    
def split_dataset(dataset, train_percentage, feature_headers, target_header):
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers],dataset[target_header], train_size=train_percentage)
    return train_x, test_x, train_y, test_y
    
def handel_missing_values(dataset, missing_values_header, missing_label):
    return dataset[dataset[missing_values_header] != missing_label]

def random_forest_classifier(features, target):
    clf = RandomForestClassifier()
    clf.fit(features,target)
    return clf

def dataset_statitics(dataset):
    print(dataset.describe())
    
def main():
    dataset = pd.read_csv(OUTPUT_PATH)
    #dataset_statitics(dataset)
    dataset = handel_missing_values(dataset, HEADERS[6],'?')
    
    try:
        train_x, test_x, train_y, test_y = split_dataset(dataset, 0.7, HEADERS[1:-1], HEADERS[-1])
    except TypeError:
        print("Cannot Unpack!!")
        pass
    
    test_temp = [[int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]),int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])]]
    
    trained_model = random_forest_classifier(train_x, train_y)
    
    predictions = trained_model.predict(test_temp)

    print(predictions[0])
    #print("Test Accuracy :: ", accuracy_score(test_y, predictions))
    
if __name__ == '__main__':
    main()
    
    