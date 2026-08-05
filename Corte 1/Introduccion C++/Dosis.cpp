#include <iostream>
using namespace std;

int main()
{
    int mesesBebe;
    float pesoBebe, dosisVacuna;
    
    cout << "Ingrese los meses del bebe: " << endl;
    cin >> mesesBebe;
    cout << "Ingrese el peso del bebe: " << endl;
    cin >> pesoBebe;
    
    dosisVacuna = ((pesoBebe + 10)/(mesesBebe * 8))*8;
    
    cout << "La dosis que necesita el bebe es de: " << dosisVacuna << endl;
}