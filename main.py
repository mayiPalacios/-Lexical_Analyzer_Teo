from lexer import analyze, get_symbol_table

if __name__ == "__main__":
    code = '''
    // This is a comment
   #include <iostream>

// Variable global
int globalVar = 10;

// Constante global
const double PI = 3.141592653589793;

class SampleClass {
public:
    // Constructor
    SampleClass() : memberVar(0) {}  // Inicialización de miembro

    // Miembro de clase
    int memberVar;

    // Miembro estático de clase
    static float staticMember;

    void sampleMethod() {
        // Variable local en un método
        char localChar = 'A';

        // Variable estática local
        static int staticLocalVar = 100;

        std::cout << localChar << std::endl;
    }
};

// Definición de miembro estático de clase
float SampleClass::staticMember = 1.23f;

int main() {
    // Variable local
    int localVar = 20;

    // Array local
    int arr[5] = {1, 2, 3, 4, 5};

    SampleClass obj;
    obj.sampleMethod();

    return 0;
}


    '''

    analyze(code)
    symbols = get_symbol_table()
