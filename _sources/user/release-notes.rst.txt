.. include:: ../affdo_docs_common.rst

Release Notes
^^^^^^^^^^^^^
The new features released with each AFFDO version are as follows.

AFFDO 24.09
***********

The current release version |AFFDO_VERSION| centers around a fully web-based service (`https://dust.sdsc.edu <https://dust.sdsc.edu>`_). It has the following features:

**Features**

* **Automated Force Field Development**: Fully automates the generation of ligand-specific Generalized Amber Force Field (GAFF) torsion parameters, requiring no user intervention.

* **Web-based Interface**: The AFFDO platform is available as a web service, providing an intuitive and user-friendly experience.
  
* **Ligands Fragmentation Tool Integration**: Utilizes the specialized tool *FragMentor* to fragment large ligands, optimizing torsion parameters efficiently while preserving the chemical environment.

* **Cloud Integration**: Handles computationally expensive tasks through cloud instances, enabling GPU-accelerated and parallelized quantum chemistry calculations, reducing turnaround time.

* **JAX-based Parameter Optimization**: Leverages JAX for fast, gradient-based optimization with automatic differentiation, optimizing force field parameters with high precision and speed.
  
* **AMBER Compatibility**: AFFDO generates input files, compatible with AMBER-based free energy simulation workflows like ProFESSA, for an easy integration.   


*Last updated on* |UPDATE_DATE|.
