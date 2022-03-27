# Name: Sanchit Kripalani
# Batch: M1 
# Roll No: 31145

# Healthcare Expert System
# We will be using experta, which is a python libarary to 
# implement Rule-Based expert systems using Python.
# It is similar to CLIPS language, which is the most popular 
# Language to implement Rule-Based logic.
from experta import *

# This expert systems aims at identifying whether a patient has a cold
# or a flu. Flu is caused only by influenza based viruses while common cold 
# can be caused by a number of viruses. 
# Cold is usually a milder disease as compared to Flu, hence the symptoms of 
# of Flu are stronger.  

# Note here that the class must be subclass of KnowledgeEngine
class FluOrCold(KnowledgeEngine):

   def __init__(self):
      self.flu_symptoms = 0
      self.clod_symptoms = 0
      super().__init__()

	# Expert systems needs a set of Facts to be present for the system to work.
	# DefFacts is called every time the reset method is called.
   @DefFacts()
   def symptoms(self):
      yield Fact(action="flu_or_cold")

   # <---- Defining rules to classify as Cold ----> 

   # Cold Symptoms
   # Fever
   @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="no fever"),
             Fact(symptom="mild fever"),
             Fact(symptom="low temperature"),
             Fact(symptom="mild temperature"),
             Fact(symptom="no hyperthermia"),
             Fact(symptom="mild hyperthermia"),
             Fact(symptom="no pyrexia"),
             Fact(symptom="mild pyrexia")))
   def fever_cold(self):
       global cold_symptoms
       cold_symptoms +=  1

   # Coughing
   @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="dry cough"),
             Fact(symptom="mucus cough")))
   def coughing_cold(self):
       global cold_symptoms
       cold_symptoms +=  1

   # Nasal discharge
   @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="stuffy nose"),
             Fact(symptom="runny nose")))
   def nasal_discharge_cold(self):
       global cold_symptoms
       cold_symptoms += 1

   # Tiredness
   @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="mild tiredness"),
             Fact(symptom="mild fatigue"),
             Fact(symptom="mild exhaustion")))
   def tiredness_cold(self):
       global cold_symptoms
       cold_symptoms += 1

   # Headache
   @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="headache"),
           Fact(symptom="mild headache"),
           Fact(symptom="mild migraine"),
           Fact(symptom="mild head pain")), salience=0)
   def headache_cold(self):
       global cold_symptoms
       cold_symptoms += 1

   # Dizziness
   @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="no lightheadedness"),
            Fact(symptom="no syncope"),
            Fact(symptom="no fainting"),
            Fact(symptom="no dizziness")))
   def dizziness_flu(self):
       global cold_symptoms
       cold_symptoms += 1

   # Nausea
   @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="no nausea"),
            Fact(symptom="no vomiting"),
            Fact(symptom="no stomach upset"),
            Fact(symptom="no sickness"),
            Fact(symptom="no low appetite")))
   def nausea_cold(self):
       global cold_symptoms
       cold_symptoms += 1 

	# <---- End of Symptom rules for Cold ---->    


   # <---- Defining rules to claasify as Flu ----> 

   # Flu Symptoms
   # Fever
   @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="high fever"),
            Fact(symptom="moderate fever"),
            Fact(symptom="high temperature"),
            Fact(symptom="moderate temperature"),
            Fact(symptom="high hyperthermia"),
            Fact(symptom="moderate hyperthermia"),
            Fact(symptom="high pyrexia"),
            Fact(symptom="moderate pyrexia")))
   def fever_flu(self):
        global flu_symptoms
        flu_symptoms += 1

   # Coughing
   @Rule(Fact(action='flu_or_cold'),
         Fact(symptom="dry cough"))
   def coughing_flu(self):
       global flu_symptoms
       flu_symptoms += 1

   # Nasal discharge
   @Rule(Fact(action='flu_or_cold'),
          Fact(symptom="runny nose"))
   def nasal_discharge_flu(self):
       global flu_symptoms
       flu_symptoms += 1

   # Tiredness
   @Rule(Fact(action='flu_or_cold'),
          OR(Fact(symptom="moderate tiredness"),
             Fact(symptom="severe tiredness"),
             Fact(symptom="moderate fatigue"),
             Fact(symptom="severe fatigue"),
             Fact(symptom="moderate exhaustion"),
             Fact(symptom="severe exhaustion")))
   def tiredness_flu(self):
       global flu_symptoms
       flu_symptoms += 1

   # Headache
   @Rule(Fact(action='flu_or_cold'),
        OR(Fact(symptom="headache"),
           Fact(symptom="moderate headache"),
           Fact(symptom="severe headache"),
           Fact(symptom="moderate migraine"),
           Fact(symptom="severe migraine"),
           Fact(symptom="moderate head pain"),
		   # Salience = 1 will mean that this rule will be prioritized and thus fired first
           Fact(symptom="severe head pain")), salience=1)
   def headache_flu(self):
       global flu_symptoms
       flu_symptoms += 1

   # Dizziness
   @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="lightheadedness"),
            Fact(symptom="syncope"),
            Fact(symptom="fainting"),
            Fact(symptom="dizziness")))
   def dizziness_flu(self):
       global flu_symptoms
       flu_symptoms += 1

   # Nausea
   @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="nausea"),
            Fact(symptom="vomiting"),
            Fact(symptom="stomach upset"),
            Fact(symptom="sickness"),
            Fact(symptom="low appetite")))
   def nausea_cold(self):
       global flu_symptoms
       flu_symptoms += 1

   # Common Symptoms (These symptoms are common to both cold and flu)
   # Sneezing
   @Rule(Fact(action='flu_or_cold'),
         Fact(symptom="sneezing"))
   def sneezing_cold_flu(self):
       global cold_symptoms
       cold_symptoms += 1
       global flu_symptoms
       flu_symptoms += 1


   # Sore Throat
   @Rule(Fact(action='flu_or_cold'),
         OR(Fact(symptom="pain throat"),
            Fact(symptom="throat sore"),
            Fact(symptom="sore throat")))
   def sore_throat_cold_flu(self):
       global cold_symptoms
       cold_symptoms += 1
       global flu_symptoms
       flu_symptoms += 1

      
# Output
flu_symptoms = 0
cold_symptoms = 0

print("\nSymptom Anaylzer Expert System".center(20, " "))
print("Note ".center(40, "-"))
print ("Enter one symptom in line ".center(40, "-"))
print ("Enter (done) to show your state ".center(40, "-"))
print(" ")

# Create an Engine object
engine = FluOrCold()

while(1):
    symptom = input("Enter a Symptom you have: ")
    # Exit from loop if the input equal "done"
    if symptom.strip().lower() == "done":
       break
    engine.reset()  #  Prepare the engine for the execution.
    engine.declare(Fact(symptom=symptom.strip().lower()))
    engine.run()  #  Run it

    print(flu_symptoms)
    print(cold_symptoms)
    print()

# Check if user enter less than 3 symptoms      
if ((flu_symptoms < 3) and (cold_symptoms < 3)):
    print("You must enter at least 3 symptoms")
# Cann't diagnose user state when the flu and cold symptoms are equal 
elif((flu_symptoms== cold_symptoms)):
    print("Can't diagnose your state")
# If the flu counter greater than cold counter, then the user has flu
elif ((flu_symptoms > 3) and (flu_symptoms > cold_symptoms)):
    print ("You have flu")
# If the cold counter greater than flu counter, then the user has cold
elif ((cold_symptoms > 3) and (flu_symptoms < cold_symptoms)):
    print ("You have cold")