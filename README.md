# FEC
Compare the difference between the tone of speech of a person and the facial expressions on their face in order to find if they contradict each other; could detect lying in individuals.

Inspiration
We saw the people in nearby groups using image tracking with objects, and we found that very interesting.

What it does
Given a MP4 file of a person speaking and their face, it will try to determine the probability that they are lying using emotion of face, tone of their words, and their speaking speed.

How we built it
We used libraries that detected both facial expressions and the emotions that the words spoken by the person indicated, and then we compared the two in order to find if they contradicted; if they contradicted there was a high chance they were lying. If they were speaking very fast it would amplify this amount.

Challenges we ran into
A lot of libraries were outdated and needed correction or change in a library used or what portion of the library we used.

Accomplishments that we're proud of
Completing our first working Streamlit website.

What we learned
We learned a lot about OpenCV and Streamlit. This was also the first experiene any of us had with ML

What's next for FEC
We can try to determine more emotions besides positive or negative.

Built With
Python, Streamlit, OpenCV, MoviePy, SciPy, Tensorflow, and DeepFace
