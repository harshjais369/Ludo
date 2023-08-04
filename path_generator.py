def genPath(start_point, colour):
    ls = []
    for i in range(start_point, 53):
        if start_point == 1 and i == 52:
            break
        ls.append(f'c{i}')
    if len(ls) != 51:
        for i in range(1, 52):
            if len(ls) == 51:
                break
            ls.append(f'c{i}')
    for i in range(1, 6):
        ls.append(f'c{colour}{i}')
    print(f'Total cells: {len(ls)}')
    return ls


rpath = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13', 'c14', 'c15', 'c16',
'c17', 'c18', 'c19', 'c20', 'c21', 'c22', 'c23', 'c24', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30', 'c31', 'c32',
'c33', 'c34', 'c35', 'c36', 'c37', 'c38', 'c39', 'c40', 'c41', 'c42', 'c43', 'c44', 'c45', 'c46', 'c47', 'c48',
'c49', 'c50', 'c51', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5']

strt = int(input('Start from: '))
clr = str(input('Colour code: '))
print(genPath(strt, clr))
