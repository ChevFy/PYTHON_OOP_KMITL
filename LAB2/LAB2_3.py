import json

def something(data):
    def add_score(data):
        if data.count('|') != 2:
            return 'Invalid'
        ex_dict, key, value = data.split('|')
        if "'" not in key : return "Invalid" 
        ex_dict = ex_dict.strip()
        key = key.replace(" " , "")
        key = key.replace("'","")
        ex_dict = ex_dict.replace("'", '"')
        
        if int(value) < 0 or key == '':
            return json.loads(ex_dict)

        try:
            new_dict = json.loads(ex_dict)  
            new_dict[key] = int(value)  
            return new_dict
        except :
            return 'Invalid'

    def calc_average_score(new_dict):
        count = 0
        sum_val = 0
        for value in new_dict.values():
            sum_val += value  
            count += 1  
        if count == 0: 
            return f"{0:.2f}"
        final = sum_val / count   
        return f"{final:.2f}"

    try:
        output = add_score(data)  
        if output == 'Invalid':
            return ('Invalid')
        else:
            output2 = calc_average_score(output) 
            return ("{0}, Average score: {1}".format(output,output2))  
    except:
        return ('Invalid')


value = input()
print(something(value))