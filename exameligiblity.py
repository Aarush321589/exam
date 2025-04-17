medical_cause=input("did you have a medical cause yes or no")
atten=int(input("enter the attendence of students"))
if medical_cause=="Y":
    print('you are allowed')
else:
    if atten>=75:
        print("allowed")
    else:
        print("not allowed")