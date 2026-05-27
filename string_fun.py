courses=[ "history","math","science","compsci"]
courses2=["hindi", "english"]
courses.append("art") #print or add in the back

courses.insert(0,"art") #print in front
courses.insert(0,courses2)
courses.extend( courses2) #add inwithout bracket
courses.remove("math")




print (courses)

print(courses[0])     #1st place or 0th places

print(courses[2:])