from fractions import gcd
import random
import math

def startup():
    print("Welcome to SuperMath!")
    print("This program computes numbers using imputs that you give it.")
    global choice
    choice = input("Would you like to compute e, pi, tau, the golden ratio or a Pythagorean triple... ")
    print("   ")
    choice = choice.lower()
    while not choice.isalpha():
        print("You're answer was invalid. Try again.")
        choice = input("Would you like to compute e, pi, tau, the golden ratio or a Pythagorean triple... ")
    if choice in ["e", "pi", "tau", "the golden ratio", "golden ratio", "golden", "triple", "pythagorean triple"]:
        print("Please wait. The program will begin shortly...")
        print("   ")
    while choice not in ["e", "pi", "tau", "the golden ratio", "golden ratio", "golden", "triple", "pythagorean triple"]:
        print("You didn't choose one of the options. Try again.")
        choice = input("Would you like to compute e, pi, tau, the golden ratio or a Pythagorean triple... ")
        choice = choice.lower()
        print("   ")
    print("How many times would you like this program to produce that (different ones each time)?")
    print("(If you do more than 10, they are saved in a .txt file in the root directory of python. If you don't know where that is, google it.)")
    print("   ")
    global iterations
    iterations = input("So, how many times would you like this program to produce that (different ones each time)... ")
    while not iterations.isdigit():
         print("You're answer was invalid. Try again.")
         iterations = input("So, how many times would you like this program to produce that (different ones each time)... ")
    iterations = int(iterations)
    print("   ")
    if choice == "pi":
        print("For pi, you can choose between 7 dfferent methods. They are Parker, Viete, Wallis, Ramanujan (Method 1, 1914), Madhava-Leibniz 1, Madhava-Leibniz 2 or through Buffon's Needle?")
        choicepi = input("What method... ")
        choicepi.replace(" ", "")
        choicepi.replace("-", "")
        choicepi.replace("'", "")
        while choicepi not in ["parker", "viete", "wallis", "ramanujan", "madhavaleibniz1", "madhava1", "leibniz1", "madhavaleibniz2", "madhava2", "leibniz2", "buffon", "buffonsneedle", "needle", "buffons"]:
            print("You're answer was invalid. Try again.")
            choicepi = input("What method... ")
        if choicepi == "parker":
            randompi()
        elif choicepi == "viete":
            radpi()
        elif choicepi == "wallis":
            wallispi()
        elif choicepi in ["madhavaleibniz1", "madhava1", "leibniz1"]:
            leibniz1pi()
        elif choicepi in ["madhavaleibniz2", "madhava2", "leibniz2"]:
            leibniz2pi()
        elif choicepi in ["buffon", "buffonsneedle", "needle", "buffons"]:
            needlepi()
        elif choicepi == "ramanujan":
            ramanpi()
    elif choice == "e":
        print("For e, you can choose between 2 dfferent methods. They are the normal method and the root method.")
        choicee = input("What method... ")
        choicee = choicee.lower()
        while not choicee.isalpha():
            print("You're answer was invalid. Try again.")
            choicee = input("What method... ")
        while choicee not in ["normal", "root"]:
            print("You're answer was invalid. Try again.")
            choicee = input("What method... ")
        if choicee == "normal":
            enormal()
        elif choicee == "root":
            eroot()
    elif choice == "tau":
        print("For tau, you can choose between 7 dfferent methods. They are Parker, Viete, Wallis, Ramanujan, Madhava-Leibniz 1, Madhava-Leibniz 2 or through Buffon's Needle?")
        choicetau = input("What method... ")
        choicetau = choicetau.lower()
        choicetau.replace(" ", "")
        choicetau.replace("-", "")
        choicetau.replace("'", "")
        while not choicetau.isalpha():
            print("You're answer was invalid. Try again.")
            choicetau = input("What method... ")
        while choicetau not in ["parker", "viete", "wallis", "madhavaleibniz1", "ramanujan", "madhava1", "leibniz1", "madhavaleibniz2", "madhava2", "leibniz2", "buffon", "buffonsneedle", "needle", "buffons"]:
            print("You're answer was invalid. Try again.")
            choicetau = input("What method... ")
        if choicetau == "parker":
            randomtau()
        elif choicetau == "viete":
            radptau()
        elif choicetau == "wallis":
            wallistau()
        elif choicetau in ["madhavaleibniz1", "madhava1", "leibniz1"]:
            leibniz1tau()
        elif choicepi in ["madhavaleibniz2", "madhava2", "leibniz2"]:
            leibniz2tau()
        elif choicetau in ["buffon", "buffonsneedle", "needle", "buffons"]:
            needletau()
        elif choicetau == "ramanujan":
            ramantau()
    elif choice in ["the golden ratio", "golden ratio", "golden"]:
        phi()
    elif choice in ["pythagorean triple", "triple"]:
        triple()

