# Student Performance Predictor 

This project is an **end-to-end Machine Learning application** that predicts a student’s academic performance based on multiple input features.  

It is built with **Python, Flask, Scikit-learn, and Streamlit** for development and deployed using **AWS Elastic Beanstalk**.  

---

##  Project Overview  

- **Goal**: Predict student performance (e.g., marks or grade) from input data.  
- **Tech Stack**:  
  - Python  
  - Pandas, NumPy (Data Handling)  
  - Scikit-learn (Model Training)  
  - Matplotlib/Seaborn (Visualization)  
  - Flask (Backend API)  
  - Streamlit (Interactive Interface)  
  - AWS Elastic Beanstalk (Deployment)  

---

##  Project Structure  

capstoneml/
│── .ebextensions/        # AWS Elastic Beanstalk configs
│── .github/workflows/    # GitHub Actions for CI/CD
│── .vscode/              # VS Code settings
│── artifacts/            # Trained models, transformers, and metadata
│── catboost_info/        # CatBoost training logs and info
│── notebook/             # Jupyter notebooks (EDA, experiments, ingestion)
│── src/                  # Source code: pipelines, training, prediction
│── static/               # Static files (CSS, JS, assets for Flask app)
│── templates/            # HTML templates for Flask frontend
│── app.py                # Flask application entrypoint
│── requirements.txt      # Dependencies
│── runtime.txt           # Runtime environment (for Azure deployment)
│── setup.py              # Package setup file
│── README.md             # Project documentation
│── .gitignore            # Git ignore rules



---

## Installation & Usage  

### Clone the repository  
```bash
git clone https://github.com/riaatiwarii/capstoneml.git
cd capstoneml

### Create virtual enviroment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### Install dependencies 
pip install -r requirements.txt

### Run locally
python app.py

# The app will be available at:
# http://127.0.0.1:5000/predict

```
 ## Deployment

This project was deployed using:

AWS Elastic Beanstalk → http://stuper.us-east-1.elasticbeanstalk.com/predict

Azure App Service (via GitHub Actions workflow)

 Note: The AWS link is no longer active because the AWS account was deleted to avoid billing charges.
