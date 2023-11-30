##
import warnings
warnings.filterwarnings('ignore')

import streamlit as st
import plotly.express as px
import pandas as pd

##
st.set_page_config(page_title="Superstore!!!",
                   page_icon=":bar_chart:",
                   layout="wide")
st.title(" :bar_chart: SuperStore Dashboard")

##
fl = "Data/Sample - Superstore.xls"

##
df = pd.read_excel(fl)
df.set_index("Row ID", inplace=True)
st.write(df.head())

##
df["Order Date"] = pd.to_datetime(df["Order Date"])

startDate = df["Order Date"].min()
endDate = df["Order Date"].max()
##
col1, col2 = st.columns(2)

with col1:
    date1 = st.date_input("start date", startDate)
    date1 = pd.to_datetime(date1)

with col2:
    date2 = st.date_input("end date", endDate)
    date2 = pd.to_datetime(date2)

##
df = df[(df["Order Date"] >= date1) &
        (df["Order Date"] <= date2)].copy()

##
st.sidebar.header("Choisissez votre filtre: ")
# Create filter for Region
region = st.sidebar.multiselect("Choisissez votre région", df["Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

# Create filter for State
state = st.sidebar.multiselect("Choisissez l'État", df2["State"].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)]

# Create filter for City
city = st.sidebar.multiselect("Choisissez la ville", df3["City"].unique())
if not city:
    df4 = df3.copy()
else:
    df4 = df3[df3["City"].isin(state)]

