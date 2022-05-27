def AutoPartes(ventas:list):
    registro = {
      "Producto consultado": ventas
    }
    return registro 





def consultaRegistro(ventas,idProducto):   
    validador = False
    consulta =""
    for j in ventas["Producto consultado"]:
         if idProducto in j:
             validador = True   
             print("Producto consultado :"+f"{j[0]}  Descripción  {j[1]}  #Parte  {j[2]}  Cantidad vendida  {j[3]}  Stock  {j[4]}  Comprador {j[5]}  Documento  {j[6]}  Fecha Venta  {j[7]}" )
    if not validador:
        print( "No hay registro de venta de ese producto")         
             
   
     
 
     
print(consultaRegistro(AutoPartes([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010))