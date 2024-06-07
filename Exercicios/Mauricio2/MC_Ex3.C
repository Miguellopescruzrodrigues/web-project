#include "TMath.h"
#include <iostream>
#include "TRandom.h"
#include "TH1.h"
#include <math.h>

using namespace std;
double m = 0.511;
double k;
int nexp = 10000;
int cont = 0;
double x;




void MC_Ex3() {

TFile f("histo2.root","UPDATE");
TH1D * h1 = new TH1D("5KeV", "5KeV", 100,0, 3.141);

for(double j = 0; j< nexp; j++) {
//
	for(double i =0; i <1200; i++) {
		double zz = 1.076*(gRandom->Rndm());

		x =3.14*(gRandom->Rndm());

	if (zz <= ((pow((1/(1+0.01*(1-cos(x)))),2))*(((1/(1+0.01*(1-cos(x))))+(1+0.01*(1-cos(x))))-sin(x)*sin(x)))*sin(x)){i=1200;}
	}
	h1->Fill(x);
	}

h1->Write();
	cout << cont << endl;
	cont = cont + 1;

}