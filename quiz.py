print("Welcome My Game")
a = input("if you want to play, write yes! : ").lower()


if a != "yes":
    quit()
print("Let's start")
score = 0

b=input("What is the capital of Turkey? ").upper()
if b == "ANKARA":
    score+=1

c= input("Who is the founder of Turkey: ").upper()
if c=="ATATURK":
 score+=1

d=input (str("When the Turkish Republic was found :"))
if d== "1923":
    score+=1
    
e=input (str("what is the first constitution of Turkısh Republic :"))
if e== "1924":
    score+=1

f=input (str("When the six arrow program approved by CHP:"))
if f== "1931":
    score+=1

g=input ("Who is the second president of Turkey :").upper()
if g== "INONU" :
     score+=1
print("The game has end, you have " +  str(score)  +  " true answers.")
