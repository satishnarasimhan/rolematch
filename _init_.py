# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 11:55:53 2025

@author: Satish Narasimhan
This will help assess a matches for a job description against a set of resumes 
and vice versa (i.e. matches for a resume against a set of roles)
"""
import rolematch as r
import glob
from pathlib import Path

if __name__ == '__main__':

    file_path = Path.cwd()
    print("Current Working Directory:", file_path)
    print("Choose: 1 if you want ascertain the match against a resume\n")
    
    print("Choose: 2 if you want ascertain the match against a job description\n")

    choice = input ("Enter you choice :")
    if choice == '1':
    # Save your resume in the current working directory i.e. where this .py file is located, and enter the name e.g. SN.pdf
    # Store resume files as .pdf
        resume = r.read_pdf_resume('SN.pdf')
        
        try:
            for fp in glob.glob('*.txt'):
                with open(fp, 'r', encoding='utf-8') as file:
                    job_description = file.read()
                    print(fp)
                
                text = [resume, job_description]
                r.get_percentage_match(text)
        except FileNotFoundError:
            print("Error: Input file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        # Save your job description in the current working directory i.e. where this .py file is located, and enter the name e.g. JD.txt
        jd_txt = open('JD.txt')
        job_description = jd_txt.read()
        for pdf_file_path in Path(file_path).glob("*.pdf"):
            resume = r.read_pdf_resume(pdf_file_path)
            print(pdf_file_path)

            text = [resume, job_description]
            r.get_percentage_match(text)






    