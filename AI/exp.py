def rule1(symptoms):
    if 'fever' in symptoms and 'cough' in symptoms:
        return 'You may have a cold.'
    return None

def rule2(symptoms):
    if 'fever' in symptoms and 'shortness of breath' in symptoms:
        return 'You may have pneumonia.'
    return None
    
def rule3(symptoms):
    if 'nausea' in symptoms and 'weakness' in symptoms:
        return 'You may have Stomach upset.'
    return None
    
def rule4(symptoms):
    if 'headache' in symptoms and 'restlessness' in symptoms:
        return 'You may have Acid reflex.'
    return None

def medical_diagnosis(symptoms):
    rules = [rule1, rule2,rule3,rule4]
    
    for rule in rules:
        diagnosis = rule(symptoms)
        if diagnosis:
            return diagnosis
    
    return 'No specific diagnosis could be made.'

user_symptoms = input("Enter your symptoms : ")

diagnosis_result = medical_diagnosis(user_symptoms)
print(diagnosis_result)

