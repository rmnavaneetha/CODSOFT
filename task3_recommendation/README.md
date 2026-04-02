# 🎬 Recommendation System (Task 4)

## 📌 Overview

This project implements a **simple Recommendation System** using **Python**.
It suggests movies to users based on their preferences using a **Content-Based Filtering** technique.

---

## 🧠 Concept

The system uses:

* **Content-Based Filtering**
* **Cosine Similarity**
* **Text Vectorization (CountVectorizer)**

It recommends movies by comparing their **genres** and finding similar ones.

---

## ⚙️ How It Works

1. A list of movies with genres is defined
2. Genres are converted into numerical vectors
3. Cosine similarity is calculated between movies
4. User inputs a movie name
5. System recommends similar movies

---

## ✨ Features

* 📥 Accepts user input
* 🎯 Recommends similar movies
* ⚡ Fast and efficient
* 🧩 Easy to understand implementation

---

## 📦 Requirements

Install dependencies using:

```bash
pip install scikit-learn
```

---

## ▶️ Usage

Run the program with:

```bash
python recommendation_system.py
```

---

## 💡 Example Output

```text
Available Movies:
Inception
Titanic
Avengers

Enter a movie name: Inception

Recommended Movies:
Interstellar
Avengers
John Wick
```

---

## 📊 Dataset

* Uses a **small in-built dataset** inside the code
* No external dataset is required

---

## 📸 Screenshots

### 🔹 Input
![Input Screenshot](images/input.png)
### 🔹 Output
![Output Screenshot](images/output.png)