def accerror():
    global accuracyny
    global errorny
    accuracyny = input("Do you care about what the accuracy of the approximation is... ")
    print("   ")
    accuracyny = accuracyny.lower()
    if accuracyny in ["y", "yes"]:
        accuracyny = 1
    elif accuracyny in ["n", "no"]:
        accuracyny = 0
    else:
        print("Your answer was invalid")
        accuracyny = input("Do you care about what the accuracy of the approximation is... ")
        print("   ")
    errorny = input("Do you care about what the approximation will be off by... ")
    errorny = errorny.lower()
    print("   ")
    if errorny in ["y", "yes"]:
        errorny = 1
    elif errorny in ["n", "no"]:
        errorny = 0
    else:
        print("Your answer was invalid")
        errorny = input("Do you care about what the approximation will be off by... ")
    print("   ")
    print("   ")

def randompi():
    global constant
    global constant_name
    constant = math.pi
    constant_name = "Pi"
# This part is the startup.
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+                                                                        +")
    print("+          This program will compute pi using random numbers.            +")
    print("+                                                                        +")
    print("+     It will ask for the maximum number you would like to be chosen.    +")
    print("+                                                                        +")
    print("+         It will take however many pairs of numbers you ask for,        +")
    print("+              compare if their highest common factor is 1               +")
    print("+                   and, if it is, add to a counter.                     +")
    print("+                                                                        +")
    print("+   The final probability is plugged into a formula to approximate pi.   +")
    print("+                                                                        +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# This part deals with pi's questions.
    global maximum
    global ria
    print("   ")
    print("What do you want the maximum value for the range to be? (put in the letter)")
    print("a) 50  b) 100  c) 1000  d) 10000  e) Other")
    print("   ")
    maximum = input("Maximum value for range... ")
    print("   ")
    maximum = maximum.lower()
    while maximum not in ["a", "b", "c", "d", "e", "random"]:
        print("You're answer was invalid. Try again.")
        maximum = input("Maximum value for range... ")
    if maximum == "a":
        maximum = 50
    elif maximum == "b":
        maximum = 100
    elif maximum == "c":
        maximum = 1000
    elif maximum == "d":
        maximum = 10000
    elif maximum == "e":
        maximum = int(input("Enter a value... "))
        print("   ")
        while maximum <= 10:
            print("You're value is too small. Please enter a bigger one.")
            maximum = int(input("Enter a value... "))
    elif maximum == "random":
        maximum = random.randrange(0, 100000)
    print("   ")
    print("How many pairs do you want to use? (put in the letter)")
    print("a) 50  b) 100  c) 1000  d) 10000  e) Other")
    print("   ")
    ria = input("How many pairs of numbers... ")
    while ria not in ["a", "b", "c", "d", "e", "random"]:
        print("You're answer was invalid. Try again.")
        ria = input("Maximum value for range... ")
        print("   ")
    if ria == "a":
        ria = 50
    elif ria == "b":
        ria = 100
    elif ria == "c":
        ria = 1000
    elif ria == "d":
        ria = 10000
    elif ria == "e":
        ria = int(input("Enter a value... "))
        print("   ")
        while maximum <= 10:
            print("You're value is too small. Please enter a bigger one.")
            maximum = int(input("Enter a value... "))
            print("   ")
    elif ria == "random":
        ria = random.randrange(0, 100000)
    print("   ")

# This part defines and then approximates pi.
    def piapprox(m, i):
        global amount
        global count
        global pi_approx
        amount = 0
        count = 0
        while count != i:
            x = random.randrange(0, m)
            y = random.randrange(0, m)
            divisor = gcd(x, y)
            if divisor == 1:
                amount = amount + 1
            count = count + 1
        global approx
        approx = (6/(amount/i)) ** 0.5
    if iterations == 1:
        piapprox(maximum, ria)
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            piapprox(maximum, ria)
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def radpi():
    global constant
    global constant_name
    global limit
    constant = math.pi
    constant_name = "Pi"
    def acalc(n):
        global a
        a = math.sqrt(2)
        count = 0
        while count < n:
            a = math.sqrt(2+a)
            count += 1
        return a
    limit = int(input("Enter a limit of how many terms in the repeated multiplication... "))
    def piapprox():
        global approx
        terms = []
        terms_actual = list(terms)
        count2 = 0
        while count2 <= limit:
            term = 4/(acalc(count2))
            terms.append(term)
            count2 += 1
        count3 = 1
        running = 1
        while count3 <= len(terms_actual):
            running = running * terms_actual[count3]
            count3 += 1
        approx = running * 4/math.sqrt(2)
    if iterations == 1:
        piapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            piapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def leibniz1pi():
    global constant
    global constant_name
    global limit
    constant = math.pi
    constant_name = "Pi"
    limit = int(input("What would you like the limit to be for the Sigma sum... "))
    def piapprox():
        n = 0
        terms = []
        terms_actual = list(terms)
        while n <= limit:
            terms_actual.append(((1/((4*n)+1))-(1/((4*n)+3))))
        count = 0
        while count <= len(terms_actual):
            running = running + terms_actual[count]
        running = running * 4
        approx = running
    if iterations == 1:
        piapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            piapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes) 

