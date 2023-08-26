import re


 
def get_str_from_food_dict(food_dict: dict):  # to output our fulfilment msg we want to generate a str from the food dict
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result

# this is the helper function where we used regular expression to extract session id from output contexts
def extract_session_id(session_str: str):       # session str is the output context wala string
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)       # group(0) is it matches with the entire exp and group(1) is it will give us just the inside part
        return extracted_string

    return ""

# if __name__=="__main__":

#     print(extract_session_id("projects/chatora-ghel/agent/sessions/424413bf-f7bb-dabf-7d7b-6d547643c10f/contexts/ongoing_tracking"))
