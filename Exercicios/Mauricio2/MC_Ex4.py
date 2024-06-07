# Essa questão foi feita no google colab pois tive dificuldade de colocar o conda no meu computador
#
# Vou colocar aqui, separado por traços "-----------------" as células que botei no colab para fazer esse código rodar.event
# No colab coloquei o nome do código de "run_pythia.py", mas para enviar, preferi seguir o padrão dos meus exercícios


# ---------------------------------------------------------------
# !wget -q -c https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# !bash Miniconda3-latest-Linux-x86_64.sh -b -f -p /usr/local
# import os
# os.environ["PATH"] += ":/usr/local/bin"
# !conda --version
#----------------------------------------------------------------

#----------------------------------------------------------------
#!conda create -c conda-forge --name pythia_env python=3.8 pythia8 root -y
#----------------------------------------------------------------



#----------------------------------------------------------------
#code = """ #DESCOMENTAR PARA RODAR NO COLAB
import pythia8
import ROOT
from ROOT import TFile, TTree, vector, TH1F, TLorentzVector, TCanvas


f = TFile("output.root", "RECREATE")
tree = TTree("Pythia Events", "Eventos do Pythia")

# Vetores para os dados
n_pt = vector('float')()
n_eta = vector('float')()
n_phi = vector('float')()

tree.Branch("Particle_pt", n_pt)
tree.Branch("Particle_eta", n_eta)
tree.Branch("Particle_phi", n_phi)

# Inicialize o Pythia para simular produção de bóson Z com decaimento em múons
pythia = pythia8.Pythia()
pythia.readString("Beams:eCM = 13000.")  
pythia.readString("WeakBosonAndParton:qg2gmZq = on")  
pythia.readString("23:onMode = off")  # Desativar todos decaimentos do Z
pythia.readString("23:onIfAny = 13")  # Ativar decaimento do Z em múons
pythia.init()


muons = []

h_invariant_mass = TH1F("h_invariant_mass", "Massa Invariante muons", 100, 0, 120)
h_pt = TH1F("h_pt", "Particle_pt", 100, 0, 20)
h_eta = TH1F("h_eta", "Particle_eta", 100, -5, 5)
h_phi = TH1F("h_phi", "Particle_phi", 100, -3.14, 3.14)

# Loop para gerar eventos
for iEvent in range(10000):
    muons.clear()  # Limpar a lista de múons
    if not pythia.next():
        continue

    n_pt.clear()  # Limpar os vetores para partículas finais
    n_eta.clear()
    n_phi.clear()

    # Preencher os vetores 
    for particle in pythia.event:
        if particle.isFinal() and particle.isVisible():
            n_pt.push_back(particle.pT())
            n_eta.push_back(particle.eta())
            n_phi.push_back(particle.phi())
            h_pt.Fill(particle.pT())
            h_eta.Fill(particle.eta())
            h_phi.Fill(particle.phi())

            if abs(particle.id()) == 13:  # Identificar múons
                muons.append(TLorentzVector(particle.px(), particle.py(), particle.pz(), particle.e()))

            # Calcular a massa invariante para dois múons
                if len(muons) == 2:
                    mass = (muons[0] + muons[1]).M()  
                    h_invariant_mass.Fill(mass) 

    tree.Fill()  # Preencher a tree


f.Write()





# Canvas para Particle_pt
c1 = TCanvas("c1", "Canvas 1", 800, 600)
h_pt.Draw()
c1.SaveAs("particle_pt.png")  # Salvar como PNG


c2 = TCanvas("c2", "Canvas 2", 800, 600)
h_eta.Draw()
c2.SaveAs("particle_eta.png")  


c3 = TCanvas("c3", "Canvas 3", 800, 600)
h_phi.Draw()
c3.SaveAs("particle_phi.png")  


c4 = TCanvas("c4", "Canvas 4", 800, 600)
h_invariant_mass.Draw()
c4.SaveAs("invariant_mass.png")  
f.Close()

#""" #DESCOMENTAR PARA RODAR NO COLAB

#////////////////////////////////////////////////////////////
#Esse pedaço estáva na mesma célula que o código no colab, aqui está comentado para caso você queira rodar direto do seu coputador
#with open("run_pythia.py", "w") as file:
#    file.write(code)
#////////////////////////////////////////////////////////////
#----------------------------------------------------------------


#---------------------------------------------------------------
#!conda run -n pythia_env python run_pythia.py
#---------------------------------------------------------------