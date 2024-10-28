#student_scores = {'Tom' : 85 , 'Serena' : 92, 'Alex' : 78,'Nina':88}

#for student,score in student_scores.items():
#    print(f"{student} recived score : {score}")

book_ratings = {"Moby-Dick" : 8 , "The Great Gatsby" : 9,"War and Peace" : 10,"The Catcher in the Rye": 8}
print(book_ratings["The Great Gatsby"])
print(book_ratings.get("Moby- Dick",0))
print(book_ratings)
del book_ratings["Moby-Dick"]
print(book_ratings)

spacemail = {}

# Let's populate with incoming messages
spacemail['Station Alpha'] = 'Supply request: cosmic fuel'
spacemail['Station Beta'] = 'Engineering report: engines operational'
spacemail['Station Gamma'] = 'Medical report: crew status healthy'

# Let's print the initial spacemail log
print("Initial Spacemail Log:")
for station, message in spacemail.items():
    print(f"Station: {station}, Message: {message}")

# TODO: Add a new message from Station Delta and verify the updated spacemail log
spacemail["Station Delta"] = 'Machine Report: Working status'