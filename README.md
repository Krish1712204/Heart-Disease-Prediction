# Heart Disease Classification Web App 🩺

![heart Disease](https://github.com/user-attachments/assets/ec467e06-a893-4ad6-8339-c152f5dbb01a)


This project is a web-based application built using **Streamlit** that classifies the likelihood of heart disease based on medical parameters. It takes user inputs such as age, cholesterol levels, chest pain type, and other health indicators to predict whether the person is likely to have heart disease or not.

## Features

- User-friendly web interface to input medical report details.
- Predicts whether a person is at risk of heart disease.
- Uses pre-trained machine learning model for classification.

## How It Works

1. The user inputs their medical report details, such as age, sex, chest pain type, blood pressure, cholesterol, heart rate, and other relevant features.
2. The app scales the inputs using a pre-trained scaler and uses a machine-learning model to predict whether the person has heart disease.
3. Based on the input, the app displays whether the user is fit or needs treatment.

## Model

- The app uses a pre-trained classification model stored in a `.pkl` file.
- It also uses a pre-trained scaler to normalize the input features before prediction.

## Installation and Usage

1. Clone the repository:

```bash
git clone "https://github.com/gokulraktate/Heart-Disease-Prediction.git"
```

2. Navigate to the project directory:

```bash
cd heart-disease-classification
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Place the pre-trained model files (`Model.pkl` and `scaler.pkl`) in the `./models/` directory.

5. Run the Streamlit app:

```bash
streamlit run app.py
```

6. Open your browser and go to `http://localhost:8501` to access the app.

Optional way -->
---

1. Download the files and extract them.
2. Open the terminal or anaconda prompt at the same location and fulfill the required library in a particular environment.
3. Type "streamlit run app.py" in that terminal.
4. A web page will open to enter details.
5. Enter the value of the specified parameters.
6. Click on the predict button to generate results.   

## Input Parameters

The following inputs are required for prediction:

- **Age**: Age of the patient.
- **Sex**: Gender (0 for Female, 1 for Male).
- **Chest Pain Type**:
  - 1: Typical angina
  - 2: Atypical angina
  - 3: Non-anginal pain
  - 4: Asymptomatic
- **Resting Blood Pressure (trestbps)**: Blood pressure level (in mm Hg).
- **Cholesterol (chol)**: Serum cholesterol level (in mg/dl).
- **Resting ECG (restecg)**:
  - 0: Normal
  - 1: ST-T wave abnormality or Left Ventricular Hypertrophy (enlarged heart)
- **Max Heart Rate Achieved (thalach)**: Maximum heart rate achieved during exercise.
- **Exercise-Induced Angina (exang)**:
  - 0: No
  - 1: Yes
- **Oldpeak**: Depression induced by exercise relative to rest.
- **Slope of the Peak Exercise ST Segment (slope)**:
  - 1: Upsloping
  - 2: Flat
  - 3: Downsloping
- **Number of Major Vessels (ca)**: Number of coronary arteries with significant stenosis.
- **Thalassemia (thal)**:
  - 1: Normal
  - 2: Fixed defect
  - 3: Reversible defect

## Project Structure

```bash
.
├── app.py                  # Main Streamlit app script
├── models/
│   ├── Model.pkl           # Pre-trained heart disease classification model
│   └── scaler.pkl          # Pre-trained scaler for input normalization
├── modules/
│   └── heartDisease.ipynb  # Python file for selection of model
├── requirements.txt        # List of required Python packages
└── README.md               # Project documentation
```

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Scikit-learn
- Pickle

You can install the necessary dependencies using the `requirements.txt` file provided in the repository.

## Acknowledgements

- The dataset used to train the model is from [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease).
- Scikit-learn is used for building and training the model.
- Streamlit is used for the web interface.

## License

This project is licensed under the MIT License.

---


Upvote, Share and follow for more⬆️⬆️⬆️🔝.


Made with ❤️ by Gokul
