import json

juniors={
    "classmates": [
        {
            "name": "Debora",
            "age": 29,
            "time_studied": 0
        },
        {
            "name": "Paulo",
            "age": 34,
            "time_studied": 10
        }
    ]
}   

print(type(juniors))


def work_on_this_dict():
    #this dictonary is like a tree. Its made of branches. In this example the dictionary called juniors has inside the classmates,
    #which has 2 elements, two students
    
    #if we print this we ll get classmates on the output and not the students since classmates is an array of 2 students and its
    #the first key of the dictionary
    for student in juniors:
        print(student)
    # Output: classmates
        
    #To get the students we need to first get inside the classmates. Again, like a tree we are going to the branch classmates and
    #see the smaller branches that are there
    #If juniors where a tree this would be the structure:    
    
    #       Debora Paulo
    #         \     /
    #           \ /
    #            |
    #        classmates
    #            |
    #         juniors
    
    #To get the sudents data from the dict we'll then get inside of the branch classmates:
    for student in juniors["classmates"]:
        print(student)
    # Output: {'name': 'Debora', 'age': 29, 'time_studied': 0}
    #         {'name': 'Paulo', 'age': 34, 'time_studied': 10}
    
    #If we just want to get their names. We'll use an auxiliar variable. The aux variable has the array of the two students
    #each one with 3 keys: name, age, time_studied. So we can loop in there and print just the name
    aux=juniors["classmates"]
    print(aux)
    
    counter=0
    for i in aux:
        counter+=1
        print('Student number', counter,'is:', i['name'])
        
    # Output: Student number 1 is: Debora
    #         Student number 1 is: Paulo
    
    #We can create a loop with a condition iside of it. For example we'll return only the students name that started studying python:
    for i in aux:
        if i['time_studied'] > 0:
            print('Student', i["name"], 'has started studying python')
    
    #Dictionarys can be more complicated
    
    
work_on_this_dict()