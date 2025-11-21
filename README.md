<p align="right">
<img src="https://github.com/ATTMOS/AFFDOWS/actions/workflows/update-docs.yml/badge.svg">
</p>
<p align="left">
<img width="320" height="75" src="./resources/logo-no-background.png">
</p>

An Automated Force Field Developer and Optimizer developed by ATTMOS Inc.

Automated Force Field Developer and Optimizer (AFFDO) is a cutting-edge platform that automates the development and optimization of molecular mechanics force field parameters, tailored specifically to ligand-specific Generalized Amber Force Field (GAFF) torsions.

The present version AFFDO-24.09 is available as a web service at [https://www.attmosdiscovery.com/tools](https://www.attmosdiscovery.com/tools), free of charge.

Features
--------

- **Enhanced torsion fitting algorithms**  
  Improved accuracy and robustness through upgraded optimization routines, better initialization strategies, and smarter convergence handling.

- **Automatic ligand fragmentation**  
  Intelligently splits molecules into chemically meaningful fragments, configurable by fragment size, to improve parameter quality and reduce computational cost.

- **Flexible reference data generation**  
  Supports DFT and XTB for torsional scan reference data

- **Advanced optimization modes**  
  Offers both coupled and uncoupled torsion fitting strategies, allowing adaptable parameterization across diverse chemical environments.

- **Efficient parallel computing**  
  Project-level and fragment-level parallelization dramatically reduce walltime. Smart resource selection automatically assigns optimal compute resources.

- **Comprehensive interactive HTML reports**  
  Dynamic reports with energy profile plots, 3D molecule viewer, optimization statistics, and full run metadata. Fully viewable offline.

- **Real-time job management**  
  Fragment-level progress bars, smarter job tracking, cancellation support, and detailed email notifications with key run parameters.

- **User-friendly web interface**  
  Clean submission workflow, automatic validation, integrated visualization tools, and responsive UI improvements.

- **Cloud-optimized infrastructure**  
  Deployed on scalable compute backends with improved queueing, retry handling, and optimized parallel resource management.

- **AMBER ecosystem compatibility**  
  Generates ParmEd update files and topology updates fully compatible with GAFF/GAFF2-based MD and RBFE workflows.

For more details, see [Features](https://attmos.github.io/AFFDOWS/user/release-notes.html).

How It Works
------------

AFFDO is accessible as a web service [here](https://www.attmosdiscovery.com/tools). Users upload a ligand structure in .mol/.mol2/.sdf/.pdb format and provide the molecular charge and email address. Upon submission, the job enters a queue system and an email with a job ID is sent to the user. Job status can be checked with this ID through the web interface.

When the job completes, users receive an email with a download link containing:
- **ParmEd input file** (.in) with optimized multi-primitive torsion parameters
- **Interactive HTML report** (fitting_report.html) with energy profiles and 3D visualization
- **Summary statistics** and plots for each optimized torsion
- **Topology files** and configuration details
- **Fragment-specific results** (when fragmentation is used)

The optimized parameters can be easily applied to GAFF topology files using the provided `update_topology.py` helper script.

To learn more about using AFFDO and handling the output files, please refer to our [Getting Started Guide](https://attmos.github.io/AFFDOWS/user/getting-started-guide.html).

Bug Reports and Feedback
-------------------------

Your feedback helps improve the AFFDO platform. Please submit any issues or feature requests via the [GitHub Issues section](https://github.com/ATTMOS/AFFDOWS/issues). We value your input!

Citation
--------

If you use AFFDO in your research, please cite the latest version:

*Blanco-Gonzalez, A.; Betancourt, W.; Snyder, R.; Zhang, S.; Giese, T. J.; Piskulich Z. A.; Goetz, A. W.; Merz, K. M., Jr.; York, D. M.; Aktulga, H. M.; Manathunga, M. Automated Force Field Developer and Optimizer Platform: Torsion Reparameterization. ChemRxiv 2024, doi:10.26434/chemrxiv-2024-lcnx1.*

License
-------

AFFDO web service is available for non-commercial purposes, free of charge. For commercial use, please contact ATTMOS at [info@attmosdiscovery.com](info@attmosdiscovery.com).
