# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Machine Learning**, **Streamlit**, and **TMDB API**.  
The app recommends movies similar to the selected one and displays their posters in real time.

---

## 🚀 Live Demo
👉 https://movie-recommendation-system-sdboog33ck7c98fzjntwpy.streamlit.app/

---

## 📌 Features
- Content-based movie recommendations
- Cosine similarity using CountVectorizer
- Real-time poster fetching via TMDB API
- Clean and interactive Streamlit UI
- Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Pandas & NumPy
- Scikit-learn
- TMDB API
- Git & GitHub

---

## ⚙️ How It Works
1. Movie metadata is processed and combined into tags
2. Text is vectorized using CountVectorizer
3. Cosine similarity is computed between movies
4. On selection, top 5 similar movies are recommended
5. Posters are fetched using TMDB API

---

## 🖥️ Installation (Local Setup)

```bash
git clone https://github.com/AKSHITOMAR/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
streamlit run app.py


