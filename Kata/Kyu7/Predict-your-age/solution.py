import math 

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age_list = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    new_age_list = age_list
    #Ugly but OK
    new_age_list[0] = new_age_list[0]*new_age_list[0]
    new_age_list[1] = new_age_list[1]*new_age_list[1]
    new_age_list[2] = new_age_list[2]*new_age_list[2]
    new_age_list[3] = new_age_list[3]*new_age_list[3]
    new_age_list[4] = new_age_list[4]*new_age_list[4]
    new_age_list[5] = new_age_list[5]*new_age_list[5]
    new_age_list[6] = new_age_list[6]*new_age_list[6]
    new_age_list[7] = new_age_list[7]*new_age_list[7]
    
    #summerize
    age_int = sum(new_age_list)
    new_age_int = math.sqrt(age_int)
    new_age_int = new_age_int/2
    new_age_int = math.floor(new_age_int)
    new_age_int = int(new_age_int)
    #print
    return new_age_int
