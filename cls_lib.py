sub_fields=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
class allmethods:
    def Subfields():
        print("Sub-fields in AI are : ")
        for i in range(len(sub_fields)):
            print(sub_fields[i])


    def OddEven():
        num1=int(input("Enter the number : "))
        if num1%2==0:
            return f"{num1} is even number"
        else:
            return f"{num1} is odd number"
        

    def Eligible():
        gender=input("Enter your gender : ")
        age = int(input("Enter your age : "))
        if(gender == "MALE" or gender == "male" or gender == "M"):
            if(age>=21):
                var= "ELIGIBLE"
            else:
                var= "NOT ELIGIBLE"
        elif(gender == "FEMALE" or gender == "female" or gender == "F"):
            if(age>=18):
                var= "ELIGIBLE"
            else:
                var= "NOT ELIGIBLE"
        else:
            var= "INVALID GENDER..."   
        return f"Your Gender : {gender} \nYour age : {age} \n{var}"


    def percentage():
        limit = int(input("Enter total subjects : "))
        b=0
        for i in  range(limit):
            a=int(input(f"Subject {i+1}"))
            print(f"Subject :{i+1} = {a}")
            b+=a
            c=b/limit
        return f"Total : {b}\nPercentage : {c:.14f}"
    

    def a_o_t():
            h=int(input("height : "))
            b=int(input("breadth : "))
            a_o_t=((h)*(b))/2
            return f"Height : {h}\nBreadth : {b} \nArea formula : (Height*Breadth)/2\nArea of triangle is : {a_o_t}"
    

    def p_o_t():
            h=int(input("height1 : "))
            h2=int(input("height2 : "))
            b=int(input("breadth : "))
            p_o_t=h+h2+b
            return f"Height1 : {h}\nHeight2 : {h2}\nBreadth : {b}\nPerimeter formula : Height1+Height2+Breadth\nPerimeter of Triangle : {p_o_t}"
    