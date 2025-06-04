def calculadora():
    print("Bienvenido a la calculadora interactiva")
    print("Ingresa 'salir' para terminar el programa")
    print("Operaciones disponibles: +, -, *, /")
    
    while True:
        # Obtener la expresión del usuario
        entrada = input("Ingresa una operación (ej. 5 + 3) o 'salir': ")
        
        if entrada.lower() == 'salir':
            print("¡Gracias por usar la calculadora!")
            break
        
        try:
            # Dividir la entrada en partes
            partes = entrada.split()
            
            if len(partes) != 3:
                print("Formato incorrecto. Usa: numero operador numero")
                continue
                
            num1 = float(partes[0])
            operador = partes[1]
            num2 = float(partes[2])
            
            # Realizar la operación
            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 == 0:
                    print("Error: No se puede dividir entre cero")
                    continue
                resultado = num1 / num2
            else:
                print("Operador no válido. Usa: +, -, *, /")
                continue
                
            print(f"Resultado: {resultado}")
            
        except ValueError:
            print("Error: Ingresa números válidos")
        except Exception as e:
            print(f"Error inesperado: {e}")

# Iniciar la calculadora
calculadora()