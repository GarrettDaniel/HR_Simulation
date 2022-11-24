import json
import boto3
import random
import datetime
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
        self.address = fake.address()
        
        self.role = roles_list[random.randint(0, len(roles_list)-1)]
        self.role_type = roles_dictionary[self.role]['role_type']
        
        min_salary = roles_dictionary[self.role]['salary']['min']
        max_salary = roles_dictionary[self.role]['salary']['max']
        self.salary = random.randint(min_salary, max_salary)
        
        min_age = roles_dictionary[self.role]['average_age']['min']
        max_age = roles_dictionary[self.role]['average_age']['max']
        self.age = random.randint(min_age, max_age)
        
        self.current_employee = random.choices([True, False], weights=(70,30), k=1)
        
        self.entry = {
            "Employee_ID" : self.id,
            "First_Name" : self.first_name,
            "Last_Name" : self.last_name,
            "Address" : self.address,
            "Age" : self.age,
            "Role" : self.role,
            "Current_Employee" : self.current_employee
        }
        
        return
    
    def to_string(self):
        
        print(json.dumps(self.entry, indent=4, default=str))
        
        return