def leibniz2pi():
    global constant
    global constant_name
    global limit
    constant = math.pi
    constant_name = "Pi"
    limit = int(input("What would you like the limit to be for the Sigma sum... "))
    def piapprox():
        n = 0
        terms = []
        terms_actual = list(terms)
        while n <= limit:
            terms_actual.append((2/((4*n +1)*(4*n + 3))))
        count = 0
        while count <= len(terms_actual):
            running = running + terms_actual[count]
        running = running * 4
        approx = running
    if iterations == 1:
        piapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            piapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def wallispi():
    global constant
    global constant_name
    global limit
    constant = math.pi
    constant_name = "Pi"
    limit = int(input("What would you like the limit to be for the product sum... "))
    def piapprox():
        n = 1
        terms = []
        terms_actual = list(terms)
        while n <= limit:
            terms_actual.append(((2*n)/(2*n - 1))*((2*n)/(2*n + 1)))
        count = 0
        while count <= len(terms_actual):
            running = running * terms_actual[count]
        approx = running
    if iterations == 1:
        piapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            piapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def ramanpi():
    global constant
    global constant_name
    global limit
    constant = math.pi
    constant_name = "Pi"
    limit = int(input("What would you like the limit to be for the product sum... "))
    def piapprox():
        n = 0
        terms = []
        terms_actual = list(terms)
        while n <= limit:
            terms_actual.append((((math.factorial(4*n))/(((4**n)*math.factorial(n))**4))*((1103+26390*n)/(882**(2*n)))))
        count = 0
        while count <= len(terms_actual):
            running = running + terms_actual[count]
        running = running * ((math.sqrt(8))/99**2)
        approx = 1/running
    if iterations == 1:
        piapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            piapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def needlepi():
    global constant
    global constant_name
    global length
    global width
    constant = math.pi
    constant_name = "Pi"
    print("This method uses a famous probabiliy to approximate pi using a re-arranged formula from the problem of Buffon's Needle.")
    length = int(input("What do you want the length of the needle to be... "))
    width = int(input("What do you want the width of the parallel sections to be... "))
    P = 1808/3408
    def piapprox():
        global approx
        approx = ((2*length)/(width*P))
    if iterations == 1:
        piapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            piapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def randomtau():
    global constant
    global constant_name
    constant = 2 * math.pi
    constant_name = "Tau"
