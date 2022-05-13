m = int(input('m int >> '))
n = int(input('n int >> '))
fam_m = {input(f'm | #{_} str >> ') for _ in range(m)}
fam_n = {input(f'n | #{_} str >> ') for _ in range(n)}
print(f'Only m: {m - len(fam_m & fam_n)}')
