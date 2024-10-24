Getting Started Guide
=====================

AFFDO (Automated Force Field Developer and Optimizer) is designed to provide customized torsion parameters for small drug-like molecules, significantly enhancing the accuracy of binding free energy predictions. After completing a run with AFFDO, users receive a comprehensive package containing all the necessary input files, log files, and final outputs required for further computational analysis.

This tutorial outlines the structure of the output package and how to use the provided files to update your Generalized Amber Force Field (GAFF) topology for molecular dynamics simulations.

Output Structure
-----------------

The output directory contains several important files and subdirectories. Below is an explanation of the key components:

* **ParmEd input file (.in)**: 
  This file contains the newly optimized torsion parameters and is the primary output of the AFFDO workflow. Use this file with the AMBER molecular dynamics package to update your simulation topology files, ensuring that the improved torsion parameters are incorporated into subsequent simulations.

* **AFFDO log file (.log)**: 
  The log file captures the entire AFFDO workflow, including the details of how torsion parameters were optimized. It can be used to verify that the workflow completed as expected.

* **Supporting files and folders**:
        - **Mol files (.mol and .mol2)**: These files contain the original ligand coordinates and atom labels used during the AFFDO run.
        - **Data JSON (.json)**: Contains metadata and settings used during the AFFDO run. This file includes information such as the selected methods, parameters, and computational environment.
        - **Results folder**: Contains intermediate files generated throughout the AFFDO workflow. This includes conformer generation, centroid optimization, torsional scans, and parameter optimization steps. These files may be useful if you want to investigate the detailed steps taken by AFFDO.

If the fragmentation algorithm was executed:

* **Fragments image (.png)**: 
  A visual representation of the fragments analyzed and parametrized.

* **Fragment results folder (e.g., project_f1, project_f2)**: 
  Contains output files for each fragment that was analyzed separately.

Using the ParmEd Input File
---------------------------

Before integrating the `.in` file into your GAFF topology, you need to update the file by adding a residue ID to the atom labels. This step is critical for accurate Alchemical Free Energy Simulations, particularly when using dual topology methods like the Alchemical Enhanced Sampling (ACES) method.

**Adding a Residue ID to the ParmEd File**

A Python script named `add_resid_number.py` is provided to automate this step. This script modifies the `.in` file to include the specified residue ID in the atom labels, which will be inserted into the topology file.

**Usage:**

To run the script, use the following command:

.. code-block:: none

    python add_resid_number.py <input_file_name> <resid>

Where:

- `<input_file_name>`: The name of the ParmEd input file you want to modify.
- `<resid>`: The residue ID to add to the atom labels.

**Example**:

If your file is named `params_filename.in` and you want to add residue ID 1, run the following:

.. code-block:: none

    python add_resid_number.py params_filename.in 1

The script will create a new file named `output-params_filename.in` with the residue ID added to the atom labels.

To update the topology with the parameters fitted by AFFDO, use the `parmed` tool from Amber as follows:

.. code-block:: none
    
    parmed -p topology_file -i output-params_filename.in

This will generate a new topology file named 'new.prmtop' incorporating the optimized torsion parameters.

**Note**: Ensure that Python is installed and accessible from your command line before running the script.


Disclaimer
----------

Please be advised that AFFDO is part of an active development project. While we strive to provide accurate and reliable results, the underlying technology is continuously evolving, and there may be occasional updates or changes.




*Last updated on 10/24/2024.*
