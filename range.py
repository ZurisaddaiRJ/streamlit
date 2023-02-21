import streamlit as st
import pandas as pd

st.title('Streamlit - search ranges')

DATA_URL = ('https://firebasestorage.googleapis.com/v0/b/streamlit-zuri.appspot.com/o/csv%2Fdataset.csv?alt=media&token=ebafcf9b-e030-4dcf-b753-0dbaead9b51b')

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL) # read csv
    filtered_data_byrange = data[ (data['index'] >= startid) & (data['index'] <= endid) ]

    return filtered_data_byrange # return the dataframe

startid =  st.text_input('Start index : ')
endid = st.text_input('End index : ')
btnRange = st.button('Search by range' )

if (btnRange):
    filterbyrange = load_data_byrange(int(startid), int(endid)) # call the function
    count_row = filterbyrange.shape[0] # count number of records
    st.write(f"Total items : {count_row}")

    st.dataframe(filterbyrange)
