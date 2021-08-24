import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write('''
# Bienvenue dans votre application Machine learning 
Cette application prédit la catégorie des fleurs d'iris
''')

st.sidebar.header("Les parametres d'entrées")

def uses_input():
    sepal_lenght=st.sidebar.slider('La longueur du sepal', 4.3, 7.9, 5.3)
    sepal_widht=st.sidebar.slider('La largeur du sepal', 2.0, 4.4, 3.3)
    petal_lenght=st.sidebar.slider('La longueur du petal', 1.0, 6.9, 2.3)
    petal_widht=st.sidebar.slider('La largeur du petal', 0.1, 2.5, 1.3)
    data={'sepal_lenght': sepal_lenght,
          'sepal_widht': sepal_widht,
          'petal_lenght': petal_lenght,
          'petal_widht': petal_widht,
    }
    fleur_parametre=pd.DataFrame(data, index=[0])
    return fleur_parametre

st.date_input('calandrier')

df=uses_input()

st.subheader('On veut trouver la categorie de cette fleur')
st.write(df)

iris=datasets.load_iris()
model=RandomForestClassifier()
model.fit(iris.data, iris.target)
prediction=model.predict(df)

st.subheader("La categorie de la fleur d'iris est: ")
st.write(iris.target_names[prediction])