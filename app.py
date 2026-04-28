import streamlit as st
import time
import random

sentences=[
    "Python is a powerful programming language.",
    "Streamlit makes web apps easy to build.",
    "Practice typing daily to improve speed.",
    "Data science is an exciting field.",
    "Consistency is the key to success."
]
st.title("⌨️ Typing Speed Test")
if "start_time" not in st.session_state:
    st.session_state.start_time=None
if "sentence" not in st.session_state:
    st.session_state.sentence=random.choice(sentences)
st.write("Type this sentence:")
st.info(st.session_state.sentence)
if st.button("Start Test"):
    st.session_state.start_time=time.time()
user_input=st.text_area("Start typing here...")
if st.button("Submit"):
    if st.session_state.start_time is None:
        st.warning("Click 'Start Test' first!")
    else:
        end_time=time.time()
        time_taken=end_time - st.session_state.start_time
        word_count=len(user_input.split())
        wpm=(word_count/time_taken)*60
        correct_chars=sum(1 for i, j in zip(user_input, st.session_state.sentence) if i==j)
        accuracy=(correct_chars / len(st.session_state.sentence))*100
        st.success(f" Time: {round(time_taken, 2)} seconds")
        st.success(f" WPM: {round(wpm, 2)}")
        st.success(f" Accuracy: {round(accuracy, 2)}%")