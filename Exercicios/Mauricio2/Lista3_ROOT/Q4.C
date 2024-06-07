#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TCut.h"
#include "TCanvas.h"
#include "TMath.h"

void Q4() {
    TFile *file = TFile::Open("tree.root");
    TTree *tree = (TTree*)file->Get("tree1");
    TH1F *hist = new TH1F("hist", "Momento total", 100, 120, 160);

    //Definindo variaveis e acessando as branches.
    Int_t           event;
    Float_t         ebeam;
    Float_t         px;
    Float_t         py;
    Float_t         pz;
    Float_t         zv;
    Float_t         chi2;
    Float_t         Momento;

    tree->Branch("event",&event,"event");
    tree->Branch("ebeam",&ebeam,"ebeam/F");
    tree->Branch("px",&px,"px/F");
    tree->Branch("py",&py,"py/F");
    tree->Branch("pz",&pz,"pz/F");
    tree->Branch("zv",&zv,"zv/F");
    tree->Branch("chi2",&chi2,"chi2/F");

    tree->SetBranchAddress("px",&px);
    tree->SetBranchAddress("py",&py);
    tree->SetBranchAddress("pz",&pz);
    tree->SetBranchAddress("zv",&zv);
    tree->SetBranchAddress("ebeam",&ebeam);
    tree->SetBranchAddress("event",&event);
    tree->SetBranchAddress("chi2",&chi2);


float Mean_ebeam = 0;
for (int i = 0; i < tree->GetEntries(); i++) {
    tree->GetEntry(i);

      Mean_ebeam = Mean_ebeam + ebeam;
      
   }
    Mean_ebeam = Mean_ebeam/tree->GetEntries();


    //Tentativa de usar o Tcut ---------------------------------------------------------------------
    TCut *cut = new TCut("TMath::Abs(ebeam - Mean_ebeam) > 0.2");


for (int i = 0; i < tree->GetEntries(); i++) {
    tree->GetEntry(i);
    if ((ebeam - Mean_ebeam) > 0.2){
      Momento = TMath::Sqrt(px*px + py*py + pz*pz);
      hist->Fill(Momento);
    }
  }
 
  hist->Draw();

}
