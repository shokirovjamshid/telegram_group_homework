from read_data import read_data
from find_all_users_name import find_all_users_name

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    count_message = {}
    for n in users_id:
        count_message[n]=0
    for i in data["messages"]:
        if "actor" in i.keys():
            if str(type(i['text']))=="<class 'list'>":
                for n in i['text']:
                    count_message[i['actor']]+=1
            else:
                count_message[i['actor']]+=1
        else:
            if str(type(i['text']))=="<class 'list'>":
                for n in i['text']:
                    count_message[i['from']]+=1
            else:
                count_message[i['from']]+=1
        
    return count_message
print(find_user_message_count(read_data('data/result.json'),find_all_users_name(read_data('data/result.json'))))