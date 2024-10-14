# Team-PLS-Genome-Assembly

University of Rennes 1

git@github.com:hakimGMO/Team-PLS-Genome-Assembly.git


# livre Bioinformatics Algorithms : How do we assemble genomes?
https://www.bioinformaticsalgorithms.org/bioinformatics-chapter-3




# Consignes

Les projets doivent être réalisés par groupes de 3 personnes de la même promo (BEE, CAH ou BMC). Le projet est à rendre avant le lundi 4 novembre 23h59 (autrement dit, le 5 novembre c'est trop tard). Vous avez donc un mois pour le réaliser.

Les sujets sont des chapitres (sélectionnés par nos soins) tirés des livres :

Modelling for Field Biologists and Other Interesting People, Hanna Kokko (BEE, CAH)
Modeling Evolution, an introduction to numerical methods,Derek A. Roff (BEE, CAH)
Bioinformatics Algorithms, Phillip Compeau & Pavel Pevzner (BMC)


Vous devez choisir un seul chapitre. Vous trouverez les pdf des chapitres dans l'activité ci-dessous sauf pour Bioinformatics Algorithms qui est accessible en ligne.

Chaque chapitre sélectionné vous propose de découvrir des modélisations variées que vous devez écrire en langage python. Dans certains ouvrages, du code R ou MatLab est fourni, à vous de comprendre et de traduire ce code en python (ou de le refaire à votre façon). Le but du projet est d'aller le plus loin possible dans le chapitre que vous aurez choisi mais nous avons bien conscience des différences de niveau entre les groupes, ce sera pris en compte.

L'évaluation se fera sur le fichier python rendu dans l'activité "Projet Python" et sur une présentation orale qui aura lieu le jeudi 7 novembre. 

La présentation durera 8 minutes maximum et vous présenterez votre travail ensemble. Vous devez toutes et tous savoir répondre aux questions. En particulier, nous poserons des questions sur votre code python et nous choisirons à qui nous posons la question. Organisez-vous pour que tous les membres du groupe comprennent bien le code python.

# Lesson 3.3 : String Reconstruction as a Walk in the Overlap Graph

From a string to a graph
Repeats in a genome necessitate some way of looking ahead to see the correct assembly in advance. Returning to our above example, you may have already found that TAATGCCATGGGATGTT is a solution to the String Reconstruction Problem for the collection of fifteen 3-mers in the last section, as illustrated below. Note that we use a different color for each interval of the string between occurrences of ATG.

TAA              
AAT            
ATG          
TGC        
GCC      
CCA    
CAT  
  ATG  
    TGG  
      GGG  
        GGA  
          GAT  
            ATG  
              TGT  
              GTT
TAATGCCATGGGATGTT

STOP and Think: Is this the only solution to the String Reconstruction Problem for this collection of 3-mers?

In the figure below, consecutive 3-mers in TAATGCCATGGGATGTT are linked together to form this string's genome path.



Figure: The fifteen color-coded 3-mers making up TAATGCCATGGGATGTT are joined into the genome path according to their order in the genome.

String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.

Input: A sequence path of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni (for 1 ≤ i ≤ n).
Reconstructing the genome from its genome path is easy: as we proceed from left to right, the 3-mers “spell’ out TAATGCCATGGGATGTT, adding one new symbol to the genome at each new 3-mer.  This yields a function PathToGenome(﻿path).

Unfortunately, constructing the genome path requires us to know the genome in advance.

Code Challenge: Solve the String Spelled by a Genome Path Problem. (Solve on Cogniterra or Rosalind.)
