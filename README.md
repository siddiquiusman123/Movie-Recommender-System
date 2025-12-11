# 🎬 Movie Recommender System

This project recommends **movies similar to a selected movie** using Machine Learning and Natural Language Processing (NLP).  
It is deployed as an interactive **Streamlit web application**, where users can choose a movie and instantly get top recommendations.

---

## 📌 Features
- Uses **TMDB Movies Dataset** (metadata: genres, cast, crew, keywords, overview)
- Creates a combined "tags" column for NLP processing
- Generates a **cosine similarity matrix** for accurate recommendations
- Simple & fast **Streamlit UI** for selecting movies
- Preprocessed dataset stored as `movies_dict.pkl` and `similarity.pkl`

---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- scikit-learn  
- NLTK  
- Streamlit  
- Joblib  

---

## 🌐 Live Demo
🔗 Click here to try the app  
👉 *Add your Streamlit link here after deployment*

---

## 🎯 How It Works
- All important textual movie fields (genres, keywords, cast, crew, overview) are combined  
- Text is cleaned, tokenized, and stemmed  
- Converted into vectors using **TF-IDF Vectorization**  
- Similarity between movies calculated using **Cosine Similarity**  
- Recommender returns the **top 5 most similar movies**  

---


