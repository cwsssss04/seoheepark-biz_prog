import streamlit as st # streamlit 라이브러리 

"""
#비즈니스 모델 분석

[네이버](http://www.naver.com)

[홍익대학교](https://www.hongik.ac.kr)

이것이 일반 본문

```
print("코드 블록")
```
"""

st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

with st.echo():
    #이 블록의 코드와 결과를 출력
    name= 'Seohee Park'
    st.write("Hello,Streamlit!",name)

    st.latex('\int_a^bf(x)dx')
    

'# :movie: 이미지, 오디오, 동영상'

#### :[이미지: st.image()]
st.image("./data/images.png", caption="파이썬 로고", width=500)


