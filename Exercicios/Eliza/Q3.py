from ROOT import TFile
from ROOT import TLorentzVector
from ROOT import TH1F
from ROOT import TF1
#import numpy as np
from ROOT import RooRealVar
from ROOT import RooDataHist
from ROOT import RooDataSet
from ROOT import RooExponential
from ROOT import RooGaussian
from ROOT import RooVoigtian
from ROOT import RooPolynomial
from ROOT import RooCBShape
from ROOT import RooArgList
from ROOT import RooArgSet
from ROOT import RooAddPdf
from ROOT import RooPlot
from ROOT import TLegend
from ROOT import RooFit
from ROOT import TLatex
from ROOT import RooChi2Var
from ROOT import TStyle
from ROOT import TCanvas, TFile, TPaveText, TH1F, TLegend, TTree
from ROOT import gStyle, TGraphErrors, TF1, TGraph, gPad, gRandom
from ROOT import kRed, kBlue
from ROOT import TFitResultPtr, TMatrixD
import ROOT 

# lendo o arquivo
file0 = TFile("DataSet_lowstat.root")
Data = file0.Get("data")


# cores na legenda
green = TH1F("h2","Ex",1,-10,10)
green.SetLineColor(ROOT.kGreen)
green.SetLineStyle(1)
green.SetLineWidth(2)

blue = TH1F("h2","Ex",1,-10,10)
blue.SetLineColor(ROOT.kBlue)
blue.SetLineStyle(1)
blue.SetLineWidth(2)

orange = TH1F("h2","Ex",1,-10,10)
orange.SetLineColor(ROOT.kOrange)
orange.SetLineStyle(1)
orange.SetLineWidth(2)

Dashed = TH1F("h2","Ex",1,-10,10)
Dashed.SetLineColor(ROOT.kDashed)
Dashed.SetLineStyle(1)
Dashed.SetLineWidth(2)


#Variaveis ===============================================================
mass = RooRealVar("mass", "mass [GeV]", 2, 6);
frame3 = mass.frame(RooFit.Title(r"$J/\psi$-$\psi(2S)$"))
Data.plotOn(frame3)

c3 = TCanvas("c3","c3",800,400)

mean_CBS = RooRealVar("mean_CBS", "mean_CBS",3.1, 3.1, 3.1)
sigma_CBS = RooRealVar("sigma_CBS", "sigma_CBS", 0.09, 0.0, 0.2)
alpha = RooRealVar("alpha_CBS", "alpha_CBS", 1.5, 0, 6)
n = RooRealVar("n_CBS", "nCBS",1.5, 0, 6)


mean_CBS2 = RooRealVar("mean_CBS2", "mean_CBS2",3.5, 3.5, 3.5)
sigma_CBS2 = RooRealVar("sigma_CBS2", "sigma_CBS2", 0.2, 0.0, 0.3)
alpha2 = RooRealVar("alpha_CBS2", "alpha_CBS2", 1.5, 0, 6)
n2 = RooRealVar("n_CBS2", "nCBS2",1.5, 0, 1)


pol1 = RooRealVar ( " pol1 " , " pol1 " , 0 , -10.0 , 10.0)

sinal_1=RooRealVar("sinal_1", "sinal_1", 0.5, 0, 1.);
sinal_2=RooRealVar("sinal_1", "sinal_1", 0.5, 0, 1.);

#Funções=================================================================
CBS = RooCBShape("CBS", "CBS", mass, mean_CBS, sigma_CBS, alpha,n)
CBS2 = RooCBShape("CBS2", "CBS2", mass, mean_CBS2, sigma_CBS2, alpha2,n2)
linear = RooPolynomial("linear", "linear", mass, pol1)



sum_pdf = RooAddPdf("sum_pdf", "Soma dos ajustes", RooArgList(CBS, CBS2, linear), RooArgList(sinal_1, sinal_2))


sum_pdf.fitTo(Data)


sum_pdf.plotOn(frame3, RooFit.LineColor(kBlue))
sum_pdf.plotOn(frame3, RooFit.Components("CBS"), RooFit.LineStyle(ROOT.kDashed), RooFit.LineColor(ROOT.kOrange))
sum_pdf.plotOn(frame3, RooFit.Components("CBS2"), RooFit.LineStyle(ROOT.kDashed), RooFit.LineColor(ROOT.kGreen))
sum_pdf.plotOn(frame3, RooFit.Components("linear"), RooFit.LineStyle(ROOT.kDashed), RooFit.LineColor(ROOT.kDashed))

#Legenda-----------
legend = TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(blue, "Ajuste", "l")
legend.AddEntry(orange, "CBS", "l")
legend.AddEntry(green, "CBS2", "l")
legend.AddEntry(Dashed, "linear", "l")
chi2_ndf = frame3.chiSquare()
legend.AddEntry(sum_pdf,"Chi2/NDF: {:.2f}".format(chi2_ndf), "")




frame3.Draw()
c3.Draw()
legend.Draw()

c3.Print("mass.png")
