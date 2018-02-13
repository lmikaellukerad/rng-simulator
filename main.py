import math
import collections

running = True

list_ftl = [(777, 'Argent'), (324, 'Brasi'), (631, 'Rebecca'), (789, 'Eidan_Nawtsuji'), (250, 'Clandestine_Philosophies'), (500, 'Clandestine_Philosophies'), (750, 'Clandestine_Philosophies'), (278, 'Sad_Lucio'), (642, 'Sad_Lucio'), (795, 'Sad_Lucio'), (501, 'Cole_MacGrath³')]
list_civ = [(400, 'Gargamel'), (730, 'Gargamel'), (167, 'Gargamel'), (777, 'Rebecca'), (400, 'Cole_MacGrath'), (600, 'Cole_MacGrath'), (483, 'Amnestics'), (666, 'Why_do_I_even_try'), (333, 'kaiyogenesis'), (17, 'Technicolour'), (269, 'Technicolour'), (700, 'Technicolour'), (347, 'Teklogikal'), (99, 'Teklogikal'), (913, 'CryBaby'), (613, 'CryBaby'), (313, 'CryBaby'), (115, 'Greatatemi'), (263, 'Greatatemi'), (21, 'Irisaurus_Rex'), (4, 'DannyNight'), (47, 'DannyNight'), (457, 'DannyNight'), (333, 'Clarque'), (667, 'Clarque'), (408, 'Trinx'), (783, 'Trinx'), (885, 'Trinx'), (230, 'CHICKEN_NUGGET'), (923, 'CHICKEN_NUGGET'), (444, 'CHICKEN_NUGGET'), (333, 'Argent'), (555, 'Argent'), (777, 'Argent'), (873, 'Rhiana'), (137, 'ramaster00'), (259, 'ramaster00'), (579, 'ramaster00'), (251, 'Noldaru'), (466, 'Noldaru'), (885, 'Noldaru'), (145, 'Encoded'), (146, 'Encoded'), (147, 'Encoded'), (2, 'idealspark'), (998, 'idealspark'), (453, 'idealspark'), (719, 'Punkek_the_Snek'), (195, 'Punkek_the_Snek'), (44, 'Punkek_the_Snek'), (666, 'stixx'), (968, 'stixx'), (158, 'stixx'), (456, 'Yuurri23')]
list_numbers = list_ftl


def list_to_dict(l):
    d = collections.defaultdict(list)
    for item in l:
        d[item[0]].append(item[1])
    return d


def get(item):
    return item[0]


def print_results(x):
    print("Percentage chance of each entrant for being selected after the first round")
    for k, v in x.items():
        print(k + ": " + "%.2f" % ((v/1000)*100) + "%")


def calculate(y):
    list_sorted = sorted(y, key=get)
    dict_chances = {}
    first = list_sorted[0]
    for entrant in first[1]:
        dict_chances[entrant] = dict_chances.get(entrant, first[0])
    total = first[0]
    for i in range(0, len(list_sorted)):
        entry = list_sorted[i]
        if i + 1 < len(list_sorted):
            next_entry = list_sorted[i + 1]
            for entrant in entry[1]:
                dict_chances[entrant] = dict_chances.get(entrant, 0) + math.ceil((next_entry[0] - entry[0])/2)
            for entrant in next_entry[1]:
                dict_chances[entrant] = dict_chances.get(entrant, 0) + math.ceil((next_entry[0] - entry[0])/2)
            total = total + math.ceil(next_entry[0] - entry[0])
        else:
            for entrant in entry[1]:
                dict_chances[entrant] = dict_chances.get(entrant, 0) + 1000 - entry[0]
            total = total + 1000 - entry[0]
    print_results(dict_chances)


def process(x):
    split_command = x.split()
    print(len(split_command))
    if len(split_command) in range(2, 5):
        name = split_command[0]
        if type(name) is str:
            for i in range(1, len(split_command)):
                try:
                    number = int(split_command[i])
                    list_numbers.append((number, name))
                except ValueError:
                    return False
            return True
    return False


while running:
    command = input()
    if command == "exit":
        running = False
    elif command == "reset":
        list_numbers = []
    elif command == "calculate":
        calculate(list_to_dict(list_numbers).items())
    elif command == "list":
        print(sorted(list_to_dict(list_numbers).items(), key=get))
    elif process(command):
        print(list_numbers)
    else:
        print("invalid")








