def create_table():
    data=""
    with open("Simplified_to_Traditional.txt","r",encoding="utf-8") as file:
        data=file.read().replace("=>",":")

    with open("Simplified_to_Traditional.txt","w+",encoding="utf-8") as file:
        file.write("{"+data+"}")

def get_table(Sim_to_Tr=False):
    with open("Simplified_to_Traditional.txt", "r", encoding="utf-8") as file:
        table = eval(file.read())
    if Sim_to_Tr:
        return table
    return {value:key for key,value in table.items()}


if __name__=="__main__":
    print(get_table(True))

