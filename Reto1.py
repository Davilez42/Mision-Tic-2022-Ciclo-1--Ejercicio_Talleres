def CDT(nombre:str,capital:int,tiempo:int):
    porcentaje_interes = 0.03
    penalidad = 0.02
    if tiempo>2:
            valor_intereses = (capital*porcentaje_interes*tiempo)/12
            valor_total = capital+valor_intereses
            mensaje = f"Para el usuario {nombre} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"
            return mensaje
    else:
        if tiempo<=2:
            valor_a_perder = capital*penalidad
            valor_total = capital-valor_a_perder
            
            mensaje = f"Para el usuario {nombre} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"
            return mensaje
       