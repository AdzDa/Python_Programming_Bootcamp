""""
Problem 2: Friends, Colleagues, and Details
    Dictionaries, lists, and key-value pairs.

    Your boss tasks you with creating a company directory. Make a list called "employees", which will
    contain one dictionary per person and include the keys "name", "age", "department", "phone", and "salary".
    Once you have the list of dictionaries set up, loop through the list and print out the "name",
    "department", and "phone" number of each employee. Their "age" and "salary" should remain secret!

    Expected Output:
        Ron Swanson in Management can be reached at 555-1234.
        Leslie Knope in Middle Management can be reached at 555-4321.
        Andy Dwyer in Shoe Shining can be reached at 555-1122.
        April Ludgate in Administration can be reached at 555-3345.
"""

#Nested Dictionary
#to retrieved data(eg.): employee["1"]["name"]
employees = {
    "employeee_1" : {  
            "name": "Ron Swanson",
            "age": 55,
            "department": "Management",
            "phone": "555-1234",
            "salary": ",000"  
    },

    "employeee_2" : {
            "name": "Leslie Knope",
            "age": 40,
            "department": "Middle Management",
            "phone": "555-4321",
            "salary": ",000"
    },

    "employeee_3" : {
            "name": "Andy Dwyer",
            "age": 28,
            "department": "Shoe Shining",
            "phone": "555-1122",
            "salary": ",000"
    },

    "employeee_4" : {
            "name": "April Ludgate",
            "age": 35,
            "department": "Administration",
            "phone": "555-3345",
            "salary": ",000"
    }
}

#loops to print desired output
for key in employees:
    print(employees[key]["name"], "in", employees[key]["department"], "can be reached at", employees[key]["phone"])

