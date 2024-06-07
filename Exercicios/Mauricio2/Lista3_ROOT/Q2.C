#include <TGraph.h>
#include <TGraphErrors.h>
#include <TCanvas.h>
#include <TFile.h>
#include <iostream>
#include "RtypesCore.h"

void Q2() {

    TGraph *graph = new TGraph();

    fstream file1;
    file1.open("graphdata.txt", ios::in);

    while(1)
    {
        double x, y;
        file1 >> x >> y;
        graph->SetPoint(graph->GetN(), x, y);
        if(file1.eof()) break;
    }
    file1.close();

    TCanvas *c1 = new TCanvas("c1", "TGraph", 800, 600);
    graph->SetMarkerStyle(21); 
    graph->SetMarkerColor(1);
    c1->SetFillColor(42);
    c1->SetGrid();
    c1->GetFrame()->SetFillColor(21);
    c1->GetFrame()->SetBorderSize(12);
    graph->SetTitle("TGraph");
    graph->Draw("APL"); // A for markers, P for connecting lines, L for line color

//-----------------------------------------------------------------------------------------------------

    std::ifstream arquivo("graphdata_erro2.txt"); 
    if (!arquivo) { 
        std::cerr << "Erro ao abrir o arquivo." << std::endl;
        return 1; 
    }

    std::vector<float> coluna1;
    std::vector<float> coluna2;
    std::vector<float> coluna3;
    std::vector<float> coluna4;
    float valor1, valor2, valor3, valor4;

    while (arquivo >> valor1 >> valor2 >> valor3 >> valor4) {
        coluna1.push_back(valor1);
        coluna2.push_back(valor2);
        coluna3.push_back(valor3);
        coluna4.push_back(valor4);
    }
    arquivo.close();

    float x[coluna1.size()];
    float y[coluna2.size()];
    float ex[coluna3.size()];
    float ey[coluna4.size()];
    std::copy(coluna1.begin(), coluna1.end(), x);
    std::copy(coluna2.begin(), coluna2.end(), y);
    std::copy(coluna3.begin(), coluna3.end(), ex);
    std::copy(coluna4.begin(), coluna4.end(), ey);
    

    auto c2 = new TCanvas("c2","TGraphErrors",800,600);
    const Int_t n = 10;
    auto gr = new TGraphErrors(n,x,y,ex,ey);
    c2->SetFillColor(42);
    c2->SetGrid();
    c2->GetFrame()->SetFillColor(21);
    c2->GetFrame()->SetBorderSize(12);
    gr->SetTitle("TGraphErrors");
    gr->SetMarkerColor(1);
    gr->SetMarkerStyle(21);
    gr->Draw("ALP");



 }
