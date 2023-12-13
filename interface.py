import engine
import defaults


def simple_output(image_path, town, state, object, personality):
    answer, object, details, prompt_tokens, completion_tokens, total_tokens = recycle_check(image_path, town, state, object, personality)
    return to_text(answer, object, details, prompt_tokens, completion_tokens, total_tokens)


def to_text(answer, object, details, prompt_tokens=0, completion_tokens=0, total_tokens=0):
    header = ""
    result_code = -1
    
    #Result Code: 0 = no, 1 = maybe, 2 = yes       

    if "but" in answer:
        header += ("Is this " + object + " recyclable? " + answer + "\n")
        result_code = 1
    
    elif(answer=="No, but..." or answer=="No, probably not." or answer=="No."):
        header += ("Is this " + object + " recyclable? " + answer + "\n")
        result_code = 0

    else:
        header += ("Is this " + object + " recyclable? " + answer + "!\n")
        result_code = 2
    
    ###
    
    wantCost = prompt_tokens!=0 and completion_tokens!=0 and total_tokens!=0
    
    if wantCost:
        totalCost = engine.getCost(prompt_tokens, completion_tokens)
        costOutput = ("Prompt tokens: " + str(prompt_tokens) + ". " "Completion tokens: " + str(completion_tokens) + ". " "Total tokens: " + str(total_tokens) + ". Total cost: $" + str(totalCost))

    return_tuple = (result_code, object, header, details)
    if wantCost:
        return_tuple = return_tuple + (costOutput,)

    return return_tuple

        

def recycle_check(image_path, town="", state="", object=defaults.getDefaultObject(), personality=defaults.getDefaultPersonality()):
        
    raw_response= engine.query_recycling_info(image_path, town, state, object, personality)
    print("Recycle_check: " + str(raw_response))
    message = engine.extract_message(raw_response)
    answer, object, details = engine.separate_answer_and_details(message)
    
    # tokens are number (not string)
    prompt_tokens, completion_tokens, total_tokens = engine.numTokens(raw_response)
    
    return_tuple = (answer, object, details, prompt_tokens, completion_tokens, total_tokens)
    
    return return_tuple

