import json
import boto3
import random
import datetime
import numpy as np
import uuid
import numpy as np
from faker import Faker

fake = Faker()

roles_list = [
    "Software Engineer",
    "Data Scientist",
    "UX Designer",
    "Graphic Designer",
    "Web Developer",
    "Technical Writer",
    "Sales Representative",
    "Customer Support",
    "Manager",
    "HR Generalist",
    "Recruiter",
    "Recruiting Coordinator",
    "HR Business Partner",
    "Payroll Specialist"
]

roles_dictionary = {
    "Software Engineer" : {
        "salary" : { 
            "min": 97000, 
            "max": 160000 
        },
        "role_type" : "tech",
        "average_age" : { 
            "min": 20, 
            "max": 60
        }
    },
    "Data Scientist" : {
        "salary" : {
            "min" : 92000,
            "max" : 180000
        },
        "role_type" : "tech",
        "average_age" : { 
            "min": 28, 
            "max": 55
        }
    },
    "UX Designer" : {
        "salary" : {
            "min" : 80000,
            "max" : 125000
        },
        "role_type" : "tech",
        "average_age" : { 
            "min": 18, 
            "max": 35
        }
    },
    "Graphic Designer" : {
        "salary" : {
            "min" : 50000,
            "max" : 75000
        },
        "role_type" : "tech",
        "average_age" : { 
            "min": 20, 
            "max": 40
        }
    },
    "Web Developer" : {
        "salary" : {
            "min" : 75000,
            "max" : 105000
        },
        "role_type" : "tech",
        "average_age" : { 
            "min": 16, 
            "max": 42
        }
    },
    "Technical Writer" : {
        "salary" : {
            "min" : 65000,
            "max" : 90000
        },
        "role_type" : "business",
        "average_age" : { 
            "min": 20, 
            "max": 60
        }
    },
    "Sales Representative" : {
        "salary" : {
            "min" : 60000,
            "max" : 100000
        },
        "role_type" : "business",
        "average_age" : { 
            "min": 20, 
            "max": 65
        }
    },
    "Customer Support" : {
        "salary" : {
            "min" : 38000,
            "max" : 52000
        },
        "role_type" : "business",
        "average_age" : { 
            "min": 16, 
            "max": 50
        }
    },
    "Manager" : {
        "salary" : {
            "min" : 115000,
            "max" : 230000
        },
        "role_type" : "business",
        "average_age" : { 
            "min": 35, 
            "max": 65
        }
    },
    "HR Generalist" : {
        "salary" : {
            "min" : 60000,
            "max" : 85000
        },
        "role_type" : "HR",
        "average_age" : { 
            "min": 30, 
            "max": 65
        }
    },
    "Recruiter" : {
        "salary" : {
            "min" : 50000,
            "max" : 75000
        },
        "role_type" : "HR",
        "average_age" : { 
            "min": 20, 
            "max": 65
        }
    },
    "Recruiting Coordinator" : {
        "salary" : {
            "min" : 45000,
            "max" : 60000
        },
        "role_type" : "HR",
        "average_age" : { 
            "min": 20, 
            "max": 35
        }
    },
    "HR Business Partner" : {
        "salary" : {
            "min" : 64000,
            "max" : 125000
        },
        "role_type" : "HR",
        "average_age" : { 
            "min": 30, 
            "max": 65
        }
    },
    "Payroll Specialist" : {
        "salary" : {
            "min" : 46000,
            "max" : 60000
        },
        "role_type" : "HR",
        "average_age" : { 
            "min": 20, 
            "max": 65
        }
    }
}

class Employee():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        address = fake.address() #street_address\ncity, STATE_CODE ZIP_CODE

        self.street_address = fake.street_address()
        self.city = fake.city()
        self.state_code = address.split(" ")[-2]
        self.zip_code = address.split(" ")[-1]
        
        self.role = roles_list[random.randint(0, len(roles_list)-1)]
        self.role_type = roles_dictionary[self.role]['role_type']
        
        min_salary = roles_dictionary[self.role]['salary']['min']
        max_salary = roles_dictionary[self.role]['salary']['max']
        self.salary = random.randint(min_salary, max_salary)
        
        min_age = roles_dictionary[self.role]['average_age']['min']
        max_age = roles_dictionary[self.role]['average_age']['max']
        self.age = random.randint(min_age, max_age)
        
        self.current_employee = random.choices([True, False], weights=(70,30), k=1)
        self.years = round(np.random.normal(loc=8, scale=2),2)
        if self.years <= 0:
            self.years = 1
        if self.age - self.years > 20: # meaning they started working here before they were 20
            self.years = 2
            
            
        ## TODO: Add fields for things like benefits, 401k, email address, ssn, and other things that may be relevant
        ## TODO: Add missing values and mistakes to allow for data cleaning and preparation practice
        
        self.benefit_401k = random.choices([True, False], weights=(70,30), k=1)
        self.benefit_401k_contribution = round(np.random.normal(loc=10, scale=2),1)
        if self.benefit_401k_contribution < 0 or self.benefit_401k_contribution > 100:
            self.benefit_401k_contribution = 10
        
        self.benefit_dental = random.choices([True, False], weights=(85,15), k=1)
        self.benefit_vision = random.choices([True, False], weights=(30,70), k=1)
        self.benefit_medical = random.choices([True, False], weights=(90,10), k=1)
        
        self.miles_to_work = round(np.random.normal(loc=10, scale=5),1)
        if self.miles_to_work <= 0:
            self.miles_to_work = 5
            
        self.remote_employee = random.choices([True, False], weights=(35,65), k=1)
        
        self.entry = {
            "Employee_ID" : self.id,
            "First_Name" : self.first_name,
            "Last_Name" : self.last_name,
            "Street_Address" : self.street_address,
            "City": self.city,
            "State_Code": self.state_code,
            "Zip_Code": self.zip_code,
            "Role" : self.role,
            "Role_Type": self.role_type,
            "Salary": self.salary,
            "Age" : self.age,
            "Years_at_Company": self.years,
            "Benefit_401k": self.benefit_401k,
            "Contribution_401k": self.benefit_401k_contribution,
            "Benefit_Dental": self.benefit_dental,
            "Benefit_Vision": self.benefit_vision,
            "Benefit_Medical": self.benefit_medical,
            "Miles_to_Work": self.miles_to_work,
            "Remote_Employee": self.remote_employee,
            "Current_Employee" : self.current_employee
        }
        
        return
    
    def to_string(self):
        
        print(json.dumps(self.entry, indent=4, default=str))
        
        return