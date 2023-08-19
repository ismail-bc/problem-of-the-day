import json

f = open("EX_json.json","a")
datax = {"Counrty": [
        {"Counrty_N": "oman", "pop": "5"},
        {"Counrty_N": "usa", "pop": "340"},
        {"Counrty_N": "uk","pop": "70"},
        {"Counrty_N": "m","pop": "10"},
        {"Counrty_N": "q","pop": "25"}] }

data = json.load(f)
json.dump(data,datax,indent = 4)

for i in data["Counrty"]:
    print(i)
 
f.close()
print("###############################")

def Enp():
    with open("EX_json.json","r+") as file:
        EorR = input("do you want to enter(e), remove(r) a country or exit(x)?: ")
    
        if EorR == "e":
            def ENew():
                y = input("Enter a country name you want to insert into the json file: ")
                yy = input("Enter a country population you want to insert into the json file: ")
                x = {"Counrty_N" : f"{y}", "pop" : f"{yy}"}
                file_data = json.load(file)
                if x not in file_data["Counrty"]:
                    file_data["Counrty"].append(x)
                    file.seek(0)
                    json.dump(file_data, file, indent = 4)
                    again = input("Do you want to enter another one?: (yes,no)")
                    if again == "yes":
                        ENew()
                else:
                    print("It already exisits")
                    ENew()
            ENew()
        elif EorR == "r":
            def Rem():
                y = input("Enter a country name you want to remove from the json file: ")
                file_data = json.load(file)
                for i in file_data["Counrty"]:
                    for key,value in i.items():
                        if value == y:
                            file_data["Counrty"].remove(i)
                            file.seek(0)
                            open("EX_json.json","w")
                            json.dump(file_data, file,indent = 4)
                            again = input("Do you want to remove another one?: (yes,no)")
                            if again == "yes":
                                Rem()
                            else:
                                print("Ok")
                        else:
                            print("It do not exisits")
                            z = input("Again? (yes/other): ")
                            if z == "yes":
                                Rem()
                            else:
                                Exit = True
                                break
                    if Exit:
                        break
            Rem()
        else:
            print("Ok")
Enp()

f = open("EX_json.json")
data = json.load(f)
for i in data["Counrty"]:
    print(i)
f.close()