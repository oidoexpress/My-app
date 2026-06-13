import strEamlit as st
st.title("이시형의 첫 웹앱!!")
st.write('반가워요! 와주셔서 감사드립니다!')

import streamlit as st

st.set_page_config(
    page_title="MBTI Pokémon Finder",
    page_icon="⚡",
    layout="centered"
)

# CSS 꾸미기
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#74ebd5,#9face6);
}

.title {
    text-align:center;
    font-size:3rem;
    font-weight:bold;
    color:white;
    margin-bottom:20px;
}

.card {
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 8px 20px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">✨ MBTI Pokémon Finder ✨</div>', unsafe_allow_html=True)

pokemon_data = {
    "INTJ": {
        "pokemon": "Mewtwo",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "desc": "전략적이고 독립적인 천재형. 목표를 향해 꾸준히 나아가는 강력한 리더!"
    },
    "INTP": {
        "pokemon": "Alakazam",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
        "desc": "호기심이 많고 분석을 좋아하는 발명가형!"
    },
    "ENTJ": {
        "pokemon": "Charizard",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "desc": "카리스마 넘치는 지휘관. 강한 추진력을 가지고 있어!"
    },
    "ENTP": {
        "pokemon": "Gengar",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
        "desc": "창의적이고 장난기 많은 아이디어 뱅크!"
    },
    "INFJ": {
        "pokemon": "Lugia",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
        "desc": "조용하지만 깊은 통찰력을 가진 이상주의자!"
    },
    "INFP": {
        "pokemon": "Eevee",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "desc": "상상력이 풍부하고 따뜻한 마음을 가진 몽상가!"
    },
    "ENFJ": {
        "pokemon": "Lucario",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
        "desc": "사람들을 이끄는 따뜻한 리더!"
    },
    "ENFP": {
        "pokemon": "Pikachu",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "desc": "에너지 넘치고 모두와 친해지는 분위기 메이커!"
    },
    "ISTJ": {
        "pokemon": "Blastoise",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "desc": "책임감 있고 믿음직한 수호자!"
    },
    "ISFJ": {
        "pokemon": "Chansey",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png",
        "desc": "친절하고 헌신적인 돌봄 전문가!"
    },
    "ESTJ": {
        "pokemon": "Machamp",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png",
        "desc": "실행력이 뛰어난 강한 리더!"
    },
    "ESFJ": {
        "pokemon": "Togekiss",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/468.png",
        "desc": "주변 사람들을 행복하게 만드는 사교왕!"
    },
    "ISTP": {
        "pokemon": "Scizor",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/212.png",
        "desc": "실용적이고 침착한 문제 해결사!"
    },
    "ISFP": {
        "pokemon": "Vaporeon",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/134.png",
        "desc": "예술적 감각이 뛰어난 자유로운 영혼!"
    },
    "ESTP": {
        "pokemon": "Infernape",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/392.png",
        "desc": "모험을 즐기고 행동력이 뛰어난 도전자!"
    },
    "ESFP": {
        "pokemon": "Jigglypuff",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
        "desc": "밝고 즐거운 엔터테이너!"
    }
}

mbti = st.selectbox(
    "🧠 당신의 MBTI를 선택하세요!",
    list(pokemon_data.keys())
)

if st.button("🔍 나와 어울리는 포켓몬 찾기!", use_container_width=True):

    result = pokemon_data[mbti]

    st.balloons()

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.image(result["image"], width=220)

    st.subheader(f"🌟 당신과 가장 잘 어울리는 포켓몬은...")
    st.title(result["pokemon"])

    st.success(result["desc"])

    st.markdown("### 🎯 성향 분석")
    st.write(
        f"""
        **{mbti}** 유형은 {result["pokemon"]}처럼 자신만의 강점을 가지고 있습니다.

        ✔ 개성이 뚜렷함  
        ✔ 특별한 재능 보유  
        ✔ 자신만의 방식으로 성장함  

        포켓몬 세계에서라면 최고의 파트너가 될 수 있어요!
        """
    )

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with ❤️ using Streamlit & Pokémon")
