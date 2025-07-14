# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 11:55:53 2025

@author: Satish Narasimhan
This will help assess a matches for a job description against a set of resumes 
and vice versa (i.e. matches for a resume against a set of roles)
The functions defined here help assess the match
"""

import io
# Resume in the format .pdf
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

from nltk.corpus import stopwords
set(stopwords.words('english'))

# Vector functions and Cosine Similarity for match analysis from scikit-learn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_pdf_resume(pdf_doc):
    resource_manager = PDFResourceManager()
    file_handle = io.StringIO()
    converter = TextConverter(resource_manager, file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    
    with open(pdf_doc, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            
        text = file_handle.getvalue()
    
    # Close open handles as good practice
    converter.close()
    file_handle.close()
    
    if text:
        return text
   
   

def get_percentage_match(text):
    cv = CountVectorizer(stop_words='english')
    count_matrix = cv.fit_transform(text)

    #Print the match percentage
    print("Match Percentage:")
    
    #Obtain percentage match
    percentage_match = cosine_similarity(count_matrix)[0][1] * 100
    percentage_match = round(percentage_match, 2)
    print("This CV matches about "+ str(percentage_match)+ "%  of the ask.")
    print("=======================================================\n")
