# write a code to input numbers btwn 1 to 100 and display the grade 

a=int(input("enter your number here : "))

if a > 100 or a < 0 : #use or not and here remmber  
        print(" your number is invalid")
elif a<=100 and a>=90 :
        print("grade a")
elif a<=90 and a>=80 :
        print("grade b")
elif a<=80 and a>=70 :
        print("grade c")
elif a<=70 and a>=60 :
        print("garde d")
else :
        print("fail")