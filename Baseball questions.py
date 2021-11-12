import random

# 21st Century Questions
q1 = ("Who hit the most home runs in the 2010’s?", "Nelson Cruz")
q2 = ("Who hit the most home runs in the 2000’s?", "Alex Rodriguz")
q3 = ("Since 2000, which team has the most wins during the regular season?", "Mariners")
q4 = ("Which player hit the first ever inside the park home run in the all star game in 2007?", "Ichiro")
q5 = ("In 2009 Derek Jeter smacked career hit number 2,722 setting the new Yankees record. Whose record did he surpass?", "Lou Gehrig")

# late 20th century questions
q11 = ("In 1970 who set the record for striking out 10 consecutive batters?", "Tom Seaver")

# early 20th century questions
q21 = ("Which pitcher holds the record for most consecutive opening day starts for the same club?", "Robin Roberts")

# dead ball era questions
q31 = ("Who had the most career hits by the end of the dead ball era?", "Honus Wagner")
q32 = ("Who won the inaugural World Series held in 1903?", "Red Sox")

# world series questions
qw1 = ("Who is the only manager with the all-time wins list for two franchises?", "Sparky Anderson")
qw2 = ("Which team has the most players in the HOF?", "Giants")
qw3 = ("Who is the most recent player to steal 100 bases in a season?", "Vince Coleman")
qw4 = ("Who is the most recent player to achieve the 40/40 mark?", "Alfonso Soriano")

# 21st century
aQuestions = [q1,q2,q3,q4,q5]
bQuestions = [q11]
cQuestions = [q21]
dQuestions = [q31,q32]
eQuestions = [qw1,qw2,qw3,qw4]
bballq = {"21st": aQuestions, "late20": bQuestions,"early20": cQuestions, "deadball": dQuestions, "WorldSeries": eQuestions}
print("Question: ")
key = list(bballq.keys())
q = random.choice(bballq[random.choice(key)])
print(q[0])


answer = input("Enter answer: ")
if answer == q[1]:
    print("Correct")
else:
    print("Wrong")

"""
# late 20th century
bQuestions = [q11]
print("Question: ")
q = random.choice(bQuestions)
print(q[0])

answer = input("Enter answer: ")
if answer == q[1]:
    print("Correct")
else:
    print("Wrong")

# early 20th century 
cQuestions = [q21]
print("Question: ")
q = random.choice(cQuestions)
print(q[0])

answer = input("Enter answer: ")
if answer == q[1]:
    print("Correct")
else:
    print("Wrong")

# dead ball era
dQuestions = [q31,q32]
print("Question: ")
q = random.choice(dQuestions)
print(q[0])

answer = input("Enter answer: ")
if answer == q[1]:
    print("Correct")
else:
    print("Wrong")

# world series 
eQuestions = [qw1,qw2,qw3,qw4]
print("Question: ")
q = random.choice(eQuestions)
print(q[0])

answer = input("Enter answer: ")
if answer == q[1]:
    print("Correct")
else:
    print("Wrong")
"""