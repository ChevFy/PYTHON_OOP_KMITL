import json

def something(data):
    def add_score(data):
       
        parts = data.split('|')
        if len(parts) != 4:  return 'Invalid'

        ex_dict, student, key, value = map(str.strip, parts)

        if len(student) != 10 : return 'Invalid' 

        if not key.startswith("'") or not key.endswith("'"):
            return 'Invalid'

        key = key.strip("'") 
        student = student.strip("'") 
        try:
            value = int(value)
            if value < 0  :
                return 'Invalid'
        except :
            return 'Invalid'

        try:
            ex_dict = ex_dict.replace("'", '"')
            new_dict = json.loads(ex_dict)
            
            if student not in new_dict:
                new_dict[student] = {}

            if key == '' : return 'Invalid'

            if key not in new_dict[student]:
                new_dict[student][key] = value 
            else :
                new_dict[student][key] = value 

            return new_dict
        except :
            return 'Invalid'

    def calc_average_score(new_dict):
        average_scores = {}
        for student, subjects in new_dict.items():
            total_score = sum(subjects.values())  
            count = len(subjects)  
            average = total_score / count if count > 0 else f"{0:.2f}"
            average_scores[student] = f"{average:.2f}"  
        return average_scores

    try:
        output = add_score(data)
        if output == 'Invalid':
            return 'Invalid'
        else:
            average_score = calc_average_score(output)
            return f"{output}, Average score: {average_score}"
    except :
        return 'Invalid'


value = input()
print(something(value))
