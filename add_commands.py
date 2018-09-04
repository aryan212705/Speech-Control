from commands import *
from priority import *
import os
import tarfile



def procedure():
    print("\nProcedure to add commands:-")
    print("1. Enter the name of command something that can be used as a function name for calling the command")
    print("2. Enter some phrases/examples for calling the command")
    print("3. Enter some keywords that can be used to recognize the command from other commands")
    print("4. If the keyword set of new command is similar to some old command then there is a need to set priority as to which command should be called in case of a conflict")
    print("5. Enter the name of a module that has the function to execute the new command")
    print("6. Confirm command addition\n")



def cmd_name_rules():
    print("\nRules for command name:")
    print("1. Name should be any valid python function name")
    print("2. Name should not previously in use\n")



def cmd_name_validity(cmd):
    if cmd.isidentifier():
        return True
    return False



def input_cmd_name():
    cmd = input("Enter the command name : ")
    if cmd_name_validity(cmd):
        return cmd
    print("The command name was invalid!!")
    return input_cmd_name()



def calling_phrase_rules():
    print("\nRules for writing the phrases used to call the command:")
    print("1. Phrases should be short")
    print("2. It should avoid usage of articles and helping verbs")
    print("3. It should contain only English words separated by spaces")
    print("4. Should have some keywords(Example: Open Terminal in Downloads)\n")



def string_validity(phrase):
    for i in phrase:
        if ord(i) not in range(65, 91) and ord(i) not in range(97, 123) and ord(i) != 32:
            return False
    return True



def input_string(string):
    n = int(input("Enter the number of " + string + " : "))
    phrases = []
    i = 0
    while i < n:
        phrase = input("Enter the " + string + " : ")
        if string_validity(phrase):
            phrases.append(phrase.lower())
            i += 1
        else:
            print("Phrase not valid!!\nPlease enter the correct phrase!!")
    return phrases



def input_phrase():
    calling_phrase_rules()
    phrases = input_string("phrases")
    return phrases



def keywords_rules():
    print("\nRules for writing keywords for each command:")
    print("1. Keywords should be entered the form of phrases")
    print("2. Order of keywords should not matter in the command")
    print("3. Keywords should be separated by spaces")
    print("Example: For command 'open terminal in downloads', keywords are:-\n\topen terminal downloads\n")



def input_keywords():
    keywords_rules()
    keywords_set = input_string("keyword phrases")
    keywords = []
    for string in keywords_set:
        string = string.split()
        keywords.append(string)
    return keywords



def priority_validation(keywords, cmd_name):
    global commands
    similar_cmd = set()
    for cmd in commands.keys():
        for key_set in commands[cmd]:
            flag = 0
            for i in keywords:
                if set(key_set).issubset(set(i)) or set(key_set).issuperset(set(i)):
                    flag = 1
                    similar_cmd.add(cmd)
                    break
            if flag:
                break
    if len(similar_cmd):
        print("The keywords for this command matches with the following commands:-")
        for i in similar_cmd:
            print(i)
    else:
        print("There is no priority issue!!")
    j = 0
    similar_cmd = list(similar_cmd)
    while j < len(similar_cmd):
        i = similar_cmd[j]
        print("Enter the choice which has higher priority:")
        print("1.", cmd_name)
        print("2.", i)
        choice = int(input())
        if choice == 1:
            if cmd_name in priority.keys():
                priority[cmd_name].append(i)
            else:
                priority.update({cmd_name:[i]})
        elif choice == 2:
            if i in priority.keys():
                priority[i].append(cmd_name)
            else:
                priority.update({i:[cmd_name]})
        else:
            j -= 1
        j += 1



def new_dictionary(phrases, keywords):
    for i in keywords:
        phrases.append(" ".join(i))
    with open("dictionary") as f:
        with open("new_dictionary", "w") as f1:
            for line in f:
                f1.write(line)
    with open("new_dictionary", "a") as f1:
        for i in range(len(phrases) - 1):
            f1.write(phrases[i])
            f1.write("\n")
        f1.write(phrases[-1])



def get_files():
    print("Running lmtool, wait for few seconds...")
    os.system("lmtool new_dictionary")
    files = os.listdir(os.curdir)
    temp = []
    for f in files:
        if f.endswith(".tgz"):
            temp.append([os.path.getmtime(f), f])
    temp.sort(reverse = True)
    tar = tarfile.open(temp[0][1], 'r')
    files = []
    for member in tar.getmembers():
        if ".dic" in member.name or ".lm" in member.name:
            tar.extract(member)
            files.append(member.name)
    tar.close()
    return files



def function_rules():
    print("\nThe rules for the module that contains the functions:-")
    print("1. The module must contain a function by the name of the command")
    print("2. The module can have any number of functions")
    print("3. The functions should not have any compilation errors")
    print("4. The module should be properly tested\n")



def get_module():
    module = input("Enter the module name along with the extension : ")
    files = os.listdir(os.curdir)
    if module in files:
        return module.split('.')[0]
    print("Module not found!!")
    return get_module()    



def confirm():
    ans = input("Do you want to confirm this operation?(y/n) : ")
    if ans == 'Y' or ans == 'y' or ans == '':
        return True
    return False



def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.rename('newfile.txt',originalfile)



def change_script(module):
    add = "from " + module + " import *\n"
    insert("scripts.py", add)



def change_commands(cmd, keywords):
    global commands
    commands.update({cmd : keywords})
    with open("commands.py", 'w') as f:
        f.write("commands = ")
        print(commands, file = f)



def change_priority():
    global priority
    with open("priority.py", 'w') as f:
        f.write("priority = ")
        print(priority, file = f)



def mk_copy():
    time = int(time.time())
    os.mkdir(time)
    os.rename("en-us.dic", time + "/en-us.dic")
    os.rename("en-us.lm", time + "/en-us.lm")
    os.rename("dictionary", time + "/dictionary")
    os.rename("scripts.py", time + "/scripts.py")
    os.rename("commands.py", time + "/commands.py")
    os.rename("priority.py", time + "/priority.py")



def rename_files(files):
    os.rename(files[0],"en-us.dic")
    os.rename(files[1],"en-us.lm")
    os.rename("new_dictionary", "dictionary")




if __name__ == "__main__":
    
    procedure()    #print the entire procedure for command addition
    cmd_name_rules()    #print rules for command name
    cmd = input_cmd_name()    #take command name from user
    phrases = input_phrase()    #input phrases from the user
    keywords = input_keywords()    #input keywords from the user
    priority_validation(keywords, cmd)    #check for priority issues if any and asks the user to resolve them
    function_rules()     #print rules for the function file
    module = get_module()    #get module name from user
    if confirm():    #ask user to confirm the operation
        new_dictionary(phrases, keywords)    #creates a new_dictionary for lmtool
        files = get_files()    #use new_dictionary with lmtool to improve model
        mk_copy()    #make copy of previous files
        change_script(module)    #adds the new module to the scripts.py file
        change_commands(cmd, keywords)    #adds the new command to the commands dictionary in commands.py file
        change_priority()    #make changes to the priority dictionary
        rename_files(files)    #rename files(dictionary, en-us.dic, en-us.lm) for the new model
        print("\nYour new model is ready!!")
    else:
        print("Aborted")
