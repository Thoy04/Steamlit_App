import seaborn as sns
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt


st.title('Data Dashboard')

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file:
    st.write('File Uploladed...')

    df = pd.read_csv(uploaded_file)

    st.subheader('Data Preview')
    st.write(df.head(7))

    st.subheader('Data Info')
    st.write(df.describe())

    st.subheader('Filter Data')
    ids = list(df['ID'].unique())
    selected_id = st.selectbox('Select ID to filter by', ids)
    filtered_df = df[df['ID'] == selected_id]

    st.subheader('Plot Performance Data')

    if st.button('Generate Plot'):
        st.line_chart(filtered_df.set_index('Date')['Performance'])

    st.subheader('Plot Performance Boxplots')

    if st.button('Generate Boxplot'):
        fig, ax = plt.subplots()
        ax = sns.boxplot(data=df, x='ID', y='Performance')
        st.pyplot(fig)
else:
    st.write('Waiting For File Uploladed...')

