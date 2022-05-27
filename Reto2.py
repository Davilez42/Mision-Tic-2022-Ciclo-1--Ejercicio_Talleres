








def cliente(informacion:dict)->dict:
  
     info_nueva = {
            "nombre":informacion["nombre"],
            "edad":informacion["edad"],
            "atraccion":'',
            "apto":'',
            "primer_ingreso":informacion["primer_ingreso"],
            "total_boleta":''            
             }
    

     if informacion["edad"]>18:
         total_Valor =0
         if informacion["primer_ingreso"]:
                 total_Valor = 20000-(20000*0.05)
         else:
             total_Valor = 20000        
         info_nueva["atraccion"]="X-Treme"
         info_nueva["apto"]=True
         info_nueva["total_boleta"]=total_Valor
         

     else: 
          if informacion["edad"]<=18 and informacion["edad"]>=15:
                 total_Valor =0
                 if informacion["primer_ingreso"]:
                      total_Valor = 5000-(5000*0.07)
                 else:
                     total_Valor = 5000        
                 info_nueva["atraccion"]="Carroschocones"
                 info_nueva["apto"]=True
                 info_nueva["total_boleta"]=total_Valor
                 
              
          else:
                 if informacion["edad"]<15 and informacion["edad"]>=7:
                     total_Valor =0
                     if informacion["primer_ingreso"]:
                              total_Valor = 10000-(10000*0.05)
                     else:
                          total_Valor = 10000        
                     info_nueva["atraccion"]="Sillas voladoras"
                     info_nueva["apto"]=True
                     info_nueva["total_boleta"]=total_Valor
                   
                 else:
                     info_nueva["atraccion"]="N/A"
                     info_nueva["apto"]=False
                     info_nueva["total_boleta"]="N/A"
     return info_nueva                   


              
               
                





