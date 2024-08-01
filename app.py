import streamlit as st
from langchain.prompts import  PromptTemplate
from langchain.llms import  CTransformers
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint

# Load environment variables from the .env file
load_dotenv()

# Access the Hugging Face API token
huggingface_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Check if the token is loaded correctly
if huggingface_api_token is None:
    raise ValueError("Hugging Face API token is not set. Please check your .env file.")

## Function to get response from LLAMA 2 Model
def getResponse(input_text, language):

    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-2-7b",
        temperature=0.01,
        huggingfacehub_api_token=huggingface_api_token
    )

### Prompt Template

    template="""
    Write a code using { language } for {input_text}
    """
    prompt = PromptTemplate(input_variables=["lang", "text"],
                            template=template
                            )

    ## Generate response
    response = llm(prompt.format(lang=language , text= input_text))
    print(response)
    return response


# Setting Up StreamLit framework
st.set_page_config(

    page_title="Developer Assistant",
    page_icon='👽',
    layout='centered',
    initial_sidebar_state='collapsed'
)
st.header("Developer Assistant 👽")

input_text=st.text_input("Enter the question")

col1 =st.columns([5,5])

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