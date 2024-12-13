import streamlit as st
import pandas as pd

st.title('Анализ данных из CSV файла')

uploaded_file = st.file_uploader('Загрузите CSV файл', type="csv")

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.subheader('Данные:')
    st.dataframe(data)

    st.subheader('Статистика:')
    st.write(data.describe())

    st.subheader('График:')
    column = st.selectbox('Выберите столбец для построения графика', data.columns)

    st.line_chart(data[column])

    st.write(f'Тип данных выбранного столбца: {data[column].dtype}')
else:
    st.write('Загрузите файл для начала загрузки')
