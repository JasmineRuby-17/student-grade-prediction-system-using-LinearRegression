

https://github.com/user-attachments/assets/fc5d3444-5c5b-419d-adbd-630130d1bd71


# 🎓 Student Grade Prediction System 🚀

A machine learning project that predicts students’ final grades (G3) using academic and behavioral factors.

## 📌 Overview
This project uses Linear Regression to predict student performance based on:

📘 G1 – First Grade  
📘 G2 – Second Grade  
📚 Study Time (1–4)  
🚫 Absences  

It demonstrates a complete end-to-end ML workflow from preprocessing to deployment.


## ⚙️ Features
✔ Data preprocessing & feature selection  
✔ Linear Regression model  
✔ Evaluation using MAE & RMSE  
✔ Interactive UI (CLI + Streamlit)  
✔ Real-time grade prediction  
✔ Performance insights (Excellent / Good / Average / Needs Improvement)

## 🧠 Workflow
1. Data preprocessing (cleaning + encoding)  
2. Feature selection (G1, G2, studytime, absences)  
3. Train-test split (80/20)  
4. Model training (Linear Regression)  
5. Evaluation (MAE, RMSE)  
6. Model saving using `pickle`  
7. Deployment using Streamlit  

## 📊 Input & Output

| Input Feature | Range |
|--------------|------|
| G1, G2       | 0 – 20 |
| Study Time   | 1 – 4 |
| Absences     | 0 – 100 |

🎯 Output: Predicted Final Grade (G3)

## 💻 Tech Stack
Python • Pandas • NumPy • Scikit-learn • Streamlit

## ▶️ Run Locally
git clone https://github.com/your-username/student-grade-prediction.git

cd student-grade-prediction

python gradeprediction.py (file name)
