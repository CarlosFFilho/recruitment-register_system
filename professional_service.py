from flask import Flask
from sql import *


app_professional = Flask(__name__)


# HOME PAGE

@app_professional.route('/')

def __init__(self, Identity_person, Chemical_industry_years, Last_position, Performed_activities):
    
    self.Identity_person = Identity_person
    self.Chemical_industry_years = Chemical_industry_years
    self.Last_position = Last_position
    self.Performed_activities = Performed_activities


# MECHANISM TO SAVE PROFESSIONAL INFORMATIONS

@app_professional.route('/saveprofessional')

def Save_Sql(Identity_person, Chemical_industry_years, Last_position, Performed_activities):
    
    Chemical_industry_years = float(Chemical_industry_years)
    concept4 = "Eligible" if Chemical_industry_years >= 3 else "No"
    values4 = ["DEFAULT, '{0}', {1}, '{2}', '{3}', '{4}'".format(Identity_person, Chemical_industry_years, Last_position, Performed_activities, concept4)]
    insert_data(values4, "professional_experience")


if __name__ == '__main__':
    
    app_professional.run(debug=True)