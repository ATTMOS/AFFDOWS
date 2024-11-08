Getting Started Guide
=====================

The user should visit AFFDO web server at `https://dust.sdsc.edu <https://dust.sdsc.edu>`_, upload a ligand structure in .pdb/.mol/.mol2 format, and provide the molecular charge and email address. Upon the submission of the project, the job enters a queue system and an email with a job ID is sent to the user. The status of the job can be checked with this job ID through the web interface. When the job is finished, the user receives a second email that contains a link to download the results of the AFFDO project. The project folder contains optimized torsion parameters along with the input and output files, and other files required to update the AMBER topology files.

Output Structure
-----------------

The project directory contains several important files and subdirectories. Below is an explanation of the key components:

* **ParmEd input file (.in)**: 
  This file contains the newly optimized torsion parameters and is the primary output of the AFFDO workflow. Use this file with parmed tool of the AmberTools molecular dynamics package to update your topology files.

* **AFFDO log file (.log)**: 
  The log file captures the output of the entire AFFDO workflow run, including the details of how reference data was collected and torsion parameters were optimized. It can be used to verify that the workflow completed as expected.

* **Supporting files and folders**:
        - **Mol files (.mol and .mol2)**: These files contain the original ligand coordinates that were used to initiate the AFFDO run.
        - **Data JSON (.json)**: Contains metadata and settings used for the AFFDO. This file includes information such as the selected methods, parameters, and computational environment.
        - **Results folder**: Contains intermediate files generated throughout the project. This includes conformer generation, centroid optimization, torsional scans, and parameter optimization steps. These files may be useful if you want to investigate the detailed steps taken by AFFDO.

If the fragmentation algorithm was executed:

* **Fragments image (.png)**: 
  A visual representation of the fragments generated during the run.

* **Fragment results folder (e.g., project_f1, project_f2)**: 
  Contains output files for each fragment that was analyzed separately.

Using the ParmEd Input File
---------------------------

Before injecting the parameters using `.in` file into your GAFF topology, you need to update the file by adding a residue ID to the atom labels. 

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




*Last updated on 11/08/2024.*
