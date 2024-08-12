import streamlit as st
from langchain.prompts import  PromptTemplate
from langchain.llms import  CTransformers
from langchain.memory import ConversationBufferMemory

## Function to get response from LLAMA 2 Model
def getResponse(input_text, language):
    ### LLama2 model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={
                          'max_new_tokens':500,
                          'temperature':0.01})
    ### Prompt Template

    template="""
      Write the code using {language} for {input_text}
    """
    prompt = PromptTemplate(input_variables=["language", "input_text"],
                            template=template
                            )
    ### Memory
    memory = ConversationBufferMemory()
    ## Generate response
    response = llm(prompt.format(language=language , input_text= input_text))
    memory.save_context(
        {"input": input_text},
        {"output": response})
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
                       'Dart',
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