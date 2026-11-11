from pyscript import document, display


def candidate_checker(e):
    club_members = ['chester roxas', 'joel gonzales', 'ezekiel backay', 'joseph co', 'franco maglaqui', 'rene butterbonia', 'rene buterbonia', 'jarence manacap']

    ft_name = document.getElementById('first_name').value
    lt_name = document.getElementById('last_name').value
    candidate = f'{ft_name} {lt_name}'.strip()
    member_checker = candidate.lower() in club_members
    messages = (f'Sorry {candidate}, your name is not on the list.', f'Congratulations {candidate}! You are now part of the ICT club.')
    document.getElementById('result').innerText = messages[member_checker]


def result_checker(e):
    document.getElementById('output').innerHTML = ""

    # Grade level sets with student names
    grade7 = {'Taranbir Singh', 'Rafael Magdayao', 'Lucas Flores'}
    grade8 = {'Joseph Co', 'Joel Gonzales', 'Jarence Manacap', 'Jaden Galvez'}
    grade9 = {'Hans Baquiran', 'Franco Maglaqui', 'Chester Roxas'}
    grade10 = {'Amanda Bower', 'Luis Bacay', 'Cedric Visorde', 'Savannah Reyes'}

    # Retrieve and clean up input values
    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()

    new_member = f'{first_name} {last_name}'.title()
    new_members_set = {new_member}

    all_members = grade7 | grade8 | grade9 | grade10 | new_members_set
    total_members = len(all_members)

    members_list = "<br>".join(sorted(all_members))

    document.getElementById('output').innerHTML = f'All members:<br>{members_list}'
    display(f'Total members: {total_members}', target='output')


# Non-Metal elements
non_metals = {
    "H":  ("Hydrogen",   1,   1.008),
    "He": ("Helium",     2,   4.0026),
    "C":  ("Carbon",     6,   12.011),
    "N":  ("Nitrogen",   7,   14.007),
    "O":  ("Oxygen",     8,   15.999),
    "F":  ("Fluorine",   9,   18.998),
    "Ne": ("Neon",      10,   20.180),
    "P":  ("Phosphorus", 15,   30.974),
    "S":  ("Sulfur",     16,   32.06),
    "Cl": ("Chlorine",   17,   35.45),
    "Ar": ("Argon",      18,   39.948),
    "Se": ("Selenium",   34,   78.971),
    "Br": ("Bromine",    35,   79.904),
    "Kr": ("Krypton",    36,   83.798),
    "I":  ("Iodine",     53,   126.90),
    "Xe": ("Xenon",      54,   131.29),
    "At": ("Astatine",   85,   210),
    "Rn": ("Radon",      86,   222),
    "Ts": ("Tennessine", 117,  294),
    "Og": ("Oganesson",  118,  294)
}


def element_checker(e):
    symbol = document.getElementById('element_name').value.strip().title()
    
    result = non_metals.get(symbol, ("Element Not Found", "-", "-"))

    if result[0] == "Element Not Found":
        document.getElementById('result').innerText = "Element Not Found"
    else:
        document.getElementById('result').innerHTML = f"""
            Symbol: {symbol}<br>
            Name: {result[0]}<br>
            Atomic Number: {result[1]}<br>
            Atomic Mass: {result[2]}
        """