import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("api_key")
client = OpenAI(api_key=api_key)

#Helper function to call the OpenAI API
def call_openai(prompt):
    response = client.responses.create(
        model="gpt-4.1",
        instructions=
        '''
        - Your are a Helping Bot for Mr. Kiran (Sai Kiran). 
        - You help Kiran to learn new topics and help him for his career progression.
        - You are helpful and friendly to Kiran. 
        - You should help Kiran only for IT and Technology specific Topics. For any other questions just mention him to refer to other sources.
        - Keep your responses very short and simple.
        ''' ,
        input=prompt,
        temperature=0.5,
        max_output_tokens=100
    )
    return response.output_text

#Main function to run the chatbot
def main():     
    st.title("Kiran's Helping Bot") #title of the chatbot
    if "messages" not in st.session_state: #session state is a dictionary that stores the state of the application
        st.session_state.messages = [] #initialize the messages list

    for message in st.session_state.messages:   #To render previous messages
        with st.chat_message(message["role"]):
            st.write(message["content"])


    if prompt := st.chat_input("Enter a message"): #chat input is a function that allows the user to enter a message
        st.session_state.messages.append({"role": "user", "content": prompt}) #append the message to the messages list
        with st.chat_message("user"):
            st.write(prompt)
        #call the openai api
        response = call_openai(prompt) #call the openai api
        st.session_state.messages.append({"role": "assistant", "content": response}) #append the response to the messages list
        with st.chat_message("assistant"):
            st.write(response)



if __name__ == "__main__":
    main()
    print(st.session_state.messages)