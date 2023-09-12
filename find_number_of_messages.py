from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    s = 0
    for i in data["messages"]:
        if str(type(i['text']))=="<class 'list'>":
            for n in i['text']:
                s+=1
        else:
            s+=1
    return s
print(find_number_of_messages(read_data('data/result.json')))