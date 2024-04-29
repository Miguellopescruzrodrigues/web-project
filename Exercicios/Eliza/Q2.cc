#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooPlot.h"
#include "RooGaussian.h"
#include "RooCBShape.h" // Crystall Ball
#include "RooExponential.h" // Exponential
#include "RooFit.h"
#include "RooAddPdf.h"
#include "RooRandom.h"
#include "TCanvas.h"
#include "TPaveText.h"

using namespace RooFit;

int Q2() {


// variaveis-------------------------------------------------------------
    RooRealVar x("x", "x", -10, 10); 
    RooRealVar mean("mean", "Mean", 0, -10, 10);//CBS
    RooRealVar sigma("sigma", "Sigma", 1, 0.1, 5);//CBS
    RooRealVar alpha("alpha", "Alpha", 1, 0.1, 10);//CBS
    RooRealVar n("n", "n", 1, 0.1, 10);//CBS

    RooCBShape CBS("CBS", "Crystall Ball", x, mean, sigma, alpha, n);

    RooDataSet *data = CBS.generate(x, 1000); // gerando os eventos 


    RooFitResult* fit_result = CBS.fitTo(*data, Save());//junta CBS com os dados 


    TCanvas *c1 = new TCanvas("c1", "Crystall Ball", 800, 600);
    RooPlot *frame = x.frame();
    frame->SetTitle("Crystall Ball");
    data->plotOn(frame);
    CBS.plotOn(frame);
    frame->Draw();

    TPaveText *Leg = new TPaveText(0.6, 0.6, 0.9, 0.9, "NDC");//legenda
    Leg->AddText(Form("Mean: %.2f", mean.getVal()));
    Leg->AddText(Form("Sigma: %.2f", sigma.getVal()));
    Leg->AddText(Form("Alpha: %.2f", alpha.getVal()));
    Leg->AddText(Form("n: %.2f", n.getVal()));
    Leg->AddText(Form("Chi2/NDF: %.2f", frame->chiSquare()));
    Leg->Draw();

//Exponencial----------------------------------------------------------------------

    TCanvas *c2 = new TCanvas("c2", "Exponencial", 800, 600);


    RooRealVar lambda("lambda", "lambda", -0.5, -10., 0.);//exp
    RooExponential exp("exp", "Exponential ", x, lambda);//exp

    RooDataSet *exp_data = exp.generate(x, 1000);//junta exp com os dados

    RooFitResult* exp_fit_result = exp.fitTo(*exp_data, Save());

    c2->Draw();
    RooPlot *exp_frame = x.frame();
    exp_data->plotOn(exp_frame);
    exp.plotOn(exp_frame);
    exp_frame->SetTitle("Exponencial");
    exp_frame->Draw("same");

    TPaveText *exp_statsBox = new TPaveText(0.6, 0.6, 0.9, 0.9, "NDC");
    exp_statsBox->AddText(Form("Lambda: %.2f", lambda.getVal()));
    exp_statsBox->AddText(Form("Chi2/NDF: %.2f", exp_frame->chiSquare()));
    exp_statsBox->Draw();

    // Salvar o canvas para visualização
    c1->SaveAs("CrystallBall.png");
    c2->SaveAs("Exponencial.png");

    return 0;
}