# This part is the startup.
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+                                                                        +")
    print("+          This program will compute tau using random numbers.           +")
    print("+                                                                        +")
    print("+     It will ask for the maximum number you would like to be chosen.    +")
    print("+                                                                        +")
    print("+         It will take however many pairs of numbers you ask for,        +")
    print("+              compare if their highest common factor is 1               +")
    print("+                   and, if it is, add to a counter.                     +")
    print("+                                                                        +")
    print("+   The final probability is plugged into a formula to approximate tau.  +")
    print("+                                                                        +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# This part deals with tau's questions.
    global maximum
    global ria
    print("   ")
    print("What do you want the maximum value for the range to be? (put in the letter)")
    print("a) 50  b) 100  c) 1000  d) 10000  e) Other")
    print("   ")
    maximum = input("Maximum value for range... ")
    print("   ")
    maximum = maximum.lower()
    while maximum not in ["a", "b", "c", "d", "e", "random"]:
        print("You're answer was invalid. Try again.")
        maximum = input("Maximum value for range... ")
    if maximum == "a":
        maximum = 50
    elif maximum == "b":
        maximum = 100
    elif maximum == "c":
        maximum = 1000
    elif maximum == "d":
        maximum = 10000
    elif maximum == "e":
        maximum = int(input("Enter a value... "))
        print("   ")
        while maximum <= 10:
            print("You're value is too small. Please enter a bigger one.")
            maximum = int(input("Enter a value... "))
    elif maximum == "random":
        maximum = random.randrange(0, 100000)
    print("   ")
    print("How many pairs do you want to use? (put in the letter)")
    print("a) 50  b) 100  c) 1000  d) 10000  e) Other")
    print("   ")
    ria = input("How many pairs of numbers... ")
    while ria not in ["a", "b", "c", "d", "e", "random"]:
        print("You're answer was invalid. Try again.")
        ria = input("Maximum value for range... ")
        print("   ")
    if ria == "a":
        ria = 50
    elif ria == "b":
        ria = 100
    elif ria == "c":
        ria = 1000
    elif ria == "d":
        ria = 10000
    elif ria == "e":
        ria = int(input("Enter a value... "))
        print("   ")
        while maximum <= 10:
            print("You're value is too small. Please enter a bigger one.")
            maximum = int(input("Enter a value... "))
            print("   ")
    elif ria == "random":
        ria = random.randrange(0, 100000)
    print("   ")

# This part defines and then approximates tau.
    def tauapprox(m, i):
        global amount
        global count
        global approx
        amount = 0
        count = 0
        while count != i:
            x = random.randrange(0, m)
            y = random.randrange(0, m)
            divisor = gcd(x, y)
            if divisor == 1:
                amount = amount + 1
            count = count + 1
        approx = 2 * ((6/(amount/i)) ** 0.5)
    if iterations == 1:
        tauapprox(maximum, ria)
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            tauapprox(maximum, ria)
            approxn = approx
            approxes += [approxn]
            iterationlist += 1

def radtau():
    global constant
    global constant_name
    global limit
    constant = 2*math.pi
    constant_name = "Tau"
    def acalc(n):
        global a
        a = math.sqrt(2)
        count = 0
        while count < n:
            a = math.sqrt(2+a)
            count += 1
        return a
    limit = int(input("Enter a limit of how many terms in the repeated multiplication... "))
    def tauapprox():
        global approx
        terms = []
        terms_actual = list(terms)
        count2 = 0
        while count2 <= limit:
            term = 4/(acalc(count2))
            terms.append(term)
            count2 += 1
        count3 = 1
        running = 1
        while count3 <= len(terms_actual):
            running = running * terms_actual[count3]
            count3 += 1
        approx = running * 4/math.sqrt(2)
        approx = approx * 2
    if iterations == 1:
        tauapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            tauapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def leibniz1tau():
    global constant
    global constant_name
    global limit
    constant = 2*math.pi
    constant_name = "Tau"
    limit = int(input("What would you like the limit to be for the Sigma sum... "))
    def tauapprox():
        n = 0
        terms = []
        terms_actual = list(terms)
        while n <= limit:
            terms_actual.append(((1/((4*n)+1))-(1/((4*n)+3))))
        count = 0
        while count <= len(terms_actual):
            running = running + terms_actual[count]
        running = running * 4
        approx = running
        approx = approx * 2
    if iterations == 1:
        tauapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            tauapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes) 

