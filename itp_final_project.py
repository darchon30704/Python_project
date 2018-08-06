import sys
#What to add more
#1. location of incident and nature of incident
#2. date and time module to determine the time and day
#3. create a barcode (patient ID) for each patient and ID patient
#4. tally the patients in each category(How many greens, yellow, reds, and blacks) and from there determine the number of ambulances
#5. tally how many adults and children
#6. Create a graphic user interface

#Green Category(Walking Wounded)
def initial_questions(ans):
    if ans=="Y" or ans=="y":
        triage="Green"
        print ("Triage: \033[1;42mGREEN\033[1;m:" , "Patient is classified as third priority(Walking Wounded).")
    else: #Age now is asked to determine what type of triage to use(Pediatric or Adult)
        age=int(input("What is the patient's age? If patient's age is less than 1, enter as 0: "))
        if age>8:
            print("Redirecting to Adult Triage...")
            adult_triage()
        else:
            print("Redirecting to Pediatric Triage...")
            pediatric_triage()
            pass

#Adult Triage
def adult_triage():
    def resp_adult(): #Is the patient breathing?
        quality=input("Is the patient breathing? Please check for chest rise. Answer Y if Yes and N if No: ")
        if quality=="N" or quality=="n":
            print("Try repositioning/opening the patient's airway")
            resp_qual_after=input("Is the patient now breathing? Answer Y if Yes and N if no: ") #Is the patient now breathing after repositioning?
            if resp_qual_after=="N" or resp_qual_after=="n":
                triage="Black"
                print("Triage:\033[1;47mBLACK\033[1;m","Patient is classified as fourth priority(Expectant/Deceased).")
            else:
                triage="Yellow"
                print("Triage:\033[1;43mYELLOW\033[1;m" , "Patient is classified as second priority(Delayed Treatment).")
        else: #Check number of respirations
            resp_rate=int(input("What is the respiration rate (breaths/min) of patient? Please input the number only."))
            if resp_rate > 30 or resp_rate <10:
                triage="Red"
                print("Triage: \033[1;48mRED\033[1;m", "Patient is classfied as first priority(Immediate Treatment).")
            else:
                perfusion_adult() #move to perfusion count

    def perfusion_adult(): #Does the patient have pulse?
        status=input("Does the patient have radial pulse? Please enter Y if Yes and N if No:")
        if status=="N" or status=="n":
            triage="Red"
            print("Triage: \033[1;48mRED\033[1;m", "Patient is classified as first priority(Immediate Treatment).")
        else: #Counting the heart rate
            heart_rate=int(input("What is the patient's heart rate (beats/min)?"))
            if heart_rate<60 or heart_rate>100:
                triage="Red"
                print("Triage: \033[1;48mRED\033[1;m", "Patient is classfied as first priority(Immediate Treatment).")
            else:
                cap_refill=int(input("What is the capillary refill? (in seconds). Please enter the number only: "))
                if cap_refill >2:
                    triage="Red"
                    print("Triage:\033[1;48mRED\033[1;m", "Patient is is classfied as first priority(Immediate Treatment).")
                else:
                    ment_status_adult()
    def ment_status_adult(): #Checking the mental status of the patient
        assess=input("Ask simple commands to the patient. Does the patient follow commands? Please enter Y if Yes and N if No: ")
        if assess=="N" or assess=="n":
            triage="Red"
            print("Triage:\033[1;48mRED\033[1;m", "Patient is classified as first priority(Immediate Treatment).")
        else:
            triage="Yellow"
            print("Triage:\033[1;43mYELLOW\033[1;m" , "Patient is classified as second priority(Delayed Treatment).")

    resp_adult()

#pediatric triage
def pediatric_triage():
    def resp_peds(): #Is the patient breathing?
        quality=input("Is the patient breathing? Please check for chest rise. Answer Y if Yes and N if No: ")
        if quality=="N" or quality=="n":
            print("Try repositioning/opening the patient's airway")
            resp_qual_after=input("Is the patient now breathing? Answer Y if Yes and N if no: ") #Is the patient now breathing after repositioning?
            if resp_qual_after=="Y" or resp_qual_after=="y":
                triage="Red"
                print("Triage:\033[1;48mRED\033[1;m:" , "Patient is classified as first priority(Immediate Treatment)")
            else:
                perfusion_peds()
        else: #Check number of respirations
            resp_rate=int(input("What is the respiration rate (breaths/min) of patient? Please input the number only."))
            if resp_rate > 45 or resp_rate <15:
                triage="Red"
                print("Triage: \033[1;48mRED\033[1;m", "Patient is classfied as first priority(Immediate Treatment).")
            else:
                perfusion_peds_resp() #move to perfusion count

    def perfusion_peds(): #Does the patient have pulse?
        status=input("Does the patient have palpable pulse? Please enter Y if Yes and N if No.")
        if status=="N" or status=="n":
            triage="Black"
            print("Triage:\033[1;47mBLACK\033[1;m","Patient is classified as fourth priority(Expectant/Deceased).")
        else:
            print("Perform five rescue breaths to the patient.")
            resp_after_rb=input("Is the patient now breathing? Please enter Y if Yes and N if No: ")
            if resp_after_rb=="N" or resp_after_rb=="n":
                triage="Black"
                print("Triage:\033[1;47mBLACK\033[1;m","Patient is classified as fourth priority(Expectant/Deceased).")
            else:
                triage="Red"
                print("Triage: \033[1;48mRED\033[1;m", "Patient is classfied as first priority(Immediate Treatment).")

    def perfusion_peds_resp(): #check perfusion for breathing patients
        status=input("Does the patient have palpable pulse? Please enter Y if Yes and N if No.")
        if status=="N" or status=="n":
            triage="Red"
            print("Triage: \033[1;48mRED\033[1;m", "Patient is classfied as first priority(Immediate Treatment).")
        else:
            ment_status_peds()

    def ment_status_peds(): #Checking the mental status of the patient
        avpu_assess=input("Use AVPU scale to check mental status. Is the patient alert and responsive to verbal commands or at least responsive to pain? Please enter Y if Yes and N if No: ")
        if avpu_assess=="N" or avpu_assess=="n":
            triage="Red"
            print("Triage:\033[1;48mRED\033[1;m:", "Patient is classified as first priority(Immediate Treatment).")
        else:
            triage="Yellow"
            print("Triage:\033[1;43mYELLOW\033[1;m:" , "Patient is classified as second priority(Delayed Treatment).")

    resp_peds()

ans=input("Is the patient ambulatory?(able to walk) Answer Y if Yes and N if No.")
initial_questions(ans)
