import streamlit as st  
from PIL import Image  

st.title('팝의 황제 마이클 잭슨 기념 웹 앱 🕺👑')


st.write('# 1. 인물소개')

st.markdown(
'''
# : King of Pop
마이클 잭슨(1958 ~ 2009)은 대중음악 역사상 가장 성공한 아티스트입니다.

- **대표적인 업적**
    - 역사상 가장 많이 팔린 앨범 *Thriller* 보유 🏆
    - 문워크(Moonwalk) 등 전설적인 댄스 퍼포먼스 창시 🕺
    - 세계 평화를 위한 사회 공헌 활동 (*Heal the World*) 🕊️

## 마이클잭슨 관련 외부 링크 공유
- [마이클 잭슨 공식 홈페이지](https://www.michaeljackson.com)
- [마이클 잭슨 유튜브 채널](https://www.youtube.com/user/michaeljacksonVEVO)

### 마이클 잭슨의 명언
"사람들은 내가 춤을 추기 때문에 무대에서 완벽하다고 생각하지만, 나는 그저 내 안의 음악을 표현할 뿐이다."
'''
)

st.divider() 


st.write('# 2. 히트 앨범 판매량에 대한 데이터')


album_data = [
    {"앨범명": "Thriller (1982년)", "추정 판매량": "7,000만 장 (역대 1위)"},
    {"앨범명": "Bad (1987년)", "추정 판매량": "4,500만 장"},
    {"앨범명": "Dangerous (1991년)", "추정 판매량": "3,200만 장"},
    {"앨범명": "Off the Wall (1979년)", "추정 판매량": "2,000만 장"}
]

st.dataframe(album_data) 

st.divider() 


st.write('# 3. 앨범 판매량 차트')

chart_data = {
    "Thriller": 70,
    "Bad": 45,
    "Dangerous": 32,
    "Off the Wall": 20
}

st.bar_chart(chart_data) 
st.divider() 


st.write('# 4. 마이클 잭슨의 밀랍인형')

st.subheader("📷 아티스트 밀랍인형 사진 (MJ.jpg)")
try:
    
    img = Image.open('./data/MJ.jpg')
    st.image(img, width=400, caption="Michael Jackson Photo")
except FileNotFoundError:
    st.error("⚠️ 'data' 폴더 안에 'MJ.jpg' 파일이 있는지 확인해주세요!")

st.subheader("🎵 마이클잭슨 이름을 인용한 노래 (DoAMJ.mp3)")
try:
    st.audio('./data/DoAMJ.mp3', format="audio/mpeg")
except FileNotFoundError:
    st.error("⚠️ 'data' 폴더 안에 'DoAMJ.mp3' 파일이 있는지 확인해주세요!")

st.subheader("🎬 마이클잭슨의 LP모음 (MJLP.mp4)")
try:
    st.video('./data/MJLP.mp4')
except FileNotFoundError:
    st.error("⚠️ 'data' 폴더 안에 'MJLP.mp4' 파일이 있는지 확인해주세요!")


