list_state_capital: {
    'state'       'capital',
    'Abia'        'Umuahia',
    'Adamawa'       'Yola',
    'Akwa_Ibom'     'Uyo',
    'Bauchi'       'Bauchi',
    'Bayelsa'    'Yenagoa',
}
x = 'parach'
print(x)

Place1 = {
    'state': 'Abia',
    'capital': 'Umuahia',
    }

place2 = {
    'state': 'Adamawa',
    'capital': 'Yola',
}

place3 = {
    'state': 'Akwa-Ibom',
    'capital': 'Uyo',
}

place4 = {
    'state': 'Bauchi',
    'capital': 'Bauchi',
}

place5 = {
    'state': 'Bayelsa',
    'capital': 'Yenagoa',
}

user = input('Enter state and capital: ')
def list_of_sc(state, capital):
    print(f'Name is {state}, and its {capital}')

    list_of_sc('Abia', 'Umuahia')
    list_of_sc('Adamawa', 'Yola')
    list_of_sc('Akwa-Ibom', 'Uyo')
    list_of_sc('Bauchi', 'Bauchi')


def list_state_capital():
    state = []
    capital = []

    for i in range(5):
        state = input('Enter a state: ')
        capital = input('Enter its capital: ')
        state.append(state)
        capital.append(capital)
    return state, capital
state, capital = list_state_capital()
print('state:', state)
print('captal:', capital)


prompt