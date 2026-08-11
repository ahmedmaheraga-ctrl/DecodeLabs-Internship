# import libraries
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
# generate variables
iris = load_iris()

x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
# print project name
print("="*80)
print("            project 2. Data classification using AI           ")
print("="*80)

# print the first 5 rows of the data to confirme every thing is ok
print(x.head())
scaler= StandardScaler()
x_scaled = scaler.fit_transform(x)

def main():
    
    x_train, x_test, y_train, y_test = train_test_split(
        x_scaled, y, test_size=0.2, random_state=42, shuffle=True
        )
    # k=5
    model = KNeighborsClassifier(n_neighbors=5)
    # fit
    model.fit(x_train,y_train)
    # predict
    predictions = model.predict(x_test)
    
    print("="*80)
    print("\nCOFUSION_MATRIX : \n")
    print(confusion_matrix(y_test,predictions))
    
    print("="*80)
    print("\nCLASSIFICATION_REPORT : \n")
    print(classification_report(y_test,predictions,target_names=iris.target_names))
    
if __name__ == "__main__":
    main()
    