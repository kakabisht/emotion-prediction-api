# Our api for resume filter.

This repository contains deep learning algorithm used to predict sentiment of a person using text.

1. Find saved keras model as model_text_analysis folder and label encoder in pickle file.
2. To deploy create environment on server and depoy using app.py .
3. Make sure server size to more than 650 mb to succesfully deploy api or deploy locally in conda environment.

### We used Flask framework, to create an API from our Model by using Model.pickle file in our code.

To run and test our application ,

1. pip install -r requirements.txt (to install all required libraries)
2. run python app.py (This is now the server)
3. You could either use postman or test.py to send data, just remember to change the content in test.py
