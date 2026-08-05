#include <iostream>
using namespace std;

int main()
{
    float gradosCentigrados, farenheith;
    
    cout << "Escribe los grados Farenheith que necesitas para convertirlos a grados: " << endl;
    cin >> farenheith;
    
    gradosCentigrados = (farenheith - 32) / 1.8;
    
    cout << "Convertido en grados centigrados es de: " << gradosCentigrados << endl;
    

    return 0;
}