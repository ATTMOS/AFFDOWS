.. include:: ../affdo_docs_common.rst

Accuracy and Performance
========================

The data reported in this section were obtained using |AFFDO_VERSION|. The code is continuously being improved. 
Please make sure to use the latest AFFDO version. 

We have validated the accuracy of AFFDO using a protein-ligand dateset reported by Wang et al.[1] In this dataset, authors 
report the experimental relative binding free energies (RBFE) values for a series of protein-ligand systems. For the validation
study, a subset of these systems was selected, and RBFE simulations were carried out using the Amber Drug Discovery Boost package [2].
The standard GAFF (GAFF 2.11) forcefield was used for ligands, ff14sb parameter set was used for proteins and TIP4P model was used for water.
The computed RBFE values using GAFF were compared against the experimental values; protein-ligand systems that displayed >1.0 kcal/mol error 
(the chemical accuracy threshold) were identified to test and validate AFFDO. Each ligand was used as input to the workflow and force fields with optimized 
dihedral parameters were obtained for each ligand. The time taken for the full reparameterization process varied from 3 to 48 hours depending 
on the system size, atom types, and hardware being used. In **Figure 1**, we present the torsional scan energy profiles for most significant torsions 
of TYK2 ejm42 (**A**) and jmc27 (**B**). The GAFF2 energy profile (Standard GAFF) of the former mostly differs from the reference profile by barrier height. 
In contrast, the latter not only differs in barrier height, but also in phase. Using the AFFDO platform, both the phase and barrier height can be fitted, 
resulting in much tighter fits to the reference profiles (Fitted GAFF). After reparameterization, fitted forcefield parameters were used to recompute RBFE 
values for protein-ligand pairs. As depicted in **Figure 2**, the reparameterized GAFF force field improves the computed RBFE for all systems. For certain systems 
(e.g. TYK2 jmc28-jmc30, jmc27-jmc30), this improvement is more prominent than the others.

.. image:: images/validation_figure.png
    :alt: This project was supported by NIH SBIR Seed fund. 


[1] Wang, L., Wu, Y., Deng, Y., et al. (2015). Accurate and reliable prediction of relative ligand binding
potency in prospective drug discovery by way of a modern free-energy calculation protocol and force
field. Journal of the American Chemical Society, 137(7), 2695-2703.

[2] Ganguly, A., Tsai, H. C., Fernández-Pendás, M., Lee, T. S., Giese, T. J., & York, D. M. (2022). AMBER
Drug Discovery Boost Tools: Automated Workflow for Production Free-Energy Simulation Setup and Analysis (ProFESSA). 
Journal of Chemical Information and Modeling, 62(23), 6069-6083.

*Last updated on 01/31/2024.*
