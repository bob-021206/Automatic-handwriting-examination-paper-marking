import pandas as pd
import difflib
import re
df = pd.read_excel(r"C:\Users\sunbinyan\Desktop\SRS\Software\Nanonets.xlsx") #path for paper待批阅答案路径
dg = pd.read_excel(r"C:\Users\sunbinyan\Desktop\SRS\Software\Standard_Answer.xlsx") #Path for standard answer标答路径
#standard_answer_sheet = pd.read_excel(r"C:\Users\sunbinyan\Desktop\SRS\Software\Standard_Answer.xlsx")
def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

def write_excel(path,name,data): #the function that write data back to excel
    dg = pd.DataFrame(data) #data should be a disctionary
    writer = pd.ExcelWriter(path, engine='openpyxl', mode='a') #path is the name of excel (a .xlsx file)
    dg.to_excel(writer, index=False, sheet_name = name)
    writer._save()

def remove_symbols(sentence):   #Remove numbers and symbols from ASCII
    import string
    del_estr = string.punctuation #+ string.digits  # ASCII 标点符号，数字
    replace = " "*len(del_estr)
    tran_tab = str.maketrans(del_estr, replace)
    sentence = sentence.translate(tran_tab)
    return sentence

def test_similarity(your_answer, standard_answer):
    clean_your_answer = remove_symbols(your_answer)
    clean_standard_answer = remove_symbols(standard_answer)
    similarity_score = string_similar(clean_your_answer,clean_standard_answer)
    return similarity_score

def test_structure(your_answer, standard_answer):
    #if
    standard_num_if = standard_answer.count("if")
    your_num_if = your_answer.count("if")
    #while
    standard_num_while = standard_answer.count("while")
    your_num_while = your_answer.count("while")
    #for
    standard_num_for = standard_answer.count("for")
    your_num_for = your_answer.count("for")
    #else
    standard_num_else = standard_answer.count("else")
    your_num_else = your_answer.count("else")
    #elif
    standard_num_elif = standard_answer.count("elif")
    your_num_elif = your_answer.count("elif")
    structure_score = float()
    structure_score = (your_num_if+your_num_while+your_num_for+your_num_else+your_num_elif)/(standard_num_if+standard_num_while+standard_num_for+standard_num_else+standard_num_elif)
    while structure_score > 1:
        structure_score = structure_score - 1
    return structure_score 


def grade_your_answer(your_answer, standard_answer):
    similarity = 0.3
    structure = 0.7
    final_grade = similarity*test_similarity(your_answer, standard_answer) + structure*test_structure(your_answer, standard_answer)
    return final_grade

def get_numbers_only(s1):
    num = re.sub("\D", "", s1)
    return num
    
def grade_all_answers(df,dg):
    rec_Grade = []
    grade = {"Grade": rec_Grade}
    len1 = len(df["Data"])
    len2 = len(dg["Answer"])
    i = 0
    while i<len1:
        j = 0
        while j < len2:
            
            if get_numbers_only(df["Student Name"][i]) == str(dg["Question"][j]):
                your_grade = grade_your_answer(df["Data"][i],dg["Answer"][j])*dg["Total Value"][j]
                rec_Grade.append(your_grade)
                j += 1
            else:
                j += 1
        i += 1
    return grade

if __name__ == '__main__':
    write_excel(r"C:\Users\sunbinyan\Desktop\SRS\Software\Nanonets.xlsx", 'Grade', grade_all_answers(df,dg))#path to write back
    print("Done")