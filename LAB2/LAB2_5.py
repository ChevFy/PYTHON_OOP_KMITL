import json

def update_records(data):
    try:
        record, record_id, property_name, value = data.split('|')

        record = record.strip()
        record_id = record_id.strip()
        property_name = property_name.strip()
        value = value.strip()

        record = record.replace("'", '"')
        new_record = json.loads(record)

        
        if property_name not in ["tracks","albumTitle","artist"] : return "Invalid"

        if  record_id in [ '0' ,'-1' ] : return "Invalid"

        if record_id not in new_record:
         
            new_record[record_id] = {}

        album = new_record[record_id]
        
        if value == '"' or value == "'" or value == '""' or value == "''" : 
            if property_name not in album : return "Invalid"
            else : 
                album.pop(property_name)
        elif property_name == "tracks":
            if "tracks" not in album:
                album["tracks"] = []  
            album["tracks"].append(value)
        else:
            album[property_name] = value  

        return new_record
    except :
        return "Invalid"

value = input()
print(update_records(value))
