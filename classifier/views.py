
from django.http import JsonResponse
import numpy as np
import tensorflow as tf
from django.views.decorators.csrf import csrf_exempt
import json
from pypdf import PdfReader
import os

model = tf.keras.models.load_model('path/to/your/model.h5')  

@csrf_exempt 
def predict(request):
    if request.method == 'POST':
        try:
            resume_file = request.FILES['resumeFile']
            if not resume_file.name.endswith('.pdf'):
                return JsonResponse({'error': 'File is not a PDF'}, status=400)

            # Save the file temporarily
            temp_file_path = os.path.join('temp', resume_file.name)  # Save to a temporary directory
            with open(temp_file_path, 'wb+') as destination:
                for chunk in resume_file.chunks():
                    destination.write(chunk)


            text = extract_text_from_pdf(temp_file_path)
            os.remove(temp_file_path)  
            input_data = text.split('\n')  
            input_data = np.array(input_data).reshape(1, -1)  

            predictions = model.predict(input_data)
            predicted_class = np.argmax(predictions, axis=-1).tolist()
            return JsonResponse({'prediction': predicted_class})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)
    text = "".join(page.extract_text() for page in reader.pages)
    return text
