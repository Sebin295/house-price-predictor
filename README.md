# 🏠 House Price Predictor — ML + Flask API

An end-to-end machine learning project that predicts residential 
property prices using a trained regression model served via a REST 
API and a polished web interface.

## 🚀 Live Demo
file:///C:/Users/sebin/Desktop/house-price-predictor/templates/index.html

## 🧠 Model Details
- Algorithm: Random Forest Regressor
- Dataset: Ames Housing Dataset (1,460 records)
- Features: 41 engineered features
- Accuracy: ~96% R² Score

## 🔌 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /predict | Single price prediction |
| POST | /predict-range | Low / Mid / High range |
| GET | /feature-importance | Top 10 price drivers |
| GET | /apidocs | Swagger API documentation |

## 🛠️ Tech Stack
Python · Scikit-learn · Flask · REST API · HTML · CSS · 
JavaScript · Docker · Swagger · Pandas · NumPy · Git

## ⚙️ Run Locally
git clone https://github.com/YOUR_USERNAME/house-price-predictor
cd house-price-predictor
pip install -r requirements.txt
python app.py
Then open http://localhost:5000 in your browser.

## 📸 Screenshot
![alt text](<Screenshot 2026-07-05 015410.png>)
![alt text](<Screenshot 2026-07-05 015429.png>)
![alt text](<Screenshot 2026-07-05 015445.png>)