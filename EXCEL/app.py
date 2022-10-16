import pandas as pd

import streamlit as st


st.set_page_config(page_title='Genomics of Drug Sensitivity in Cancer')
st.header('Results 2021')
st.subheader('Read More.')

excel_file = 'GDSC.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:D',
                   header=3)

df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='F:G',
                                header=3)
df_participants.dropna(inplace=True)