# FAKE-NEWS-DETECTOR
This project detects whether a news headline is REAL or FAKE using Machine Learning. The model is trained on a dataset of news headlines and uses text processing techniques to classify the news.

## Technologies Used
- Python  
- Streamlit  
- Scikit-learn  
- Pandas  
- TF-IDF Vectorizer  

## How It Works
1. The dataset is loaded from a CSV file.
2. Text data is converted into numerical form using TF-IDF vectorization.
3. A Logistic Regression model is trained on the processed data.
4. The trained model predicts whether a news headline is REAL or FAKE.
5. A Streamlit web interface allows users to input news headlines and see predictions.

## Project Structure
fake-news-detector  
│  
├── app.py  
├── train_model.py  
├── news.csv  
├── model.pkl  
├── vectorizer.pkl  
└── README.md  

## How to Run the Project
1. Install required libraries
pip install streamlit pandas scikit-learn

2. Train the model
python train_model.py

3. Run the web app
streamlit run app.py

## Features
- Machine learning based news classification
- Simple user interface
- Real-time prediction of news headlines

## Future Improvements
- Use a larger dataset
- Improve model accuracy
- Add news article classification instead of only headlines

## Author
Your Name
