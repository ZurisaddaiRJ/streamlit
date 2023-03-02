import pandas as pd
import streamlit as st
import codecs

name_link =codecs.open('movies.csv','rU','latin1')

st.title('netflix app')

#--- LOGO ---#
st.sidebar.image("credencial.jpg")
st.sidebar.markdown("##")

@st.cache
def load_data(nrows):
    name_link = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(name_link, nrows=nrows)
    return data

data_load_state = st.text('cargando')
data = load_data(500)
data_load_state.text('netflix app!! (using st.cache)')

st.dataframe(data)

sidebar=st.sidebar
agree=sidebar.checkbox("Mostrar todos los filmes")
if agree:
    load_data(500)
sidebar.markdown(name_link)


name = sidebar.text_input("Titulo del filme")
btnbuscar = sidebar.button("Buscar filme")

if(btnbuscar):
    filterbyname = load_data(name)
    count_row = filterbyname.shape[0]
    st.write("total names: {count_row}")

    st.dataframe(filterbyname)

#selected box
@st.cache
def load_data_bydir(direct):
    data =pd.read_csv(name_link)
    filtered_data_bydir = data[data['director'] == direct]

    return filtered_data_bydir

selected_sex =sidebar.selectbox('Seleccionar director ', data['director'].unique())
btndirector = sidebar.button('filtrar')

if(btndirector):
    filterbysex =load_data_bydir(selected_sex)
    count_row = filterbysex.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(filterbysex)





