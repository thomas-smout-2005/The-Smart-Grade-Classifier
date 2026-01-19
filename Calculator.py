name = ""
total = float(0)
score = ""


def naming(name):
    # Asking user for their name and  striping away accidental spaces and converting the name to Title Case
    name = input("What is your name").strip().title()
    return name

def scores(total):
    # Asking for Mini Project 1 score and round it to a full number
    score1 = float(input("What mark did you get on your mini prject 1?"))
    # Asking for Mini Project 2 score and round it to a full number
    score2 = float(input("What mark did you get on your mini prject 2?"))
    # Work out the total grade by adding what each grade is worth as a percentage
    total = round((score1*0.4) + (score2*0.6))
    # Returning total to be used outside of this function
    return total

def get_grade(score):
    # Running the function scores() to get the users grade
    finalScore = Average
    # Checking if grade is a first
    if finalScore >= 70:
        score = "First Class"
    # Checking if grade is a upper second
    elif finalScore >= 60:
        score = "Upper Second"
    # Checking if grade is a lower second
    elif finalScore >= 50:
        score = "Lower Second"
    # Checking if grade is a third
    elif finalScore >= 40:
        score = "Third"
    # If not any of the above then grade can only be a fail
    else:
        score = "Fail"
    # Returning score to be used outside of this function
    return score


Name = naming(name)
Average = scores(total)
Classification = get_grade(score)
# Printing results in format
print(f"Student: {Name} | Final Score: {Average} | Result: {Classification}")