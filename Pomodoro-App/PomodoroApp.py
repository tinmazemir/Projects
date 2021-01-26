import time
import streamlit as st

title = st.markdown("<h1 style='text-align: center; color: Blue;'>Session Time</h1>", unsafe_allow_html=True)
progress_bar = st.progress(100)


def Timer(session_min, break_min, break_number):
	while(break_number != 0):
		
		#session
		
		title.markdown("<h1 style='text-align: center; color: Blue;'>Session Time</h1>", unsafe_allow_html=True)
		progress_bar.progress(100)
		start_time = time.time()
		while(time.time() <= start_time + (float(session_min) * 60)):
			#print(int((start_time + float(session_min) * 60) - time.time()))
			progress_bar.progress(int(session_min / 60) * (int((start_time + float(session_min) * 60) - time.time())))

		#break
		
		title.markdown("<h1 style='text-align: center; color: Blue;'>Break Time</h1>", unsafe_allow_html=True)
		progress_bar.progress(100)
		start_time = time.time()
		while(time.time() <= start_time + (float(break_min) * 60)):
			progress_bar.progress((break_min / 60) * (int((start_time + float(break_min) * 60) - time.time())))
		break_number -= 1



session_min = st.sidebar.slider("Session Minute", 0, 180)
break_min = st.sidebar.slider("Break Minute", 1, 30)
break_number = st.sidebar.slider("Break Number", 1, 5)
#print(session_min)
start_button = st.sidebar.button("Start Session")

if start_button:
	Timer(int(session_min), int(break_min), int(break_number))