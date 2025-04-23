Getting Started Guide
=====================

The user should visit the AFFDO web server at `https://dust.sdsc.edu <https://dust.sdsc.edu>`_, upload a ligand structure in **.pdb / .mol / .mol2** format, and provide the molecular charge and an email address. After submission, the job enters a queue and an email with a **Job ID** is sent to the user. The job’s status can be checked with this ID through the web interface. When the run finishes, a second email provides a download link to the project results. The project folder contains the optimized torsion parameters plus all input, output, and helper files needed to update AMBER topology files.

Output Structure
-----------------

The project directory contains several important files and subdirectories. Below is an explanation of the key components:

- **ParmEd input file (.in)**: 
  This file contains the newly optimized torsion parameters and is the primary output of the AFFDO workflow. Use this file with parmed tool of the AmberTools molecular dynamics package to update your topology files.

- **AFFDO log file (.log)**: 
  The log file captures the output of the entire AFFDO workflow run, including the details of how reference data was collected and torsion parameters were optimized. It can be used to verify that the workflow completed as expected.

- **update_topology.py**:  
  Helper script that uses ParmEd to apply updated torsion parameters to the standard GAFF2 topology, with an optional *dual-topology* mode for RBFE work.
  
- **Supporting files and folders**:
        - **Mol file (.mol)**: Standardized MOL-format file containing the ligand’s coordinates and atom labels as processed by AFFDO.
        - **Data JSON (.json)**: Contains metadata and settings used for the AFFDO. This file includes information such as the selected methods, parameters, and computational environment.
        - **Input file folder**: The original upload (PDB/MOL2/MOL) is preserved in this folder.
        - **Standard GAFF topology folder**: Contains the unmodified GAFF2 topology files for the original ligand (.prmtop, .rst7, .mol2, .frcmod) for user reference. 
        - **Results folder**: Contains intermediate files generated throughout the project. This includes conformer generation, centroid optimization, torsional scans, and parameter optimization steps. These files may be useful if you want to investigate the detailed steps taken by AFFDO.
        

- If the fragmentation algorithm was executed:

  - **Fragments image (.png)**: 
    A visual representation of the fragments generated during the run.

  - **Fragment results folder (e.g., project_f1, project_f2)**: 
    Contains output files for each fragment that was analyzed separately.

- **Topology‑Only Mode (optional)**
  If you invoke AFFDO with the “Topology‑Only” mode, AFFDO will stop as soon as it builds the standard GAFF2 topology. No reparameterization-related files will be included.

Using the ParmEd Input File
---------------------------

Once AFFDO has generated your ParmEd update file (e.g. *params_update.in*), you can inject those torsion parameters into your GAFF2 topology using our helper script: **update_topology.py**.  
This tool automates all the ParmEd calls. Under dual‑topology mode, it keeps only those torsion modifications that appear in both ligand states. This ensures consistent torsion updates across end‑states, ideal for alchemical free‑energy simulations. 

**Usage**

To run the script, use the following command:

.. code-block:: bash

   python update_topology.py -p my_system.parm7 -i output-params_update.in [--dual-topology]

**Required arguments**
   - ``-p`` / ``--topology`` Path to the original GAFF2 ``.parm7`` file.  
   - ``-i`` / ``--update-in`` AFFDO-generated ParmEd input (``*.in``).

**Optional**
  - ``--dual-topology`` Keep only torsions present in *both* residues 1 and 2 (recommended for RBFE dual-topology workflows).

**Example**

* Single topology (standard usage):

.. code-block:: none

    python update_topology.py -p my_system.parm7 -i params_update.in

* Dual topology (common torsions only):

.. code-block:: none

    python update_topology.py -p my_system.parm7 -i params_update.in --dual-topology


Running the script creates **new.prmtop** containing the optimized torsion parameters.  
Check *parmed_update.log* (or the console) for warnings before production MD.

**Note**: Ensure that Python is installed and accessible from your command line before running the script.


Tips for Safe Topology Updates
------------------------------

When you move from AFFDO’s torsion re‑parameterisation into your MD or RBFE workflows, keep these points in mind:

#. **Use identical ligand coordinates** – The exact same `.mol`, `.pdb`, or `.mol2` file provided to AFFDO must also be read by your MD engine. Any atom order or numbering mismatch will cause ParmEd to silently skip torsion updates, so double‑check file consistency.
#. **Inspect ParmEd logs for errors** – After running `update_topology.py` (or your own ParmEd command), always glance at `parmed_update.log` or the console output for warnings. This prevents inadvertently launching production runs with default GAFF torsions.
#. **(Optional) Dual topology for RBFE** – For two‑end‑state free‑energy calculations, we recommend updating only torsions common to both ligands. The `--dual-topology` flag in `update_topology.py` handles this automatically, though you may adopt a different ParmEd strategy if preferred.

These simple checks give you confidence that your AFFDO‑refitted torsions are present in the final topology.



Disclaimer
----------

Please be advised that AFFDO is part of an active development project. While we strive to provide accurate and reliable results, the underlying technology is continuously evolving, and there may be occasional updates or changes.




*Last updated on* |UPDATE_DATE|.


