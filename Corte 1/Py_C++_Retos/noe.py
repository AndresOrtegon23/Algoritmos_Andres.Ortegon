def supermercado_noe():
    print("=== SUPERMERCADOS NOÉ - PROMOCIÓN DE ANIVERSARIO ===")
    
    # Solicitar el valor de la compra
    valor_compra = float(input("Ingrese el valor total de su compra: "))
    
    # Verificar si aplica para el descuento (mayor a 50.000)
    if valor_compra > 50000:
        print("\n¡Felicidades! Su compra es mayor a 50.000 y participa en el juego de las bolitas.")
        print("Elija el color de la bolita que sacó:")
        print("1. Roja (10% de descuento)")
        print("2. Azul (30% de descuento)")
        print("3. Amarilla (50% de descuento)")
        print("4. Blanca (¡Compra gratis / 100% de descuento!)")
        
        opcion = int(input("Ingrese el número correspondiente a su bolita (1-4): "))
        
        descuento = 0.0
        mensaje_premio = ""
        
        if opcion == 1:
            descuento = valor_compra * 0.10
            mensaje_premio = "Bolita Roja (10% de descuento)"
        elif opcion == 2:
            descuento = valor_compra * 0.30
            mensaje_premio = "Bolita Azul (30% de descuento)"
        elif opcion == 3:
            descuento = valor_compra * 0.50
            mensaje_premio = "Bolita Amarilla (50% de descuento)"
        elif opcion == 4:
            descuento = valor_compra
            mensaje_premio = "Bolita Blanca (¡Compra gratis!)"
        else:
            print("Opción no válida. No se aplicará descuento.")
            opcion = 0
            
        if opcion >= 1 and opcion <= 4:
            valor_final = valor_compra - descuento
            print(f"\n--- RESULTADO ---")
            print(f"Bolita obtenida: {mensaje_premio}")
            print(f"Valor inicial de la compra: ${valor_compra:,.2f}")
            print(f"Valor del descuento: ${descuento:,.2f}")
            print(f"Valor final a pagar: ${valor_final:,.2f}")
    else:
        print(f"\nLo sentimos, su compra fue de ${valor_compra:,.2f} y debe ser mayor a 50.000 para participar.")
        print(f"Valor final a pagar: ${valor_compra:,.2f}")

if __name__ == "__main__":
    supermercado_noe()