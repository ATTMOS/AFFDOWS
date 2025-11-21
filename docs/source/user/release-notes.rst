.. include:: ../affdo_docs_common.rst

Release Notes
^^^^^^^^^^^^^
The new features released with each AFFDO version are as follows.


AFFDO 25.11
***********

This release introduces significant improvements to parameter optimization algorithms, enhanced reporting capabilities, and better user experience features:

**Major Features**

* **Multi-Primitive Fourier Series Parameterization**: Torsion parameters now use multiple Fourier terms (n=1, 2, 3) instead of single-term representations, providing significantly improved accuracy in fitting quantum mechanical energy profiles.

* **Torsion Coupling Modes**: Added configurable torsion coupling strategies (atom-type, uncoupled) to control how similar torsions are grouped during optimization, improving parameter transferability.

* **Interactive HTML Reports**: New comprehensive HTML reports (fitting_report.html) featuring:

  - Interactive Plotly energy profile charts for all optimized torsions
  - 3D molecule viewer with torsion highlighting
  - Detailed optimization statistics and RMSE improvements
  - Downloadable results and topology files

* **ML Potential Support**: Added support for machine learning potentials (MACE, QDPI2) as reference data sources alongside DFT and XTB.

* **Enhanced Fragmentation Visualization**: Improved fragment visualization showing which torsions belong to each fragment with clearer color coding and atom numbering.

**Workflow Improvements & Usability**

* **Streamlined Output Structure**: Reorganized project output with dedicated folders:

  - ``workflow_files/`` for main deliverables (update_params.in, run_configuration.txt)
  - ``stats_summary/`` for plots and statistics
  - Fragment-specific folders with mapped parameters

* **Improved Progress Tracking**: Web interface now shows individual progress bars for each fragment during multi-fragment optimization.

* **Job Cancellation**: Added ability to cancel running jobs through the web interface with proper cleanup and status tracking.

* **Better Error Handling**: Enhanced error messages and validation throughout the workflow with clearer user feedback.

* **Multi-Primitive Update Script**: Updated ``update_topology.py`` helper script to fully support multi-primitive torsion format with automatic handling of multiple periodicity terms.

* **Email Notifications**: Enhanced email notifications with torsion coupling mode and fragment size information for better job tracking.


AFFDO 24.09
***********

The current release version |AFFDO_VERSION| centers around a fully web-based service (`https://www.attmosdiscovery.com/tools <https://www.attmosdiscovery.com/tools>`_). It has the following features:

**Features**

* **Automated Force Field Development**: Fully automates the generation of ligand-specific Generalized Amber Force Field (GAFF) torsion parameters, requiring no user intervention.

* **Web-based Interface**: The AFFDO platform is available as a web service, providing an intuitive and user-friendly experience.
  
* **Ligands Fragmentation Tool Integration**: Utilizes the specialized tool *FragMentor* to fragment large ligands, optimizing torsion parameters efficiently while preserving the chemical environment.

* **Cloud Integration**: Handles computationally expensive tasks through cloud instances, enabling GPU-accelerated and parallelized quantum chemistry calculations, reducing turnaround time.

* **JAX-based Parameter Optimization**: Leverages JAX for fast, gradient-based optimization with automatic differentiation, optimizing force field parameters with high precision and speed.
  
* **AMBER Compatibility**: AFFDO generates input files, compatible with AMBER-based free energy simulation workflows like ProFESSA, for an easy integration.   


*Last updated on* |UPDATE_DATE|.
