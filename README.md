# 🎬 Movie Recommendation System

A **content-based movie recommendation system** that suggests similar movies using **TF-IDF vectorization** and **cosine similarity**.  
It’s lightweight, easy to understand, and built completely in Python using **Scikit-learn** and **Streamlit**.

---

## 🚀 Features

- Suggests similar movies based on description, cast, crew, and genres  
- Built using TF-IDF + Nearest Neighbors  
- Simple Streamlit web interface  
- Modular design — easy to retrain with new data

---

## 🧠 Tech Stack

- **Python 3.10+**
- **Pandas**
- **Scikit-learn**
- **Streamlit**
- **Pickle** (for saving models)

---

## 📂 Project Structure

├── app.py # Streamlit app
├── main.ipynb # Model building and preprocessing notebook [will be updated soon]
├── movies.pkl # Processed movie dataset [not provided here]
├── tfidf.pkl # TF-IDF vectorizer [not provided]
├── similarity.pkl # NearestNeighbors model [not provided]
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
##Create and Activate Virtual Environment
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
##Install Dependencies
pip install -r requirements.txt
##run app
streamlit run app.py
```
## How to train your own model?

1. Follow the notebook file

## 🧾 License

This project is open-source and free to use for educational or personal projects.

