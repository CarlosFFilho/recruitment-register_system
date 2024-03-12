# IMPORTANDO ARQUIVO DOS MECANISMOS DO MYSQL

from sql import *

# CLASSES

class Person:

    def __init__(self, Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class):
        self.Name = Name
        self.Identity = Identity
        self.Type_identity = Type_identity
        self.Phone_number = Phone_number
        self.Email_address = Email_address
        self.Driving_licence = Driving_licence
        self.Driving_licence_class = Driving_licence_class

    @staticmethod
    def Save_Sql(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class):
        concept = "Eligible" if Driving_licence == "YES" and Driving_licence_class == "B" else "No"
        values1 = ["DEFAULT, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}'".format(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class, concept)]
        insert_data(values1, "person")
    
class Education(Person):

    def __init__(self, Identity_person, Educational_level, Course, Institution, Year_of_course_completion, English_language):
        self.Identity_person = Identity
        self.Educational_level = Educational_level
        self.Course = Course
        self.Institution = Institution
        self.Year_of_course_completion = Year_of_course_completion
        self.English_language = English_language

    @staticmethod
    def Save_Sql(Identity_person, Educational_level, Course, Institution, Year_of_course_completion, English_language):
        concept2 = "Eligible" if Educational_level != "Associates" and English_language == "YES" else "No"
        values2 = ["DEFAULT, '{0}', '{1}', '{2}', '{3}', {4}, '{5}', '{6}'".format(Identity_person, Educational_level, Course, Institution, Year_of_course_completion, English_language, concept2)]
        insert_data(values2, "education")

class Address(Person):

    def __init__(self, Identity_person, Street, City, State, Postal_code, Country, Avaliable_for_change):
        self.Identity_person = Identity
        self.Street = Street
        self.City = City
        self.State = State
        self.Postal_code = Postal_code
        self.Country = Country
        self.Avaliable_for_change = Avaliable_for_change
    
    @staticmethod
    def Save_Sql(Identity_person, Street, City, State, Postal_code, Country, Avaliable_for_change):
        concept3 = "Eligible" if State == "Alagoas" or Avaliable_for_change == "YES" else "No"
        values3 = ["DEFAULT, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}'".format(Identity_person, Street, City, State, Postal_code, Country, Avaliable_for_change, concept3)]
        insert_data(values3, "address")

class ProfessionalExperience(Person):
    
    def __init__(self, Identity_person, Chemical_industry_years, Last_position, Performed_activities):
        self.Identity_person = Identity
        self.Chemical_industry_years = Chemical_industry_years
        self.Last_position = Last_position
        self.Performed_activities = Performed_activities
    
    @staticmethod
    def Save_Sql(Identity_person, Chemical_industry_years, Last_position, Performed_activities):
        Chemical_industry_years = float(Chemical_industry_years)
        concept4 = "Eligible" if Chemical_industry_years >= 3 else "No"
        values4 = ["DEFAULT, '{0}', {1}, '{2}', '{3}', '{4}'".format(Identity_person, Chemical_industry_years, Last_position, Performed_activities, concept4)]
        insert_data(values4, "professional_experience")

# ALIMENTAÇÃO INICIAL DE DADOS (Serão substituídos pelos dados inseridos mediante a execução do código)    

Name = "Fulano"
Identity = "12345678912"
Type_identity = "CPF"
Phone_number = "000000000"
Email_address = "fulano_mail"
Driving_licence = "YES"
Driving_licence_class = "B"
Educational_level = "level"
Course = "Course"
Institution = "Institution"
Year_of_course_completion = "2000"
English_language = "YES"
Street = "Street a"
City = "City"
State = "State"
Postal_code = "00000000"
Country = "Country"
Avaliable_for_change = "YES"
Chemical_industry_years = 5
Last_position = "Position"
Performed_activities = "aaaaaaaaa"