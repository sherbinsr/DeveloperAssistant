import streamlit as st
from langchain.prompts import  PromptTemplate
from langchain.llms import  CTransformers

## Function to get response from LLAMA 2 Model
def getResponse(input_text, language):

    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})





# Setting Up StreamLit framework
st.set_page_config(

    page_title="Developer Assistant",
    page_icon='👽',
    layout='centered',
    initial_sidebar_state='collapsed'
)
st.header("Developer Assistant 👽")

input_text=st.text_input("Enter the question")

col1 = st.columns([5, 5])

with col1:
    language=st.selectbox('Select Language',
                          ('Java',
                           'Python',
                           'C++',
                           'C',
                           'Javascript',
                           'R',
                           'Php',
                           'Rust',
                           'Kotlin',
                           'Swift',
                           'Scala'
                           ),index=0)

submit = st.button("Generate")

## Response

if submit:
    st.write(getResponse(input_text,language))