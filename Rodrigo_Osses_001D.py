productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}
def búsqueda_de_stock_HP():
    print("Especificaciones: ") , print(productos.get("8475HD")) , print("Precio y Unidades disponibles: "), print(stock.get("8475HD"))
    print("Especificaciones: ") , print(productos.get("fgdxFHD")) , print("Precio y Unidades disponibles: "), print(stock.get("fgdxFHD"))
def búsqueda_de_stock_Lenovo():
    print("Especificaciones: ") , print(productos.get("2175HD")) , print("Precio y Unidades disponibles: "), print(stock.get("2175HD"))
    print("Especificaciones: ") , print(productos.get("123FHD")) , print("Precio y Unidades disponibles: "), print(stock.get("123FHD"))
    print("Especificaciones: ") , print(productos.get("342FHD")) , print("Precio y Unidades disponibles: "), print(stock.get("342FHD"))
def búsqueda_de_stock_Asus():
    print("Especificaciones: ") , print(productos.get("JjfFHD")) , print("Precio y Unidades disponibles: "), print(stock.get("JjfFHD"))
    print("Especificaciones: ") , print(productos.get("JjfFHD")) , print("Precio y Unidades disponibles: "), print(stock.get("JjfFHD"))
def búsqueda_de_stock_Dell():
    print("Especificaciones: ") , print(productos.get("UWU131HD")) , print("Precio y Unidades disponibles: "), print(stock.get("UWU131HD"))


    


while True:
    print("Menú Principal")
    print("[1] Stock Marca")
    print("[2] Búsqueda por precio")
    print("[3] Actualizar precio]")
    Controlmenu=int(input("Seleccione una opción numerica (1, 2, 3 o 4)"))
    if (Controlmenu)==1:
        Busqueda_De_Marca_utilizable=input("Ingrese el nombre de la marca que desea buscar (Hp, Lenovo, Asus, Dell)")
        ##El código no funcionaba de otra forma que no fuera ingresando una marca y esa variable convertirla en otra variable para convertirla en minúsculas.
        if Busqueda_De_Marca_utilizable=="hp":
            búsqueda_de_stock_HP()
        elif Busqueda_De_Marca_utilizable=="lenovo":
            búsqueda_de_stock_Lenovo()
        elif Busqueda_De_Marca_utilizable=="asus":
            búsqueda_de_stock_Asus()
        elif Busqueda_De_Marca_utilizable=="dell":
            búsqueda_de_stock_Dell()



