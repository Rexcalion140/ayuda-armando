def encontrar_palabra_mas_larga(palabras):
    palabra_longitud = []

    for p in palabras:
        palabra_longitud.append((len(p), p))

    palabra_longitud.sort()

    return palabra_longitud[-1][1]


palabras = ["javascript", "python", "c++", "php"]

print(encontrar_palabra_mas_larga(palabras))