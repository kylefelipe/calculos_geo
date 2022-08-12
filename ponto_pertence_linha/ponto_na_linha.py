# Verifica se o ponto pertençe a reta
def equacao_reta(inicio, fim, p):
    print(inicio)
    print(fim)
    print(p)
    xa, ya = inicio
    xb, yb = fim
    xp, yp = p

    matriz = [
        [xp, yp, 1],
        [xa, ya, 1],
        [xb, yb, 1]
    ]
    parte_1 = (xp * ya) + (yp * xb) + (yb * xa)
    parte_2 = (ya * xb) - (yb * xp) - (xa * yp)
    eq_reta = parte_1 - parte_2
    a = ya - yb
    b = xb - xa
    c = (xa * yb) - (xb * ya)
    abc = (a * xp) + (b * yp) + c
    print(f"Parte 1 = {parte_1}")
    print(f"Parte 2 = {parte_2}")
    print(f"Parte 1 - Parte 2 = {eq_reta}")
    print(abc)


reta = [
     [874789.39726844697725028, 8795926.77887029759585857],
     [875903.47423053090460598, 8795927.27956279180943966]
]
reta = [
     [874789.39726844697725028, 8795926.77887029759585857],
     [875903.47423053090460598, 8795927.27956279180943966]
]
a, b = reta

# wkt_geom	fid
p1 = [875799.90287362365052104, 8795927.23458899557590485]
p2 = [875662.46652667073067278, 8796379.98182608000934124]
p3 = [875195.29522121185436845, 8795926.96561238914728165]
p4 = [874936.49430223135277629, 8795926.84711784496903419]
# p1 = [-41.56338122698868887, -10.87307113795266211]
# p2 = [-41.56468330372108255, -10.86899791140667482]
# p3 = [-41.56890332987345005, -10.87313534845132246] # Fora da linha
# p4 = [-41.57126706319329656, -10.87316283372248371]

equacao_reta(a, b, p1)
# equacao_reta(b.reverse(), a.reverse(), p2.reverse())
# equacao_reta(b.reverse(), a.reverse(), p3.reverse())
