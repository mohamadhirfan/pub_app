import streamlit as st
import pandas as pd
import numpy as np
import os
import time
from matplotlib import image





path1=os.getcwd()
path2=os.path.join(path1,'resources','pub.csv')
dir_of_interest1 = os.path.join(path1,"resources","image","irfan.png")
df = pd.read_csv(path2)
st.set_page_config(layout="wide")
st.title(':red[🍻Pubs In United Kingdom To Have Some Drink And Chillout🍻]')
st.subheader(":green[About me : :sunglasses: ]")
col1,col2,col3=st.columns(3, gap='small')
with col1:
    st.subheader("[LinkedIn](https://www.linkedin.com/in/mohamadhirfan/)")
with col2:
    st.subheader("[GitHub](https://github.com/mohamadhirfan?tab=repositories)")
with col3:
    if st.button('Bio'):
        img = image.imread(dir_of_interest1)
        st.markdown('''
        Name: MOHAMADH IRFAN
        
        Education : M.Sc(Statistics)''')
        st.image(img,caption='cool data scientist')


lat = st.text_input('Enter the lattitude')
log = st.text_input('Enter the longitude')

arr = np.array(df[['lat','lon']])

if lat and log:
    point = [float(lat),float(log)]
    df['distance'] = np.sqrt(np.sum((arr-point)**2,axis=1))
    df = df.sort_values(by='distance')
    df[['lat','lon',"name","Address",'PostCode','Babergh']][:5]
    st.map(df[['lat','lon']][:5])
    #Unique Bars and Local Authorities
unique=['Number of Pubs','Number of Postal Code']

option=st.radio(label="Select below options to see total count",
                options=unique,label_visibility="visible", horizontal=True)

if option=='Number of Pubs':
    st.subheader(f"Total Pubs in UK: :green[{df['name'].nunique()}]")
elif option=='Number of Postal Code':
    st.subheader(f"Total Post Codes in UK: :green[{df['PostCode'].nunique()}]")


st.subheader(":white[🥂🍹Pubs are at the heart of British communities and serve as places for friends to gather, people to relax and unwind and stories to be told🥂🍹.]")

