#include <iostream>
#include <string>

using namespace std;

int main() {
    int num_productos;
    cout << "¿Cuántos productos va a comprar? ";
    cin >> num_productos;
    
    double total_antes_descuento = 0.0;
    
    for (int i = 1; i <= num_productos; i++) {
        string nombre;
        double precio;
        int cantidad;
        
        cout << "\nProducto #" << i << ":" << endl;
        cout << "Nombre del producto: ";
        cin >> nombre; 
        cout << "Precio unitario: ";
        cin >> precio;
        cout << "Cantidad comprada: ";
        cin >> cantidad;
        
        double subtotal = precio * cantidad;
        total_antes_descuento += subtotal;
        cout << "Subtotal del producto: $" << subtotal << endl;
    }
    
    double descuento = 0.0;
    if (total_antes_descuento > 300000) {
        descuento = total_antes_descuento * 0.10;
    } else if (total_antes_descuento >= 150000) {
        descuento = total_antes_descuento * 0.05;
    }
    
    double total_a_pagar = total_antes_descuento - descuento;
    
    cout << "\n=== RESUMEN FINAL ===" << endl;
    cout << "Total antes del descuento: $" << total_antes_descuento << endl;
    cout << "Descuento aplicado: $" << descuento << endl;
    cout << "Total a pagar: $" << total_a_pagar << endl;
    
    return 0;
}