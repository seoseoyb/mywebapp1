
import streamlit as st

st.set_page_config(
    page_title="Trip, My Type! ♡",
    page_icon="✈️",
    layout="centered",
)

# ----------------------------
# 귀여운 디자인
# ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nunito:wght@400;600;700;800&display=swap');

.stApp {
    background: linear-gradient(180deg, #fff0f6 0%, #fff8fb 55%, #ffffff 100%);
    color: #68465b;
}

.block-container {
    max-width: 720px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p, label, div {
    font-family: 'Nunito', sans-serif;
}

h1, h2, h3 {
    color: #68465b !important;
}

h1, h2 {
    font-family: 'Jua', sans-serif;
}

.hero {
    background: #ffffff;
    border: 1px solid #f7dce8;
    border-radius: 28px;
    padding: 30px 24px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(217, 148, 180, 0.10);
}

.hero-emoji {
    font-size: 3.5rem;
}

.hero h1 {
    font-size: 2.4rem;
    margin: 8px 0;
}

.hero p {
    color: #a47c91;
    margin-bottom: 0;
}

.pill {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    background: #fce1ed;
    color: #b45c86;
    font-size: 0.82rem;
    font-weight: 800;
    letter-spacing: 0.5px;
}

.result-card {
    background: #ffffff;
    border: 1px solid #f7dce8;
    border-radius: 24px;
    padding: 24px;
    margin-top: 12px;
}

.result-title {
    font-family: 'Jua', sans-serif;
    color: #68465b;
    font-size: 1.8rem;
}

.result-subtitle {
    color: #b45c86;
    font-weight: 700;
    font-size: 0.9rem;
}

.reason {
    background: #fff3f8;
    border-radius: 16px;
    padding: 16px;
    line-height: 1.7;
    color: #76576a;
}

.stButton > button {
    width: 100%;
    border: 0;
    border-radius: 999px;
    background: #f4b4d0;
    color: #68465b;
    font-weight: 800;
    padding: 0.7rem;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #ed9fc1;
    border: 0;
    color: #68465b;
}

[data-testid="stSelectbox"] label {
    color: #68465b;
    font-weight: 700;
}

.footer {
    text-align: center;
    color: #b995a8;
    font-size: 0.85rem;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# MBTI별 여행 추천 데이터
# ----------------------------
travel_data = {
    "ISTJ": {
        "place": "교토, 일본 🇯🇵",
        "style": "차분하고 계획적인 문화 여행",
        "description": "전통과 질서가 살아 있는 교토에서 천천히 여행을 즐겨보세요.",
        "reason": "계획을 세우고 역사와 문화에 집중하는 여행이 잘 어울려요. 정돈된 거리와 고즈넉한 사찰을 둘러보며 여유로운 하루를 보내보세요.",
        "activities": ["전통 사찰 산책", "다도 체험", "정갈한 일본 음식 맛보기"],
        "color": "#E8DDF5",
    },
    "ISFJ": {
        "place": "제주도, 한국 🇰🇷",
        "style": "따뜻하고 여유로운 힐링 여행",
        "description": "아름다운 자연과 맛있는 음식으로 마음을 충전하는 제주 여행!",
        "reason": "편안한 분위기에서 소중한 사람들과 추억을 만들기 좋아요. 바다를 바라보고 맛있는 음식을 먹으며 행복한 시간을 보내보세요.",
        "activities": ["오름 산책", "카페에서 쉬기", "제주 맛집 탐방"],
        "color": "#DDEFE4",
    },
    "INFJ": {
        "place": "프라하, 체코 🇨🇿",
        "style": "감성적이고 의미 있는 여행",
        "description": "동화 속 풍경을 걸으며 나만의 특별한 이야기를 만들어보세요.",
        "reason": "깊이 있는 경험과 아름다운 분위기를 좋아하는 여행자에게 어울려요. 오래된 건축물과 조용한 골목을 천천히 탐험해보세요.",
        "activities": ["유서 깊은 성 탐방", "감성적인 카페", "일몰 풍경 감상"],
        "color": "#E5DDF4",
    },
    "INTJ": {
        "place": "싱가포르 🇸🇬",
        "style": "효율적이고 새로운 것을 탐험하는 여행",
        "description": "미래 도시의 기술과 건축, 색다른 문화를 한 번에 만나는 여행!",
        "reason": "새로운 시스템과 독특한 공간을 탐험하는 데 흥미를 느낄 수 있어요. 스마트한 도시 풍경과 다양한 문화를 효율적으로 즐겨보세요.",
        "activities": ["미래형 정원 관람", "도시 건축 탐방", "박물관 관람"],
        "color": "#DCE9F8",
    },
    "ISTP": {
        "place": "다낭, 베트남 🇻🇳",
        "style": "자유롭고 액티비티 가득한 여행",
        "description": "바다와 모험을 동시에 즐기는 짜릿한 여행을 떠나보세요!",
        "reason": "직접 체험하고 새로운 활동을 즐기는 여행이 잘 어울려요. 바다에서 놀고 새로운 장소를 자유롭게 탐험하며 하루를 채워보세요.",
        "activities": ["해변 액티비티", "오토바이 대신 안전한 투어", "현지 음식 체험"],
        "color": "#D9EDF5",
    },
    "ISFP": {
        "place": "발리, 인도네시아 🇮🇩",
        "style": "감각적이고 아름다운 자연 여행",
        "description": "예쁜 풍경과 편안한 분위기 속에서 나만의 휴식을 즐겨보세요.",
        "reason": "아름다운 자연과 감성적인 공간을 좋아하는 여행자에게 잘 어울려요. 천천히 풍경을 감상하고 취향에 맞는 카페를 찾아보세요.",
        "activities": ["자연 속 산책", "예쁜 카페 방문", "공예 체험"],
        "color": "#F8E5D8",
    },
    "INFP": {
        "place": "스위스 🇨🇭",
        "style": "낭만적이고 평화로운 자연 여행",
        "description": "그림 같은 풍경 속에서 마음이 편안해지는 시간을 가져보세요.",
        "reason": "자연의 아름다움과 깊은 감정을 느낄 수 있는 여행이 잘 어울려요. 산과 호수의 풍경을 바라보며 나만의 영감을 찾아보세요.",
        "activities": ["호수 산책", "아름다운 마을 탐방", "여행 일기 쓰기"],
        "color": "#DCEEE5",
    },
    "INTP": {
        "place": "도쿄, 일본 🇯🇵",
        "style": "호기심 가득한 탐구 여행",
        "description": "독특한 기술과 문화, 새로운 아이디어를 발견하는 여행!",
        "reason": "새로운 지식과 독특한 경험을 탐구하는 것을 좋아한다면 도쿄가 재미있을 거예요. 관심 있는 분야의 장소를 자유롭게 탐험해보세요.",
        "activities": ["과학관 관람", "독특한 서점 탐방", "전자상가 구경"],
        "color": "#DFE5F7",
    },
    "ESTP": {
        "place": "방콕, 태국 🇹🇭",
        "style": "활기차고 재미있는 도시 여행",
        "description": "맛있는 음식과 신나는 거리 분위기를 마음껏 즐겨보세요!",
        "reason": "생생한 현장감과 새로운 경험을 좋아하는 여행자에게 어울려요. 활기찬 시장과 맛있는 음식을 즐기며 여행의 재미를 느껴보세요.",
        "activities": ["야시장 구경", "현지 음식 맛보기", "도시 명소 탐방"],
        "color": "#F8E1D9",
    },
    "ESFP": {
        "place": "파리, 프랑스 🇫🇷",
        "style": "즐겁고 감성적인 도시 여행",
        "description": "맛있는 디저트와 예쁜 거리에서 행복한 추억을 만들어보세요.",
        "reason": "즐거운 분위기와 아름다운 풍경, 맛있는 음식이 있는 여행이 잘 어울려요. 유명한 명소뿐 아니라 작은 골목의 매력도 느껴보세요.",
        "activities": ["디저트 카페", "미술관 관람", "도시 산책"],
        "color": "#F8DDE9",
    },
    "ENFP": {
        "place": "런던, 영국 🇬🇧",
        "style": "새로운 만남과 문화가 있는 여행",
        "description": "다양한 문화와 재미있는 이야기가 가득한 런던으로 떠나보세요!",
        "reason": "새로운 사람과 문화, 예상하지 못한 경험을 즐기는 여행자에게 어울려요. 다양한 공간을 탐험하고 그곳에서만 느낄 수 있는 경험을 만들어보세요.",
        "activities": ["뮤지컬 관람", "빈티지 숍 탐방", "공원에서 피크닉"],
        "color": "#F6E3D2",
    },
    "ENTP": {
        "place": "뉴욕, 미국 🇺🇸",
        "style": "도전적이고 창의적인 도시 여행",
        "description": "끝없는 아이디어와 다양한 문화가 살아 숨 쉬는 도시!",
        "reason": "새로운 자극과 독특한 아이디어를 좋아하는 여행자에게 잘 어울려요. 자유롭게 도시를 탐험하며 예상하지 못한 즐거움을 찾아보세요.",
        "activities": ["현대미술관 관람", "브루클린 산책", "도시 건축 탐방"],
        "color": "#DCE8F6",
    },
    "ESTJ": {
        "place": "홍콩 🇭🇰",
        "style": "알차고 역동적인 도시 여행",
        "description": "도시의 활기와 다양한 명소를 효율적으로 즐겨보세요.",
        "reason": "여러 명소를 알차게 둘러보고 다양한 활동을 즐기는 여행이 잘 어울려요. 맛있는 음식과 도시의 독특한 풍경을 모두 경험해보세요.",
        "activities": ["도시 전망 감상", "시장 탐방", "유명 명소 방문"],
        "color": "#F3E0D3",
    },
    "ESFJ": {
        "place": "오사카, 일본 🇯🇵",
        "style": "맛있고 즐거운 친목 여행",
        "description": "친구들과 맛있는 음식과 즐거운 추억을 가득 쌓아보세요!",
        "reason": "사람들과 함께 맛있는 음식을 먹고 즐거운 시간을 보내는 여행이 잘 어울려요. 활기찬 거리에서 다양한 먹거리를 즐겨보세요.",
        "activities": ["맛집 투어", "테마파크 방문", "친구들과 사진 찍기"],
        "color": "#F8DDE5",
    },
    "ENFJ": {
        "place": "시드니, 호주 🇦🇺",
        "style": "사람들과 함께하는 활기찬 여행",
        "description": "아름다운 바다와 다채로운 문화를 모두 즐기는 여행!",
        "reason": "새로운 사람들과 교류하고 함께 특별한 경험을 만드는 여행이 잘 어울려요. 아름다운 해변과 도시 문화를 함께 즐겨보세요.",
        "activities": ["해변 산책", "문화 공연 관람", "현지 투어 참여"],
        "color": "#DCEFEA",
    },
    "ENTJ": {
        "place": "두바이, 아랍에미리트 🇦🇪",
        "style": "도전적이고 특별한 경험의 여행",
        "description": "웅장한 건축과 색다른 문화를 경험하는 특별한 여행!",
        "reason": "새로운 도전과 인상적인 경험을 좋아하는 여행자에게 어울려요. 독특한 건축물과 다양한 액티비티를 즐기며 여행의 목표를 채워보세요.",
        "activities": ["랜드마크 관람", "사막 투어", "현대 건축 탐방"],
        "color": "#F5E4D5",
    },
}

# ----------------------------
# 화면
# ----------------------------
st.markdown("""
<div class="hero">
    <div class="hero-emoji">✈️ 🧳 🌷</div>
    <div class="pill">TRIP, MY TYPE!</div>
    <h1>나의 여행 취향 찾기</h1>
    <p>MBTI를 선택하고 나만의 여행지를 추천받아보세요 ♡</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("### 🌸 어떤 여행을 떠나고 싶나요?")

mbti = st.selectbox(
    "나의 MBTI를 선택해주세요",
    list(travel_data.keys()),
    index=None,
    placeholder="MBTI를 골라주세요 ♡",
)

if mbti:
    st.markdown(
        f'<div class="result-card">'
        f'<div class="result-subtitle">YOUR TRAVEL MATCH</div>'
        f'<div class="result-title">{mbti}에게 추천하는 여행지</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    data = travel_data[mbti]

    st.markdown(
        f'<div class="result-card">'
        f'<div style="font-size: 4rem; text-align: center;">🌷</div>'
        f'<div class="result-title" style="text-align: center;">{data["place"]}</div>'
        f'<p style="text-align: center; color: #a47c91;">{data["style"]}</p>'
        f'<div class="reason">{data["description"]}<br><br>'
        f'<b>왜 어울릴까요?</b><br>{data["reason"]}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.write("")
    st.markdown("### 🎀 추천 여행 활동")

    for activity in data["activities"]:
        st.markdown(
            f'<div style="background:#fff; border:1px solid #f7dce8; '
            f'border-radius:14px; padding:12px 16px; margin:8px 0; '
            f'color:#76576a;">♡ {activity}</div>',
            unsafe_allow_html=True
        )

    st.write("")
    if st.button("다른 MBTI로 다시 추천받기 ♡"):
        st.rerun()

else:
    st.info("위에서 MBTI를 선택하면 여행지 추천이 나타나요! 🌷")

st.markdown(
    '<div class="footer">made with love ♡ · MBTI Travel Recommendation</div>',
    unsafe_allow_html=True
)
