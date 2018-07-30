import sys
#Other variables
age = int(input('Enter age:'))
#ambulance is number of ambulances
ambulance = int(input('Enter number of ambulances:'))

#initiating outcome variables
#Spontaenous breathing part
#triage
answer_spontaneous_breathing = input('Is the patient spontaneously breathing? (Press N or Y): ')

values_valid= True

try:
  age = int(age)
  ambulance = str(ambulance)
except ValueError:
  sys.exit("at least one value is invalid")


#Checking if answers are N or Y.
def validity_check():
  allowed_chars = set(['N', 'Y', 'n','y'])
  if set(answer_spontaneous_breathing).issubset(allowed_chars):
    return True
    pass
  else:
    print('Enter Y or N')

#spontaneous breathing
if answer_spontaneous_breathing == 'N' or 'n':
  answer_positive_airway=input('Does the patient have a positive airway, or any form of apnea? (Enter Y or N):')
  if answer_positive_airway == 'N' or 'n':
    triage='expectant'
    print(triage)
  else:
    triage='immediate'
    print(triage)
else:
  answer_respitory_rate=int(input('What is the patients respitory rate? (Enter integer):'))
  if answer_respitory_rate > 30 :
    triage='immediate'
    print(triage)
  else:
    pass