def leibniz2tau():
    global constant
    global constant_name
    global limit
    constant = 2*math.pi
    constant_name = "Tau"
    limit = int(input("What would you like the limit to be for the Sigma sum... "))
    def tauapprox():
        n = 0
        terms = []
        terms_actual = list(terms)
        while n <= limit:
            terms_actual.append((2/((4*n +1)*(4*n + 3))))
        count = 0
        while count <= len(terms_actual):
            running = running + terms_actual[count]
        running = running * 4
        approx = running
        approx = approx * 2
    if iterations == 1:
        tauapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            tauapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def wallistau():
    global constant
    global constant_name
    global limit
    constant = 2*math.pi
    constant_name = "Tau"
    limit = int(input("What would you like the limit to be for the product sum... "))
    def tauapprox():
        n = 1
        terms = []
        terms_actual = list(terms)
        while n <= limit:
            terms_actual.append(((2*n)/(2*n - 1))*((2*n)/(2*n + 1)))
        count = 0
        while count <= len(terms_actual):
            running = running * terms_actual[count]
        approx = running
        approx = approx * 2
    if iterations == 1:
        tauapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            tauapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def ramantau():
    global constant
    global constant_name
    global limit
    constant = 2*math.pi
    constant_name = "Tau"
    limit = int(input("What would you like the limit to be for the product sum... "))
    def tauapprox():
        n = 0
        terms = []
        terms_actual = list(terms)
        while n <= limit:
            terms_actual.append((((math.factorial(4*n))/(((4**n)*math.factorial(n))**4))*((1103+26390*n)/(882**(2*n)))))
        count = 0
        while count <= len(terms_actual):
            running = running + terms_actual[count]
        running = running * ((math.sqrt(8))/99**2)
        approx = 1/running
        approx = approx * 2
    if iterations == 1:
        tauapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            tauapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def needletau():
    global constant
    global constant_name
    global length
    global width
    global P
    constant = 2*math.pi
    constant_name = "Tau"
    print("This method uses a famous probabiliy to approximate tau using a re-arranged formula from the problem of Buffon's Needle.")
    length = int(input("What do you want the length of the needle to be... "))
    width = int(input("What do you want the width of the parallel sections to be... "))
    P = 1808/3408
    def tauapprox():
        global approx
        approx = ((2*length)/(width*P))
        approx = approx * 2
    if iterations == 1:
        tauapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            tauapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def enormal():
    global constant
    global constant_name
    global n
    constant = math.e
    constant_name = "e"
    n = input("What value for n would you like... ")
    print("   ")
    while n.isalpha():
        print("You're answer was invalid. Try again.")
        n = input("What value for n would you like... ")
        print("   ")
    n = int(n)
    def eapprox():
        global approx
        approx = (1 + 1/n) ** n
    if iterations == 1:
        eapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist != iterations:
            enormal()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)

