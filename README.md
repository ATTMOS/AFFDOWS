<p align="right">
<img src="https://github.com/ATTMOS/AFFDOWS/actions/workflows/update-docs.yml/badge.svg">
</p>
<p align="left">
<img width="320" height="75" src="./resources/logo-no-background.png">
</p>

An Automated Force Field Developer and Optimizer developed by ATTMOS Inc. 

Automated Force Field Developer and Optimizer (AFFDO) is a cutting-edge platform that automates the development and optimization of molecular mechanics force field parameters, tailored specifically to ligand-specific Generalized Amber Force Field (GAFF) torsions. 

The present version AFFDO-24.09 is available as a web service at [AFFDOWS](https://dust.sdsc.edu), free of charge.

Features
--------

- Automatic ligand fragmentation
- DFT and XTB reference data generation for torsion fitting
- Efficient reference data generation by massively parallelizing computations on CPU and GPU cloud instances
- Parameter fitting based on Google's JAX library and gradient based methods
- User friendly interface

For more details, see [Features](https://attmos.github.io/AFFDOWS/user/release-notes.html).


How It Works
------------

After completing an AFFDO run, users receive optimized torsion parameters packaged alongside input and log files, all necessary for updating GAFF topology files. 

To learn more about using AFFDO and handling the output files, please refer to our [Getting Started Guide](https://attmos.github.io/AFFDOWS/user/getting-started-guide.html).

For more information, check out our [Documentation](https://attmos.github.io/AFFDOWS/index.html).

Usage
-----

AFFDO is accessible via the web service at [AFFDOWS](https://dust.sdsc.edu). You can follow the intuitive steps to upload ligands, run torsional parameterization, and retrieve the output files. 

Citation
--------

If you use AFFDO in your research, please cite the latest version:

*Blanco-Gonzalez, A.; Betancourt, W.; Snyder, R.; Zhang, S.; Giese, T. J.; Goetz, A. W.; Merz, K. M., Jr.; York, D. M.; Aktulga, H. M.; Manathunga, M. Automated Force Field Developer and Optimizer Platform: Torsion Reparameterization. ChemRxiv 2024, doi:10.26434/chemrxiv-2024-lcnx1.*

License
-------

This software is subject to a non-commercial license. A copy of the license can be found [here](https://attmos.github.io/AFFDOWS/user/license.html). For commercial use, please contact ATTMOS Inc. for a separate agreement.

Bug Reports and Feedback
-------------------------

Your feedback helps improve AFFDO platform. Please submit any issues or feature requests via the [GitHub Issues section](https://github.com/ATTMOS/AFFDOWS/issues). We value your input!

About ATTMOS Inc.
-----------------

ATTMOS Inc. is dedicated to advancing computational chemistry solutions through innovation. AFFDO is just one of our many tools designed to empower researchers in the field of drug discovery, molecular dynamics, and beyond. Learn more about us [here](https://www.attmosdiscovery.com/).

