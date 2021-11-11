import random
# 21st Century Questions
q1 = ("Who hit the most home runs in the 2010’s?", "Nelson Cruz")
q2 = ("Who hit the most home runs in the 2000’s?", "Alex Rodriguz")
q3 = ("Since 2000, which team has the most wins during the regular season?", "Mariners")
q4 = ("Which player hit the first ever inside the park home run in the all star game in 2007?", "Ichiro")
q5 = ("In 2009 Derek Jeter smacked career hit number 2,722 setting the new Yankees record. Whose record did he surpass?", "Lou Gehrig")
q6 = ("Between 2002 - 2004, this pitched set the record with the most consecutive saves with 84", "Eric Gange")
q7 = ("Who had the most stike outs in the 2010's?", "Max Scherzer")
q8 = ("This pitcher won 3 Cy young awards in the 2000's", "Randy Johnson")
q9 = ("In 2001, This player hit a walk off single against the Mariano Rivera to give his team their only world series title", "Luis Ganzalez")
q10 = ("In 2004, this player broke the MLB record for hits in a season with 262", "Ichiro")

# late 20th century questions
q11 = ("In 1970 who set the record for striking out 10 consecutive batters?", "Tom Seaver")
q12 = ("In 1989, what player won the AL MVP without making the All Star team?", "Robin Yount")
q13 = ("In 1995, this player became the first to reach 50 doubles and 50 home runs in the same season", "Albert Belle")
q14 = ("Retiring in 1993, this player tied the record for most seasons played in the MLB with 27", "Nolan Ryan")
q15 = ("This Major Leaguer played 22 season, retired in 1974, was inducted into the Hall of Fame in 1990, and is known as 'Mr. Tiger'", "Al Kaline")
q16 = ("Prior to Miguel Cabrera winning the triple crown in 2012, the last player to accomplish this was in 1967", "Carl Yastrzemski")
q17 = ("This pitcher finally threw a no-hitter in 1990 for the Blue Jays after previously losing 3 no hit bids with 2 outs in thr 9th", "Dave Steib")
q18 = ("In 1980, this player was the first to make $1 million in a single year", "Nolan Ryan")
q19 = ("Who hit the most home runs in the 1990's?", "Mark McGwire")
q20 = ("What pitcher had the most wins in the 1980's", "Jack Morris")

# early 20th century questions
q21 = ("Which pitcher holds the record for most consecutive opening day starts for the same club?", "Robin Roberts")
q22 = ("Who is the only player in Braves history to play in all three cities they called home?", "Eddie Mathews")
q23 = ("From 1947 - 1952, this player set a record for leading the MLB in home runs for 6 consecutive years", "Ralph Kiner")
q24 = ("Who hit the most home runs in the 1950's?", "Duke Snider")
q25 = ("Which player had the most hits in the 1960's?", "Roberto Clemente")
q26 = ("MLB lowered the mound in 1968 after one of the best single season pitching performances by this player", "Bob Gibson")
q27 = ("Who hit the most home runs in the 1940's?", "Ted Williams")
q28 = ("This player carries the most gold glove awards by a position player", "Brooks Robinson")
q29 = ("In 1965, this player was the oldest to appear in a game at the age of 59", "Satchel Paige")
q30 = ("This player became the first, first ballot hall of famer for a catcher", "Johnny Bench")


# dead ball era questions
q31 = ("Who had the most career hits by the end of the dead ball era?", "Honus Wagner")
q32 = ("Who won the inaugural World Series held in 1903?", "Red Sox")
q33 = ("In 1933, this player took home the American League Triple Crown", "Jimmie Fox")
q34 = ("This team hold the record for winning the least amount of games in a season in 1916", "Philadelphia Athletics")
q35 = ("This player refused to have his baseball cards sold in tabaco products, making it very rare and one of the highly sought after sports cards ever", "Honus Wagner")
q36 = ("The name of Shoeless Joe Jacksons' bat, one of the most fabled artifacts in baseball", "Black Betsy")
q37 = ("Who hit the most home runs in the 1930's?", "Jimmie Foxx")
q38 = ("In 1916, this pitcher recorded 23 wins with a 1.75 ERA", "Babe Ruth")
q39 = ("In 1920, this pitcher was the first to record 300 wins all with the same team", "Walter Johnson")
q40 = ("This player holds the record for most XBH in a single season with 119", "Babe Ruth")


# world series questions
qw1 = ("Who is the only manager with the all-time wins list for two franchises?", "Sparky Anderson")
qw2 = ("Which team has the most players in the HOF?", "Giants")
qw3 = ("Who is the most recent player to steal 100 bases in a season?", "Vince Coleman")
qw4 = ("As of 2020, who is the most recent player to achieve the 40/40 mark?", "Alfonso Soriano")
qw5 = ("Who was the first Major League player to have their number retired?", "Lou Gehrig")
qw6 = ("Which manager has been ejected the most times in MLB history?", "Bobby Cox")
qw7 = ("What MLB player holds the record for most consecutive games with a strike out?", "Aaron Judge")
qw8 = ("What player hit the Shot heard around the world?", "Bobby Thomson")
qw9 = ("Who was the first New York Met to throw a no-hitter", "Johan Santana")
qw10 = ("This player carries the most gold glove awards by a left fielder", "Barry Bonds")


# 21st century
aQuestions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
bQuestions = [q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]
cQuestions = [q21,q22,q23,q24,q25,q26,q27,q28,q29,q30]
dQuestions = [q31,q32,q33,q34,q35,q36,q37,q38,q39,q40]
eQuestions = [qw1,qw2,qw3,qw4,qw5,qw6,qw7,qw8,qw9,qw10]
bballq = {"21st": aQuestions, "late20": bQuestions,"early20": cQuestions, "deadball": dQuestions, "WorldSeries": eQuestions}
print("Question: ")
key = list(bballq.keys())
q = random.choice(bballq[random.choice(key)])
print(q[0])


answer = input("Enter answer: ")
if answer == q[1]:
    print("Correct")
else:
    print("Wrong" ",", q[1])

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
