contacts = {
    "number":4,  #key:value
    "students":   
        [   # dictionary list of students details
            {"name":"Sarah Holderness", "email":"sarah@example.com"},
            {"name":"Erica Newman", "email":"erica@example.com"},
            {"name":"Crystal Jones", "email":"crystal@example.com"},
            {"name":"Irene Bowers", "email":"irene@example.com"}

        ]
}

#Print an email group
# create for loop
for student in contacts["students"]:
    print(student["email"])
    