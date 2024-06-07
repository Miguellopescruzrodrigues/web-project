#include "TH1.h"
#include "TF1.h"
#include "TCanvas.h"

void Q3() {
    TH1F* histGaus = new TH1F("hist", "Gaussiana", 50, 0, 10);

    TF1* gaussiana = new TF1("gaussiana", "gaus", 0, 10);
    gaussiana->SetParameters(1, 5, 2); // amplitude, media e desvio padrão
    histGaus->FillRandom("gaussiana", 10000);
    gStyle->SetOptStat(111111111);

    TCanvas *c1 = new TCanvas("c1", "Gauss", 800, 600);
    histGaus->SetMarkerStyle(21); 
    histGaus->SetMarkerColor(1);

    histGaus->Draw();
}
