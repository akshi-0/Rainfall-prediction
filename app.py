import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('news_dataset_rss_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# ---- Custom Styling ----
st.set_page_config(page_title="News Classifier", page_icon="🗞️")

st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextArea, .stButton {
        font-size: 16px;
    }
    .prediction-box {
        padding: 1rem;
        margin-top: 20px;
        background-color: #000000;
        border-left: 5px solid #00796b;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
    }
    .title-style {
        font-size: 40px;
        color: #0d47a1;
    }
    .subtitle-style {
        font-size: 18px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# ---- App Title ----
st.markdown('<h1 class="title-style">📰 News Category Classifier</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-style">Paste any news headline or article snippet below and the model will tell you what category it belongs to (e.g., Sports 🏏, Politics 🗳️, Tech 💻).</p>', unsafe_allow_html=True)

# ---- Input Text ----
user_input = st.text_area("📝 Enter News Text:", height=150, placeholder="e.g. The government unveiled its new tech policy today...")

# ---- Predict Button ----
if st.button("🔍 Classify News"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some news text before classifying.")
    else:
        # Vectorize and predict
        vectorized_text = vectorizer.transform([user_input])
        prediction = model.predict(vectorized_text)[0]

        # Emoji-enhanced category display
        emoji_map = {
            "Politics": "🗳️",
            "Sports": "🏅",
            "Business": "💼",
            "Technology": "💻",
            "Entertainment": "🎬",
            "Health": "🩺"
        }
        emoji = emoji_map.get(prediction, "📰")

        # ---- Display Result ----
        st.markdown(f"""
        <div class="prediction-box">
            Predicted Category: {emoji} <span style="color:#00796b">{prediction}</span>
        </div>
        """, unsafe_allow_html=True)
