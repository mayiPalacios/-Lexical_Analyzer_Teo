#include <iostream>

using namespace std;
int numero;
int main() {
    
    int otraVariable;
    double unaVariableDecimal;

    cout << "Por favor, ingrese un número entero: ";
    cin >> numero;

 
    cout << "Por favor, ingrese otra variable entera: ";
    cin >> otraVariable;


    cout << "Por favor, ingrese una variable decimal: ";
    cin >> unaVariableDecimal;


    cout << "Usted ingresó el número entero: " << numero << endl;
    cout << "Usted ingresó otra variable entera: " << otraVariable << endl;
    cout << "Usted ingresó una variable decimal: " << unaVariableDecimal << endl;

    return 0;
}
