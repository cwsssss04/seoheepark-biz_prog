import os
import streamlit as st  
from PIL import Image  

image_path_mj = "MJ.jpg"
image_path_korea = "mj-korea.jpg"
image_path_bubbles = "mj-bubbles.png"

# 메인 제목
st.markdown("# 마이클 잭슨에 대해 <br> &nbsp;&nbsp;&nbsp;&nbsp; 알아보자 🕺👑", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .section-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1E90FF;
    }
    /* 💡 모든 이미지 캡션의 글자 크기를 살짝 줄여서 한 줄로 잘 나오게 만듭니다 */
    .stImage div p {
        font-size: 0.8rem !important;
        white-space: nowrap; /* 글자가 절대 아래로 꺾이지 않고 한 줄로 나오게 강제 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 1. 인물소개
with st.expander("👤 1. 인물소개", expanded=False):
    st.markdown(
        '''
        ### 👑 King of Pop
        마이클 잭슨(1958 ~ 2009)은 대중음악 역사상 가장 성공한 아티스트입니다.
        
        * **대표적인 업적**
            * 역사상 가장 많이 팔린 앨범 *Thriller* 보유 🏆
            * 문워크(Moonwalk) 등 전설적인 댄스 퍼포먼스 창시 🕺
            * 세계 평화를 위한 사회 공헌 활동 (*Heal the World*) 🕊️
        
        #### 🔗 외부 링크 공유
        * [마이클 잭슨 공식 홈페이지](https://www.michaeljackson.com)
        * [마이클 잭슨 유튜브 채널](https://www.youtube.com/user/michaeljacksonVEVO)
        
        > 💬 **마이클 잭슨의 명언**  
        > "사람들은 내가 춤을 추기 때문에 무대에서 완벽하다고 생각하지만, <br> 나는 그저 내 안의 음악을 표현할 뿐이다."
        '''
    )

# 2. 히트 앨범 판매량 데이터
with st.expander("📊 2. 히트 앨범 판매량에 대한 데이터", expanded=False):
    st.write("### 📀 역대 최고 히트 앨범 판매량")
    album_data = [
        {"앨범명": "Thriller (1982년)", "추정 판매량": "7,000만 장 (역대 1위)"},
        {"앨범명": "Bad (1987년)", "추정 판매량": "4,500만 장"},
        {"앨범명": "Dangerous (1991년)", "추정 판매량": "3,200만 장"},
        {"앨범명": "Off the Wall (1979년)", "추정 판매량": "2,000만 장"}
    ]
    st.dataframe(album_data, use_container_width=True)

# 3. 앨범 판매량 차트
with st.expander("📈 3. 앨범 판매량 차트", expanded=False):
    st.write("### 📊 주요 앨범 판매량 시각화 (단위: 백만 장)")
    chart_data = {
        "Thriller": 70,
        "Bad": 45,
        "Dangerous": 32,
        "Off the Wall": 20
    }
    st.bar_chart(chart_data)

# 4. 마이클 잭슨의 모습
with st.expander("🎬 4. 마이클 잭슨의 모습", expanded=False):
    st.write("### 📷 마이클 잭슨의 다양한 모습")
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if os.path.exists(image_path_mj):
            st.image(image_path_mj, use_container_width=True, caption="마이클 잭슨의 모습")
        else:
            st.error(f"⚠️ 이미지를 찾을 수 없습니다.\n\n확인한 경로: {image_path_mj}")
            
    with col2:
        if os.path.exists(image_path_korea):
            st.image(image_path_korea, use_container_width=True, caption="마이클 잭슨이 한국에 방문한 모습")
        else:
            st.error(f"⚠️ 이미지를 찾을 수 없습니다.\n\n확인한 경로: {image_path_korea}")
            
    with col3:
        if os.path.exists(image_path_bubbles):
            st.image(image_path_bubbles, use_container_width=True, caption="마이클 잭슨과 그의 애완 침팬지의 모습")
        else:
            st.error(f"⚠️ 이미지를 찾을 수 없습니다.\n\n확인한 경로: {image_path_bubbles}")
            
    st.caption("마이클 잭슨은 실제로 동물 러버라고 알려져 있을 정도로, 침팬지를 제외하고도 기린, 라마 등을 키웠습니다.")
    st.caption("마이클 잭슨은 아이들을 좋아해서 여러 방법으로 아이들에게 기부하는 기부천사로도 알려져 있습니다.")
    st.caption("또한, 환경 보호 운동에도 적극적으로 참여하며, 대표곡인 'Earth Song' 등을 통해 지구와 자연 보호의 메시지를 전하기도 했습니다.")
