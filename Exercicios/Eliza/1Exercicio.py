#import ROOT
#h = ROOT.TH1F("gauss","Example histogram",100,-4,4)
#h.FillRandom("gaus")
#c = ROOT.TCanvas("myCanvasName","The Canvas Title",800,600)
#h.Draw()
#c.Draw()

import sys
sys.path.append("/content/root_build/")
sys.path.append("/content/root_build/bin/")
sys.path.append("/content/root_build/include/")
sys.path.append("/content/root_build/lib/")
import ctypes
ctypes.cdll.LoadLibrary('/content/root_build/lib//libCore.so')
ctypes.cdll.LoadLibrary('/content/root_build/lib//libThread.so')
ctypes.cdll.LoadLibrary('/content/root_build/lib//libTreePlayer.so')

#Block to import all the ROOT functions that we will be using throughout this template
from ROOT import TFile
from ROOT import TLorentzVector
from ROOT import TH1F
from ROOT import TF1
import numpy as np
from ROOT import RooRealVar
from ROOT import RooDataHist
from ROOT import RooDataSet
from ROOT import RooExponential
from ROOT import RooGaussian
from ROOT import RooVoigtian
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


# Criando uma TTree chamada "tree" e adicionando dois ramos (branches) a ela: "x" e "y".
# Em seguida, preenchemos a TTree com dados aleatórios usando gRandom.Gaus e gRandom.Uniform.
from array import array

tree = TTree("tree", "tree")
px = array('d', [0])
py = array('d', [0])
tree.Branch("x", px, "x/D")
tree.Branch("y", py, "y/D")
#
for i in range(100):
    px[0] = gRandom.Gaus(0, 3)
    py[0] = gRandom.Uniform() * 30 - 15
    tree.Fill()
#Depois disso, estamos utilizando o RooFit para importar os dados do TTree para um RooDataSet chamado "ds".
# Define 2nd observable y
x = RooRealVar("x", "x", -3, 3)
y = RooRealVar("y", "y", -10, 10)
ds = RooDataSet("ds", "ds", RooArgSet(x, y),RooFit.Import(tree))
ds.Print()

# P l o t   d a t a s e t   w i t h   m u l t i p l e   b i n n i n g   c h o i c e s
# ------------------------------------------------------------------------------------
# Print unbinned dataset with default frame binning (100 bins)
frame = y.frame(RooFit.Title("Unbinned data shown in default frame binning"))
ds.plotOn(frame)

# Print unbinned dataset with custom binning choice (20 bins)
frame2 = y.frame(RooFit.Title("Unbinned data shown with custom binning"))
ds.plotOn(frame2, RooFit.Binning(20))

# Draw all frames on a canvas
c = TCanvas("dataimport", "dataimport", 800, 800)
c.Divide(2)
c.cd(1)
gPad.SetLeftMargin(0.15)
frame.GetYaxis().SetTitleOffset(1.4)
frame.Draw()
c.cd(2)
gPad.SetLeftMargin(0.15)
frame2.GetYaxis().SetTitleOffset(1.4)
frame2.Draw()
c.Draw()
c.SaveAs("dataimport.png")

# Abrir o arquivo ROOT e obter o TNtuple
!wget https://github.com/elizamelo/Analise-Dados-FAE/raw/main/2024_01/RooFit/example_data.root

fin = TFile("example_data.root")
nt = fin.Get("nt")

# Definir a variável RooRealVar
mass = RooRealVar("mass", "mass [GeV]", 0.0, 2.0)

# Criar o RooDataSet com a variável definida e o TNtuple
# I m p o r t a r   o   d a d o   u n b i n n e d
# --------------------------------------------------------------
# construtor do RooDataSet
data = RooDataSet("data", "data", RooArgSet(mass), RooFit.Import(nt))

#O método data.Print("v") imprime informações sobre o RooDataSet,
#incluindo os nomes das variáveis e os valores dos eventos,
#para que você possa verificar se os dados foram importados corretamente.
data.Print("v")



# Make a plot of unbinned dataset (ROOT.RooFit # default)
frame3 = mass.frame(RooFit.Title("Imported Unbinned Mass"))
data.plotOn(frame3)

# Fit a Gaussian p.d.f to the data
mean = RooRealVar("mean", "mean", 1.0, 0.0, 2.0)

sigma = RooRealVar("sigma", "sigma",0.18,0.0,10.0)

gauss = RooGaussian("gauss", "gauss", mass, mean, sigma)

gauss.fitTo(data)
#gauss.fitTo(data,RooFit.PrintLevel(-1))
#gauss.fitTo(data, RooFit.PrintLevel(-1), RooFit.Minimizer("Minuit2", "Migrad"))
gauss.plotOn(frame3)
gauss.paramOn(frame3,data)
data.statOn(frame3)
c3 = TCanvas("exemplo03","exemplo03",800,400)
frame3.Draw()
c3.Draw()

gauss.Print("t")

