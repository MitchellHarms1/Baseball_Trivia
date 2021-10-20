import random
# Hello from Github
# 21st Century Questions
q1 = ("Who hit the most home runs in the 2010’s?", "Nelson Cruz")
q2 = ("Who hit the most home runs in the 2000’s?", "Alex Rodriguz")
q3 = ("Since 2000, which team has the most wins during the regular season?", "Mariners")
q4 = ("Which player hit the first ever inside the park home run in the all star game in 2007?", "Ichiro")
q5 = ("In 2009 Derek Jeter smacked career hit number 2,722 setting the new Yankees record. Whose record did he surpass?", "Lou Gehrig")
q6 = ("Between 2002 - 2004, this pitched set the record with the most consecutive saves with 84", "Eric Gange")

# late 20th century questions
q11 = ("In 1970 who set the record for striking out 10 consecutive batters?", "Tom Seaver")
q12 = ("In 1989, what player won the AL MVP without making the All Star team?", "Robin Yount")
q13 = ("In 1995, this player became the first to reach 50 doubles and 50 home runs in the same season", "Albert Belle")
q14 = ("Retiring in 1993, this player tied the record for most seasons played in the MLB with 27", "Nolan Ryan")

# early 20th century questions
q21 = ("Which pitcher holds the record for most consecutive opening day starts for the same club?", "Robin Roberts")
q22 = ("Who is the only player in Braves history to play in all three cities they called home?", "Eddie Mathews")
q23 = ("From 1947 - 1952, this player set a record for leading the MLB in home runs for 6 consecutive years", "Ralph Kiner")

# dead ball era questions
q31 = ("Who had the most career hits by the end of the dead ball era?", "Honus Wagner")
q32 = ("Who won the inaugural World Series held in 1903?", "Red Sox")
q33 = ("In 1933, this player took home the American League Triple Crown", "Jimmie Fox")

# world series questions
qw1 = ("Who is the only manager with the all-time wins list for two franchises?", "Sparky Anderson")
qw2 = ("Which team has the most players in the HOF?", "Giants")
qw3 = ("Who is the most recent player to steal 100 bases in a season?", "Vince Coleman")
qw4 = ("As of 2020, who is the most recent player to achieve the 40/40 mark?", "Alfonso Soriano")
qw5 = ("Who was the first Major League player to have their number retired?", "Lou Gehrig")
qw6 = ("Which manager has been ejected the most times in MLB history?", "Bobby Cox")
qw7 = ("What MLB player holds the record for most consecutive games with a strike out?", "Aaron Judge")
qw8 = ("What player hit the Shot heard around the world?", "Bobby Thomson")


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
