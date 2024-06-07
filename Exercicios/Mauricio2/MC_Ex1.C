#include <iostream>
#include <cmath>
#include "TRandom3.h"  
#include "TMath.h"

int MC_Ex1() {
    double d = 1.0;  // Distância entre linhas paralelas
    double L = 0.5;  // comprimento da agulha
    int joga10 = 0;  int joga50 = 0; int joga100 = 0; int joga1000 = 0;// Contador de cruzamentoss
    int N = 10;
    double Estimativa_pi;


    for (int i = 0; i < N; ++i) {
        //ângulo entre 0 e pi
        double theta = gRandom->Uniform(0, TMath::Pi());

        // posição no centro da agulha
        double g = gRandom->Uniform(0, d / 2);

        if (L / 2 * sin(theta) > g) {
            joga10++;
        }
    }

// Equação para pi
     Estimativa_pi = (2.0 * L *N) / (d * joga10);


    //resultados
    std::cout << "N = " << N << ", Cruzamentos = " << joga10 
              << ", Estimativa de π = " << Estimativa_pi << std::endl;

//=================================================================================

    for (int i = 0; i < 50; ++i) {
        //ângulo entre 0 e pi
        double theta = gRandom->Uniform(0, TMath::Pi());

        // posição no centro da agulha
        double g = gRandom->Uniform(0, d / 2);

        if (L / 2 * sin(theta) > g) {
            joga50++;
        }
    }

// Equação para π
     Estimativa_pi = (2.0 * L *50) / (d * joga50);


    //resultados
    std::cout << "N = " << 50 << ", Cruzamentos = " << joga50 
              << ", Estimativa de π = " << Estimativa_pi << std::endl;

//=================================================================================


    for (int i = 0; i < N*10; ++i) {
        //ângulo entre 0 e pi
        double theta = gRandom->Uniform(0, TMath::Pi());

        // posição no centro da agulha
        double g = gRandom->Uniform(0, d / 2);

        if (L / 2 * sin(theta) > g) {
            joga100++;
        }
    }


// Equação para π
     Estimativa_pi = (2.0 * L *N*10) / (d * joga100);

    // resultados
    std::cout << "N = " << N*10 << ", Cruzamentos = " << joga100 
              << ", Estimativa de π = " << Estimativa_pi << std::endl;

//=================================================================================

    for (int i = 0; i < N*100; ++i) {
        //ângulo entre 0 e pi
        double theta = gRandom->Uniform(0, TMath::Pi());

        // posição no centro da agulha
        double g = gRandom->Uniform(0, d / 2);

        if (L / 2 * sin(theta) > g) {
            joga1000++;
        }
    }

        // Equação para π 
     Estimativa_pi = (2.0 * L *N*100) / (d * joga1000);

    //resultados
    std::cout << "N = " << N*100 << ", Cruzamentos = " << joga1000 
              << ", Estimativa de π = " << Estimativa_pi << std::endl;


    return 0;  
}
