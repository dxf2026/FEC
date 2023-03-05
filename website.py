import streamlit as st
from PIL import Image

st.set_page_config(page_title="FEC", page_icon=":detective:", layout="wide")
if st.sidebar.button("Home"):
  st.title("Lie detecting based off emotion and tone")
  st.subheader("Upload Video File")
  video_file = st.file_uploader("", type=["mp4"])
  if st.button("Analyze Video"):
    zing = st.container()
    with zing:
      st.write("Calculating...")
      st.write("Here we go!")
#if st.sidebar.button("")  
if st.sidebar.button("About Us"):
  st.subheader("A little about this project and us")
  t0, t1, t2, t3, t4, t5, t6, t7, t8 = st.tabs(["About This", "Inspiration", "What It Does", "How We Built This", "Challenges", "Accomplishments", "What We Learned", "What's Next", "Built With"])
  t0.write("Compare the difference between the tone of speech of a person and the facial expressions on their face in order to find if they contradict each other; could detect lying in individuals.")
  t1.write("We saw the people in nearby groups using image tracking with objects, and we found that very interesting.")
  t2.write("Given a MP4 file of a person speaking and their face, it will try to determine the probability that they are lying using emotion of face, tone of their words, and their speaking speed.")
  t3.write("We used libraries that detected both facial expressions and the emotions that the words spoken by the person indicated, and then we compared the two in order to find if they contradicted; if they contradicted there was a high chance they were lying. If they were speaking very fast it would amplify this amount.")
  t4.write("A lot of libraries were outdated and needed correction or change in a library used or what portion of the library we used.")
  t5.write("Completing our first working Streamlit website.")
  t6.write("We learned a lot about OpenCV and Streamlit. This was also the first experience any of us had with ML.")
  t7.write("Using this project, we can try to determine more emotions besides positive or negative.")
  t8.write("Python, Streamlit, OpenCV, MoviePy, SciPy, Tensorflow")
  "Made by: Daniel Feng, Gabriel Huang, Joshua Zhou"
