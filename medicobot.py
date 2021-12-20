
##from playsound import playsound
##import pytesseract
##cpath = (r"C:\Program Files (x86)\Tesseract-OCR\tesseract")
##pytesseract.pytesseract.tesseract_cmd = cpath
##import cv2
##import re
##import IPython.display as display
##from PIL import Image



def ex():
    e=int(input("\npress 1 to continue: "))

def docrec():
    age=int(input("enter the age of the person: "))

    if(age<18):
        print("you should consult an RMP doctor in your locality.\nIf the condition seems serious,consult a pediatrician for diagnosis\n")
    elif(age>60):
        print("you should consult an RMP doctor in your locality.\nIf the condition seems serious,consult a geriatritcian for diagnosis\n")

    cq=int(input("\ncontinue if you want an organ specific doctor recomendation.\n1.continue\n2.exit\n\npick one: "))

    if(cq==2):
        exit;       
    else:
        print("\npick the affected organ from below:\n1.heart\n2.brain\n3.skin\n4.eye\n5.nose\n6.tongue\n7.teeth\n8.foot\n9.kidney\n10.stomach\n11.urinary tract\n12.nervous system\n13.hormone related\n14.joints/bones/tendons/muscles\n15.reproductive system/sex organ\n16.excretory system\n\nif you can't pinpoint a specific organ,go to a diagnostic centre and they can help\n")
        n=int(input("\npick a no. from provided options: "))
        print("\n")       
        if(0<n<17):
            if(n==1):
                print("consult a cardiologist");
            if(n==2):
                print("consult a mental health professional,or a therepist,or a psychiatrist");
            if(n==3):
                print("consult a dermatologist");
            if(n==4):
                print("consult a opthalmologist or an ENT specialist");
            if(n==5):
                print("consult an ENT specialist");
            if(n==6):
                print("consult an ENT specialist");
            if(n==7):
                print("consult a dentist");
            if(n==8):
                print("consult a podiatrist");
            if(n==9):
                print("consult a nephrologist");
            if(n==10):
                print("consult a gastroenterologist");
            if(n==11):
                print("consult a urologist");
            if(n==12):
                print("consult a neurologist");
            if(n==13):
                print("consult a endocrinologist");
            if(n==14):
                print("consult a rheumatologist");
            if(n==15):
                print("consult a gynecologist if female\nconsult an andrologist or a urologist if male\nconsult a urologist if non binary reproductive organ related issue\n")
            if(n==16):
                print("consult a proctologist");
        else:
            print("\n\ninvalid option.");
    ex();

    
def bmicalc():
    h=float(input("enter height in ft.(eg,5.6 for 5ft 6in): "))

    w=float(input("enter weight in kg: "))


    BMI=float(w/((h*12*2.5*0.01)**2))
    print("BMI= ",BMI)

    if(18<=BMI<=30):
       print("\nyour weight is healthy")
    elif(BMI<18):
       print("\nyou need to gain weight")
    elif(BMI>30):
       print("\nyou need to lose weight")
    ex();
    
def cbpscan():
    import pytesseract
    cpath = (r"C:\Program Files (x86)\Tesseract-OCR\tesseract")
    pytesseract.pytesseract.tesseract_cmd = cpath
    import cv2
    import re

    iname = input("Enter image name:")
    image=cv2.imread(iname)

    text = pytesseract.image_to_string(image,lang='eng')
          
    text = text.replace(" ", "")
    text = text.replace('g/dL', " ")
    text = text.replace('-', " ")

    split_equation = text.split(" ")
    num1 = float(split_equation[0])
    num2 = float(split_equation[1])
    num3 = float(split_equation[2])

    print('Your Reading:',num1,'\nLower Limit:',num2,'\nUpper Limit:',num3)
    if(num1<num2):
        print("\nlow MCHC");
    elif(num1>num3):
        print("\nhigh MCHC");
    elif(num2<num1<num3):
        print("\nYou are healthy!");
    print("\n") 
    ex();
    

def diagopt():
    print("\nDIAGNOSIS\n")
    print("1.Doctor recommendations\n2.reports scan\n3.BMI calculation\n4.exit\n")
    d=int(input("\npick one: "))
    while(d!=4):
        if(d==1):
            print("\nDoctor recommendations\n");
            docrec();
        elif(d==2):
            print("\nreports scan\n");
            cbpscan();
        elif(d==3):
            print("\nBMI calculation\n");
            bmicalc();
        print("\n");
        d=int(input("\n1.Doctor recommendations\n2.reports scan\n3.BMI calculation\n4.exit\n\npick again: "));
    if(d==4):
        exit

def diet():
    message="\nenter the lifestyle disease for which recommendations of food intake and food to be avoided can be provided: "
    answer=input(message)
    s1="diabeties"
    s3="sugar"
    s2="blood pressure"
    s4="bp"

    if(answer==s1 or answer==s3):
        choice=int(input('\n1.type 1 diabeties\n2.type 2 diabeties\n\nwhich one of the above?:'));
        if (choice==1):
          import IPython.display as display
          from PIL import Image
          display.display(Image.open('Diabetes_type1.jpg'))
        if (choice==2):
          import IPython.display as display
          from PIL import Image
          display.display(Image.open('Diabetes_type2.jpg'))
    if(answer==s2 or answer==s4):
        hl=int(input('\n1.high BP\n2.low BP\n\nwhich one of the above?:'));
        if (hl==1):
          import IPython.display as display
          from PIL import Image
          display.display(Image.open('Blood_pressure_high.jpg'))
        if (hl==2):
          import IPython.display as display
          from PIL import Image
          display.display(Image.open('Blood_pressure_low.jpg'))
    print("\n") 
    ex();
  
  

def emerg():
    #playsoundmodule
    from playsound import playsound

    # for playing wav file

    n=int(input("enter 1 if its a true emergency: "))
    if(n==1):
        playsound('sos.wav');
   


m=int(input("\n1.EMERGENCY\n2.diet\n3.general diagnosis\n4.exit\n\npick one: "))
while (m!=4):
    if(m==1):
        emerg();
    elif(m==2):
        print("\nDIET\n");
        diet();
    elif(m==3):
        diagopt();
    m=int(input("\n\n1.EMERGENCY\n2.diet\n3.general diagnosis\n4.exit\n\npick again: "));
if(m==4):
    exit
