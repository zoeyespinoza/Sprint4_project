import plotly.express as px
import pandas as pd
import streamlit as st
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

titanic_df = pd.merge(train, test, on='PassengerId', how='outer')
titanic_df.to_csv('merged.csv', index=False)

st.header("Titanic Passenger Data")
color_by_survival = st.checkbox("Color by Survival")

fig_age = px.histogram(titanic_df, x="Age_x", nbins=20,
                       color="Survived",
                       title="Distribution of Passenger Age")


fig_fare = px.histogram(titanic_df, x="Fare_x", nbins=20, 
                        color="Survived",
                        title="Distribution of Passenger Fares")

fig_scatter = px.scatter(titanic_df, x="Age_x", y="Fare_x", 
                         color="Survived",
                         title="Passenger Age vs. Fare")

fig_age.show()
fig_fare.show()
fig_scatter.show()

