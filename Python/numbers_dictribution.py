last_name_dict = {
    'Аля': {'theory': [], 'practice': []},
    'Даня': {'theory': [], 'practice': []},
    'Андрей': {'theory': [], 'practice': []},
    'Серега': {'theory': [], 'practice': []},
    'Денис': {'theory': [], 'practice': []},
}

N_THEORETICAL = 32
N_PRACTICAL = 0


def counter(N: int, last_name_dict: dict, type: str) -> dict:
    temp = 1
    while N > temp:
        for item in last_name_dict:
            if temp > N:
                break
            last_name_dict[item][type].append(temp)
            temp += 1

    return last_name_dict


def print_dict(data: dict) -> None:
    for item in data:
        print(f'{item}', end=': ')
        temp = ''
        for elem in data[item]:
            temp += f'{elem} {data[item][elem]} - '
        print(temp[:-2])


def print_the_only_key(data: dict, key: str) -> None:
    for item in data:
        print(f'{item}: {data[item][key]}')


def relocate_data(data: dict, N: int) -> dict:
    length = len(data)
    difference = N % length
    temp = []
    for key in data:
        if difference > 0:
            temp.append(key)
            difference -= 1
        else:
            break

    for key in temp:
        data[key] = data.pop(key)

    return data


if __name__ == '__main__':
    theoretical_part = counter(N_THEORETICAL, last_name_dict, 'theory')
    relocated = relocate_data(last_name_dict, N_THEORETICAL)
    practical_plus_theoretical = counter(N_PRACTICAL, last_name_dict, 'practice')
    relocated2 = relocate_data(last_name_dict, N_PRACTICAL)
    relocated3 = relocate_data(last_name_dict, N_THEORETICAL)
    # print_dict(practical_plus_theoretical)
    print_the_only_key(practical_plus_theoretical, 'theory')
