from flask import Flask
from sql import *


app_education = Flask(__name__)


# HOME PAGE

@app_education.route('/')

def __init__(self, Identity_person, Educational_level, Course, Institution, Year_of_course_completion, English_language):
    
    self.Identity_person = Identity_person
    self.Educational_level = Educational_level
    self.Course = Course
    self.Institution = Institution
    self.Year_of_course_completion = Year_of_course_completion
    self.English_language = English_language


# MECHANISM TO SAVE EDUCATIONAL INFORMATIONS

@app_education.route('/saveeducation')

def Save_Sql(Identity_person, Educational_level, Course, Institution, Year_of_course_completion, English_language):
    
    concept2 = "Eligible" if Educational_level != "Associates" and English_language == "YES" else "No"
    values2 = ["DEFAULT, '{0}', '{1}', '{2}', '{3}', {4}, '{5}', '{6}'".format(Identity_person, Educational_level, Course, Institution, Year_of_course_completion, English_language, concept2)]
    insert_data(values2, "education")


if __name__ == '__main__':
    
    app_education.run(debug=True)