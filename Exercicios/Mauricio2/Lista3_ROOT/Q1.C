#include <iostream>
#include <cmath>
#include "TCanvas.h"
#include "TF1.h"
#include "TMath.h"
#include "TGraph.h"

using namespace std;

Double_t Fseno(Double_t *x, Double_t *par) {
    if (x[0] == 0) return 0; 
    return par[0] * sin(par[1] * x[0]) / x[0];
}

void Q1() {
    TCanvas *canvas = new TCanvas("canvas", "Function Plot", 800, 600);

    Double_t randomN1 = gRandom->Uniform(0,10);
    Double_t randomN2 = gRandom->Uniform(0,10);

    TF1 *func = new TF1("func", Fseno, 0., 10., 3);
    func->SetParameters(randomN1, randomN2); 
    func->SetLineColor(kBlue);

    TGraph *graph = new TGraph(func);
    graph->SetTitle("p0*sin(p1*x)/x");
    graph->GetXaxis()->SetTitle("Eixo X");
    graph->GetYaxis()->SetTitle("Eixo Y");

    canvas->cd();
    graph->Draw("AL");

    func->SetParameters(1, 2);

    Double_t xValue = 1.0;
    Double_t functionValue = func->Eval(xValue);
    Double_t derivativeValue = func->Derivative(xValue);
    Double_t integralValue = func->Integral(0, 3);

    cout << "Função com o valor de x=1: " << functionValue << endl;
    cout << "Derivada com x=1: " << derivativeValue << endl;
    cout << "Integral entre 0 e 3: " << integralValue << endl;

    return 0;
}
