import streamlit as st
import pandas as pd
import time
st.set_page_config(page_title="Spotify", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("01 Spotify.csv")
    time.sleep(5)
    return df 

df = load_data()

st.session_state["df"] = df

df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist] 

albuns = df_filtered["Album"].value_counts().index
album = st.selectbox("Album", albuns)
df_filtered_album = df[df["Album"] == album]

# display = st.checkbox("Display")

# if display:
#     st.bar_chart(df_filtered_album["Stream"])

# col1, col2 = st.columns(2)
col1, col2 = st.columns([0.7, 0.3]) #especifica largura de cada grafico

col1.bar_chart(df_filtered_album["Stream"])

col2.line_chart(df_filtered_album["Danceability"])


st.write(artist)
st.sidebar.button("test")


