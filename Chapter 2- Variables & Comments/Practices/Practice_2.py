#course marks calcu
courses = int(input("Number of courses: "))

grades = 0 #dot fail like this :(

#asking for your score in a course
for mark in range(courses):
    mark = float(input("Marks acquired for this course: "))
    grades += mark

total_marks = 100 

average = grades / courses #calculating average

percent = average / total_marks * 100 #calculating percentage 

print ("Grades Announcement!!") #Dudun Announcememnt!!
print (f"Average: {average}")
print (f"Percentage: {percent}")

