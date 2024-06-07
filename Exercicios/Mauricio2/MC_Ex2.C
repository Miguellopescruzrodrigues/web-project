#include <iostream>
#include <cmath>
#include "TRandom3.h"  

int MC_Ex2() {
    double a = 0;  // Limite de baixo
    double b = 1;  // Limite de cima
    int N = 10000;  // Número de eventos

    double ymax = 1.0;  // limite superior 
    

    TRandom3 random;

    int P_na_Curva = 0;  // Conta quantos pontos tem em baixo da curva

    for (int i = 0; i < N; i++) {

        double x = random.Uniform(a, b);
        double y = random.Uniform(0, ymax);

        //função x^2
        if (y <= x * x) {
            P_na_Curva++;
        }
    }

    // A área do retângulo
    double a_retangulo = (b - a)*ymax;

    // Calculo da integral
    double estimated_integral = (P_na_Curva / (double)N)*a_retangulo;

    std::cout << "A integral calculada de 0 a 1 para x^2 é: " 
              << estimated_integral << std::endl;

    return 0; 
}
