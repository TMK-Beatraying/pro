import streamlit as st
st.set_page_config(page_title = 'Ca sĩ yêu thích',page_icon=':microphone:',layout='wide',initial_sidebar_state='auto')

with st.sidebar:
  image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwHT1lW_Ls2bWp8bNQKEEW2TNeMh5Mgb9YvA&s'
  st.image(image,'Bảo Vân')
  st.write('Họ và tên: Bảo Vân')
st.title('Bài hát yêu thích :headphones:')
st.write('Vẫn nhớ - Cover')
audio = open('vannho.mp3','rb')
st.audio(audio,format = 'audio/mp3')
st.title(':musical_note: Video yêu thích:')
video = 'https://www.youtube.com/watch?v=LN-jSggbIBk'
st.video(video,format='video/mp4')