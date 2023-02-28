import streamlit as st
import os

st.title(":red[Innomatics] Data App :sunglasses:")
st.snow()


btn_click = st.button('Say hello')
if btn_click == True:
    st.subheader("Thanks for clocking")
    st.balloons()


