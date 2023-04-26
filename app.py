import plotly.express as px
import pandas as pd
import streamlit as st

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

titanic_df = pd.merge(train, test, on='PassengerId', how='outer')
titanic_df.to_csv('merged.csv', index=False)
titanic_df = titanic_df.dropna()

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

if color_by_survival:
    st.plotly_chart(fig_age, use_container_width=True)
    st.plotly_chart(fig_fare, use_container_width=True)
    st.plotly_chart(fig_scatter, use_container_width=True)
else:
    st.plotly_chart(fig_age.update_traces(marker_color='blue'), use_container_width=True)
    st.plotly_chart(fig_fare.update_traces(marker_color='blue'), use_container_width=True)
    st.plotly_chart(fig_scatter.update_traces(marker_color='blue'), use_container_width=True)
