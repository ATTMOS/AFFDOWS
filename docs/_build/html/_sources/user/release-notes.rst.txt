.. include:: ../affdo_docs_common.rst

Release Notes
^^^^^^^^^^^^^
The new features released with each AFFDO version are as follows.


AFFDO 25.11
***********

AFFDO 25.11 introduces major upgrades to the torsion fitting workflow, reporting system, fragmentation pipeline, and computational performance. The platform now delivers more accurate results, faster execution,
and a smoother user experience, while remaining fully automated and optimized for ligand-specific force field development in drug discovery (`https://www.attmosdiscovery.com/tools <https://www.attmosdiscovery.com/tools>`_).

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

* **Extended charge models** making RESP electrostatics and ABCG2 charge capabilities selectable directly from the workflow widgets.

* **Versatile workflow modes** adding a Topology-only option for quick GAFF2 topology generation with RESP charges, plus a Fragmentation-only mode that exposes FragMentor so users can isolate and parametrize just the ligand fragments they care about.

* **Performance improvements via project-level and fragment-level parallelization**, significantly reducing walltime for complex ligands (not available in the free-trial AFFDOWS).

* **Infrastructure upgrades** including smarter resource allocation, improved remote execution handling, and optimized queueing.

* **General bug fixes and stability improvements** across fitting routines, reporting, torsional scanning, and logging.


AFFDO 24.09
***********

AFFDO 24.09 centers around a fully web-based service. It has the following features:

**Major Features**

* **Automated Force Field Development**: Fully automates the generation of ligand-specific Generalized Amber Force Field (GAFF) torsion parameters, requiring no user intervention.

* **Web-based Interface**: The AFFDO platform is available as a web service, providing an intuitive and user-friendly experience.
  
* **Ligands Fragmentation Tool Integration**: Utilizes the specialized tool *FragMentor* to fragment large ligands, optimizing torsion parameters efficiently while preserving the chemical environment.

* **Cloud Integration**: Handles computationally expensive tasks through cloud instances, enabling GPU-accelerated and parallelized quantum chemistry calculations, reducing turnaround time.

* **JAX-based Parameter Optimization**: Leverages JAX for fast, gradient-based optimization with automatic differentiation, optimizing force field parameters with high precision and speed.
  
* **AMBER Compatibility**: AFFDO generates input files, compatible with AMBER-based free energy simulation workflows like ProFESSA, for an easy integration.   

* **Improved Reliability and Diagnostics**: Enhanced logging, clearer error reporting, and structured diagnostic messages provide more transparent feedback and easier troubleshooting within the web service.

* **Infrastructure for Parameter Caching**: Introduces backend support for database-driven reuse of previously computed torsion parameters, improving performance and enabling rapid iteration of AFFDO runs (not available in the free-trial AFFDOWS).


AFFDO 23.08 
***********

AFFDO 23.08 introduced the first fully notebook-driven version of the workflow, delivering a complete ligand-specific GAFF2 torsion reparameterization pipeline inside an interactive Jupyter environment. Key features include:

**Major Features**

* **End-to-end torsion reparameterization** using QUICK, geomeTRIC, and AMBER helpers, orchestrated through structured notebook cells with minimal manual configuration.

* **Interactive controls and guided panels** for uploading ligands, configuring paths, selecting compute hosts, and monitoring workflow progress directly within Jupyter.

* **Flexible compute integration**, enabling notebook sessions to offload QM tasks to local clusters, HPC systems, or cloud GPUs.

* **Built-in diagnostics and visualization**, including MM vs. QM torsion overlays, torsion fingerprint deviation metrics, and inline 3D conformer previews for rapid quality assessment.


*Last updated on* |UPDATE_DATE|.
