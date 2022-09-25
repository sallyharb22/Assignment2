#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly as py
import plotly.express as px
import streamlit as st


# In[2]:


df = pd.read_csv('student_scores.csv')
df1 = pd.read_csv('smoke_detection_iot.csv')
df2 = pd.read_csv('Breast_Cancer.csv')
df3 = pd.read_csv('vending_machine_sales.csv')
df4 = pd.read_excel('Kerala data.xlsx')


# In[3]:


fig = px.scatter(df, x = "Hours", y = "Scores", title = "Scores Based on Hours of Study")


# In[4]:


fig1 = px.box(df1, x = "Temperature[C]")


# In[5]:


fig2 = px.pie(df2, "Status", title = "Current Status of Surveyed Breast Cancer Patients")


# In[6]:


fig3 = px.bar(df3, "Type", title = "Vending Machine Sales Methods of Payment")
fig3.update_layout(plot_bgcolor="#F6E4D2")


# In[7]:


fig4 = px.line(df4, x = "date", y = "Active", title = "Active COVID-19 Cases in Kerala")


# In[8]:


interactive_plot_1 = st.container()
interactive_plot_2 = st.container()
interactive_plot_3 = st.container()
interactive_plot_4 = st.container()
interactive_plot_5 = st.container()


# In[9]:


with interactive_plot_1:
    st.header("How can a person achieve higher grades?")
    st.text("Look at this! With studying more, you can achieve higher grades!")
    st.plotly_chart(fig, use_container_width=True)


# In[5]:


with interactive_plot_2:
    st.title("On a different topic, lets look at the temperature during smoke detection!")
    st.plotly_chart(fig1, use_container_width=True)
    st.dataframe(df1)


# In[6]:


with interactive_plot_3:
    st.title("Let's move into medicine and look at the status of surveyed breast cancer patients!")
    st.header("Most of the surveyed patients are still alive, god bless!")
    st.plotly_chart(fig2, use_container_width=True)


# In[ ]:


with interactive_plot_4:
    st.title("Do people pay more using cash or card when using vending machines?")
    st.plotly_chart(fig3, use_container_width=True)
    yes_cash = st.checkbox("Cash")
    no_card = st.checkbox ("Card")
    if yes_cash:
        st.write("Try using card, it's easier than physically holding the money!")
    if no_card:
        st.write("Great, that's very efficient!")


# In[7]:


with interactive_plot_5:
    st.header("How many active COVID-19 cases where there in Kerala in 2020?")
    st.plotly_chart(fig4, use_container_width=True)
    st.text("Click the Kerala Button and learn more about this area!")
    result = st.button("Kerala Button")
    st.write(result)
    if result:
        st.write("https://en.wikipedia.org/wiki/Kerala")

