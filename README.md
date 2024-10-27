#Overview
The Resume Classifier is a web application built with Django that utilizes a trained neural network model to classify resumes based on their content. Users can upload their PDF resumes, and the model predicts the appropriate category for each resume. This application aims to streamline the resume screening process for recruiters by automating the classification of resumes.

#Features
File Upload: Users can upload resumes in PDF format.
Text Extraction: The application extracts text from the uploaded PDF files using the PyPDF2 library.
Machine Learning Model: The application uses a trained Recurrent Neural Network (RNN) model to classify resumes based on their content.
User Interface: A simple and intuitive HTML frontend for user interaction.
Technologies Used
Backend: Django
Machine Learning: TensorFlow, Keras
Frontend: HTML, JavaScript
PDF Handling: PyPDF2 for text extraction from PDF files
