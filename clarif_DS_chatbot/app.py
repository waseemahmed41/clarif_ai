import streamlit as st
from streamlit_chat import message
import llama

# Clear Chat function
def clear_chat():
    st.session_state.messages = [{"role": "assistant", "content": "Say something to get started!"}]

# Streamlit UI setup
st.title("Clarifai Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Say something to get started!"}]

# Input form for the user message
with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])

    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        label_visibility="collapsed",
    )

    b.form_submit_button("Send", use_container_width=True)

# Display chat history
for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user")

# Process user input
if user_prompt:
    print('user_prompt: ', user_prompt)

    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    message(user_prompt, is_user=True)

    # Call to Llama/Clarifai API for response
    try:
        response = llama.get_response(user_prompt)  # Get response from Clarifai's DeepSeek model
    except Exception as e:
        response = f"Error: {str(e)}"

    # Append the assistant's message
    msg = {"role": "assistant", "content": response}
    print('msg.content: ', msg["content"])
    
    # Update session state and display the response
    st.session_state.messages.append(msg)
    message(msg["content"])

# Clear chat button
if len(st.session_state.messages) > 1:
    st.button('Clear Chat', on_click=clear_chat)