def phi():
    global constant
    global constant_name
    constant = (1 + math.sqrt(5))/2
    constant_name = "Phi"
    n = int(input("What is the value of n for the upper term... "))
    if iterations > 1:
        step = int(input("What do want as the step for raising the value of n... "))
        limit = iterations + 1
    def phiapprox():
        global approx
        Phi = (1 + math.sqrt(5))/2
        phi = (1 - math.sqrt(5))/2
        upperterm = (Phi ** n - phi ** n)/math.sqrt(5)
        lowerterm = (Phi ** (n-1) - phi ** (n-1))/math.sqrt(5)
        approx = upperterm / lowerterm
    if iterations == 1:
        phiapprox()
        accerror()
    elif iterations != 1:
        iterationlist = 0
        global approxeslist
        global approxes
        approxeslist = []
        approxes = list(approxeslist)
        while iterationlist in range(1, limit):
            n =+ step
            phiapprox()
            approxn = approx
            approxes += [approxn]
            iterationlist += 1
        approxes = sorted(approxes)


    ''' work out a way to approximate this by using an nth term rule for fibonacci sequence and
    computing xth and yth (both inputs; x > y), then divide x by y and work out accuracy,
    but also ask for step, so do x+1 and y+1 (all to x+i and y+i, where i is input for step),
    then work out average, but also print out all individual ones with each accuracy. but if over 10,
    then write to file.
    '''
def triple():
    print("This part of the program computes Pythagorean triples.")
    print("   ")
    global m
    global n
    m = int(input("Give a value for m... "))
    n = int(input("Give a value for n... "))
    if iterations > 1:
        global step
        global limit
        step = int(input("Give a step for making multiple triples (since you'll need different m and n values each time)... "))
        limit = iterations + 1
    def triplecalc():
        global a
        global b
        global c
        a = abs(m*m - n*n)
        b = 2 * m * n
        c = math.sqrt(a*a + b*b)
        first = gcd(a, b)
        second = gcd(b, c)
        third = gcd(a, c)
        if first == second == third:
            divisor = first
            a = a / divisor
            b = b / divisor
            c = c / divisor
    if iterations == 1:
        triplecalc()
    elif iterations != 1:
        iterationlist = 1
        global tripleslist
        global triples
        tripleslist = []
        triples = list(tripleslist)
        while iterationlist in range(1, limit):
            m = m + step
            n = n + step
            triplecalc()
            triplesn = [a, b, c]
            triples += [triplesn]
            iterationlist += 1

def results(constant, constant_name):
    print("**************************************************************************************")
    if iterations == 1:
        print("Approximation of %s: " % choice + str(approx))
        print(constant_name + " is actually " + str(constant))
        print("   ")
        if accuracyny == 1:
            accuracy = (approx/constant) * 100
            if accuracy > 100:
                accuracy = accuracy - 100
                accuracy = 100 - accuracy
            accuracy_print = "The accuracy of your approximation is: %s" % round(accuracy, 2) + "%"
            print(accuracy_print)
            print("   ")
        if errorny == 1:
            error = approx - constant
            if error > 0:
                print("The approximation was off by +" + str(error))
                print("   ")
            elif error < 0:
                print("The approximation was off by " + str(error))
                print("   ")
    elif iterations > 1 and iterations <= 10:
        print("Approximations: ")
        count = 0
        for count in range(0, len(approxes)):
            print(approxes[count])
            count = count + 1
        print("   ")
        print(constant_name + " is actually " + str(constant))
    elif iterations > 10:
        approximations = open("approximations.txt", "w")
        for number in approxes:
            approximations.write(str(number) + "\n")
        approximations.close()
        print("Now look in the root directory of Python. The file will be overridden each time, so copy the file and save it somewhere safe if you want to keep the approximations you just calculated.")

def tripleresults():
    if iterations == 1:
        print("You're triple is: a = %s, b = %s and c = %s" % (a, b, c))
    elif iterations > 1 and iterations <= 10:
        print("Triples: (a, b, c)")
        count = 0
        for count in range(0, len(triples)):
            print(triples[count])
            count = count + 1
    elif iterations > 10:
        pythagtriples = open("triples.txt", "w")
        for count in range(0, len(triples)):
            pythagtriples.write(str(triples[count]) + "\n")
        print("Now look in the root directory of Python. The file will be overridden each time, so copy the file and save it somewhere safe if you want to keep the triples you just computed.")        

startup()
if choice not in ["triple", "pythagorean triple"]:
    results(constant, constant_name)
elif choice in ["triple", "pythagorean triple"]:
    tripleresults()
