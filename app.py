import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Predictor")

# brand
company = st.selectbox('Brand',df['Company'].unique(), help='Which company laptop are you looking for?')

# type of laptop
type = st.selectbox('Type',df['TypeName'].unique(), help='What type of laptop do you want?')

# Ram
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64], help='Select the RAM size of the laptop.')


# weight
weight = st.number_input('Weight of the Laptop', help='Select the approx weight of the desired laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'], help='Do you want the laptop to be touchscreen or not?')

# IPS
ips = st.selectbox('IPS',['No','Yes'], help='Do you want IPS display?')

# screen size
screen_size = st.number_input('Screen Size', help='What should be the screen size? Standard size are 13.3 inch, 14 inch, 15.6 inch and 17 inch')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'], help='What resolution are you looking for?')

#cpu
cpu = st.selectbox('CPU',df['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.markdown("##### The predicted price of this configuration in CAD is $" + str(round((int(np.exp(pipe.predict(query)[0]))/62),2)))
