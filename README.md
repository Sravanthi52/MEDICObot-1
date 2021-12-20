# MEDICObot
FRAMEWORK,TOOL AND TECHNOLOGIES
This program was developed using and will run on python(idle shell 3.10,64 bit)on windows 11 , and the following modules were imported:
1. cv2 (to read the image for report scanning)
2.pytesseract (for image to string conversion in report scanner function)
3. re (verify set of strings and match it)
4.IPython.display (used in diet module of the  program)
5.playsound (to play the audio file for emergency module)
Note: tesseract.exe had to be downloaded to execute pytesseract.


WORKING:-
Upon activation , the screen would display 3 options:
1.Diagnosis
2.EMERGENCY
3.Diet 
EMERGENCY:
The emergency module is an option for when you are in a life and death situation and are in no position to call for help.
 As soon as the module is picked, the user will be asked if its truly an emergency . If the answer is yes , an uninterruptable audio will be played to call for attention of a passerby.
If the answer is no , the user will be redirected back to the options screen.
DIAGNOSIS:
If diagnosis is chosen , 3 options would be displayed:
          1.symptoms
          2.reports scanner
          3.BMI
Symptoms: upon choosing this option , the person would be asked a  series of multiple choice questions regarding the patient and condition ,and would be recommended a  doctor(oncologist ,dermatologist , etc.)based on the responses received.
Reports scanner: this would scan numerical data related reports and convert the image to text and then take in the values . after taking the values , it will check whether they fall in healthy ranges , and store the ones that don’t , and then calculate the deficiencies and excesses . After calculating , the condition is displayed(this condition can be copy pasted in the diet column and a diet can be charted).
BMI: this would calculate the body mass index from inputs of height and weight, and compare with the ranges and calculate if the person is underweight or overweight.
DIET: if this option is chosen , the person would be asked the condition they have. Next they would be asked if they want a veg diet or a non veg diet, and a diet would be displayed accordingly and it will recommend foods to consume and foods to avoid.



