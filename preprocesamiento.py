import pandas as pd

FILE = "data\worlddata.csv"



# Limpiar el data set

def dropping_columns(file): # Eliminar las columnas innecesarias

    df_2 = pd.read_csv(file)

    # Poner las categorias en un diccionario
    cols = df_2.columns
    dic = {}
    ind = 0
    for i in cols:
        dic[ind] = i
        ind += 1

    print(f"Estas son las columnas: {dic}")

    to_drop = [] # Lista de las keys de las columnas que se van a eliminar

    # Event loop
    while True:
        inp = input("Ingresa las llaver numericas de a una para las columnas que queres eliminar: ")
        if inp == "n":
            break
        else:
            try:
                temp = inp # antes era int(inp) (por si no funciona ahora asi)
                to_drop.append(int(temp))
                print("Para salir escriba 'n'")
            except ValueError:
                print("Input incorrecto")
                break
        
    print("Estas seguro que queres eliminar estas columnas: ")
    for i in to_drop:
        print(dic[i])
    x = input("y/n: ")
    if x == "y":
        for i in to_drop:
            t = dic[i]
            df_2.drop(t, axis=1, inplace=True)
            df_2.to_csv(file, index=False)
    else:
        return