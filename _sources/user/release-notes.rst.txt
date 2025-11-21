.. include:: ../affdo_docs_common.rst

Release Notes
^^^^^^^^^^^^^
The new features released with each AFFDO version are as follows.


AFFDO 25.11
***********
AFFDO 25.11 introduces major upgrades to the torsion fitting workflow, reporting system, fragmentation pipeline, and computational performance. The platform now delivers more accurate results, faster execution,
and a smoother user experience, while remaining fully automated and optimized for ligand-specific force field development in drug discovery.

**Major Features**

* **Enhanced torsion fitting algorithms** resulting in improved accuracy, stability, and robustness across diverse chemical environments.

* **Improved initial guess methods** providing better optimization starting points and more reliable convergence.

* **Configurable torsion coupling and fragmentation controls** for greater flexibility in how molecules are grouped and parametrized, improving parameter transferability.

* **New interactive HTML reports** featuring clearer visualization, better statistics, and improved 3D viewing capabilities.

* **Streamlined Output Structure**: Reorganized project output with dedicated folders:

  - ``workflow_files/`` for main deliverables (update_params.in, run_configuration.txt)
  - ``stats_summary/`` for plots and statistics
  - Fragment-specific folders with mapped parameters

* **Improved job management and tracking** including fragment-level progress bars, better status reporting, jobs cancellation, and enhanced email notifications.

* **Enhanced torsion selection and scoring** using improved metrics for selecting representative torsional profiles.

* **Performance improvements via project-level and fragment-level parallelization**, significantly reducing walltime for complex ligands (no available for free-trial AFFDOWS).

* **Infrastructure upgrades** including smarter resource allocation, improved remote execution handling, and optimized queueing.

* **General bug fixes and stability improvements** across fitting routines, reporting, torsional scanning, and logging.


AFFDO 24.09
***********

AFFDO 24.09 centers around a fully web-based service (`https://www.attmosdiscovery.com/tools <https://www.attmosdiscovery.com/tools>`_). It has the following features:

**Major Features**

* **Automated Force Field Development**: Fully automates the generation of ligand-specific Generalized Amber Force Field (GAFF) torsion parameters, requiring no user intervention.

* **Web-based Interface**: The AFFDO platform is available as a web service, providing an intuitive and user-friendly experience.
  
* **Ligands Fragmentation Tool Integration**: Utilizes the specialized tool *FragMentor* to fragment large ligands, optimizing torsion parameters efficiently while preserving the chemical environment.

* **Cloud Integration**: Handles computationally expensive tasks through cloud instances, enabling GPU-accelerated and parallelized quantum chemistry calculations, reducing turnaround time.

* **JAX-based Parameter Optimization**: Leverages JAX for fast, gradient-based optimization with automatic differentiation, optimizing force field parameters with high precision and speed.
  
* **AMBER Compatibility**: AFFDO generates input files, compatible with AMBER-based free energy simulation workflows like ProFESSA, for an easy integration.   


*Last updated on* |UPDATE_DATE|.
