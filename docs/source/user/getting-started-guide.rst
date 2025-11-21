.. include:: ../affdo_docs_common.rst

Getting Started Guide
=====================

The user should visit the AFFDO web server at `https://www.attmosdiscovery.com/tools <https://www.attmosdiscovery.com/tools>`_, upload a ligand structure in **.mol/ .mol2/ .sdf/ .pdb** format, and provide the molecular charge and an email address. After submission, the job enters a queue and an email with a **Job ID** is sent to the user. The job's status can be checked with this ID through the web interface. When the run finishes, a second email provides a download link to the project results.

AFFDO is designed to provide customized torsion parameters for small drug-like molecules, significantly enhancing the accuracy of binding free energy predictions. The key deliverable is the final ParmEd input file (.in), containing the newly optimized torsion parameters using a multi-primitive Fourier series approach, ready to update the Generalized Amber Force Field (GAFF) topology file employed during your molecular dynamics simulations.

Project Folder Structure
------------------------

After AFFDO completes, you will receive the following files and folders:

.. code-block:: none

   project_root/
   │
   ├── <project>.log
   ├── <project>.mol
   ├── data.json
   ├── fitting_report.html
   ├── topology.zip
   │
   ├── workflow_files/
   │   ├── update_params_<project>.in
   │   ├── run_configuration.txt
   │   └── <project>.log
   │
   ├── stats_summary/
   │   ├── <project>_fragments.png
   │   ├── confs_999-999_dh_X-X-X-X_<fragment>.png
   │   ├── fitting_summary.txt
   │   └── fitting_report.csv
   │
   ├── input_file/
   │   └── <input_filename>
   │
   ├── resources/
   │   ├── Attmos_logo.png
   │   ├── logo.txt
   │   └── js/
   │       ├── 3Dmol.js
   │       ├── plotly.js
   │       └── html2pdf.js
   │
   ├── <project>_f1.zip
   │   ├── <project>_f1.log
   │   ├── <project>_f1.mol
   │   ├── data.json
   │   ├── update_params_<project>_f1.in
   │   ├── update_params_mapped_<project>_f1.in
   │   └── results/
   │       ├── conformers/
   │       ├── conformer_minimization/
   │       ├── clusters/
   │       ├── centroid_optimization_mm/
   │       ├── torsional_scan/
   │       ├── constrained_optimization/
   │       ├── paramopt_works/
   │       ├── paramtest_works/
   │       └── torsion_works/
   │
   ├── <project>_f2.zip
   │   └── [same structure as Fragment 1]
   │
   └── <project>_f3.zip
       └── [same structure as Fragment 1]


Main Output Files
~~~~~~~~~~~~~~~~~

- **fitting_report.html**: Interactive HTML report with energy profile plots, optimization statistics, and 3D molecule viewer showing all optimized torsions and their improvements.
- **<project>.log**: The log file captures the entire AFFDO workflow process, providing insights into how the torsion parameters were optimized and can be used to verify that the workflow completed as expected.
- **<project>.mol**: The standardized MOL-format file containing the ligand's coordinates and atom labels as processed by AFFDO.
- **data.json**: Contains metadata and settings used in the AFFDO run (reference level, force field, parametrization mode, torsion coupling mode, fragment size, etc.).

workflow_files/ folder
~~~~~~~~~~~~~~~~~~~~~~

Contains the primary deliverables for updating your MD topology:

- **update_params_<project>.in**: ParmEd input file with optimized multi-primitive torsion parameters. Each torsion is represented by multiple Fourier terms (typically n=1, 2, 3) for improved accuracy. This is the main file users need to update their GAFF/GAFF2 topology.
- **update_params_<project>.frcmod**: GAFF-style .frcmod file version of the optimized torsions (optional alternate format).
- **run_configuration.txt**: Human-readable summary of all AFFDO settings used for this run.
- **<project>.log**: Copy of the main log file for reference.

stats_summary/ folder
~~~~~~~~~~~~~~~~~~~~~

Contains summary statistics and plots for quick assessment:

- **dh_x-x-x-x_<fragment>.png**: Energy profile comparison plots for each optimized torsion showing Reference vs GAFF2 vs AFFDO curves.
- **fitting_summary.txt**: Human-readable text summary of optimization results including RMSE values and improvements for all torsions.
- **fitting_report.csv**: Machine-readable CSV with detailed statistics for each torsion.
- **<project>_fragments.png**: (If fragmentation was used) Visual representation showing how the molecule was fragmented and which torsions belong to each fragment.

topology.zip
~~~~~~~~~~~~

Archive containing the standard GAFF/GAFF2 topology files before optimization:

- **standard_GAFF2_topology/<project>.prmtop**: Unmodified GAFF2 topology file.
- **standard_GAFF2_topology/<project>.rst7**: Coordinate file.
- **standard_GAFF2_topology/<project>.mol2**: MOL2 format structure.
- **standard_GAFF2_topology/<project>.frcmod**: Original GAFF2 force field modifications.

These files are provided for reference and comparison with the optimized topology.

input_file/ folder
~~~~~~~~~~~~~~~~~~

Contains the original input file uploaded by the user (PDB/MOL2/MOL file), preserved for reference.

resources/ folder
~~~~~~~~~~~~~~~~~

Contains static resources used in the HTML report (logos, JavaScript libraries for interactive plots and 3D viewer, etc.).

Fragment-Specific Files (when fragmentation is active)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the fragmentation algorithm is executed (default for molecules with multiple torsions), the project will contain individual fragment folders with their detailed results:

- **<project>_f1/, <project>_f2/, <project>_f3/, etc.**: Separate folders for each fragment, each containing:

  - **<fragment>.mol**: Fragment structure file.
  - **<fragment>.log**: Fragment-specific log file.
  - **data.json**: Fragment-specific metadata and settings.
  - **update_params_<fragment>.in**: Fragment-specific ParmEd file with local atom numbering.
  - **update_params_mapped_<fragment>.in**: Fragment parameters mapped to parent molecule atom numbering.
  - **results/**: Detailed intermediate files for this fragment:

    - **conformers/**: Generated conformers for the fragment.
    - **conformer_minimization/**: XTB-minimized conformers.
    - **clusters/**: Clustered representative conformers.
    - **centroid_optimization_mm/**: MM optimized centroid structures.
    - **torsional_scan/**: Reference torsional scan results.
    - **constrained_optimization/**: Constrained optimization results for scan points.
    - **paramopt_works/**: Detailed parameter optimization results including iteration data and convergence information.
    - **paramtest_works/**: MM validation scans using GAFF2 and AFFDO parameters.
    - **torsion_works/**: Torsion analysis and selection results.

- **<project>_f1.zip, <project>_f2.zip, <project>_f3.zip, etc.**: Compressed archives of each fragment's complete results folder for easier download.

The fragmentation algorithm automatically splits molecules with multiple torsions into smaller fragments based on the configured fragment_size parameter (default: 3 consecutive torsions per fragment). This improves computational efficiency while maintaining accuracy. The main update_params_<project>.in file in workflow_files/ contains the merged and mapped parameters from all fragments using the parent molecule's atom numbering.

Topology‑Only Mode (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you invoked AFFDO with the "Topology‑Only" mode, AFFDO will stop as soon as it builds the standard GAFF/GAFF2 topology. No reparameterization-related files (workflow_files/, stats_summary/, fitting_report.html) will be included.

Fragmentation‑Only Mode (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you invoked AFFDO with the "Fragmentation‑Only" mode, AFFDO fragments the ligand and then immediately exits. You will receive the fragments visualization (<project>_fragments.png) and fragment structure files, but no topology or torsion reparameterization is performed.

Updating the GAFF Topology File Through ParmEd
-----------------------------------------------

Once AFFDO has generated your ParmEd update file (update_params_<project>.in), you can inject those torsion parameters into your GAFF/GAFF2 topology using our helper script: **update_topology.py**. This tool automates all the ParmEd calls and fully supports AFFDO's multi-primitive torsion format.

Under dual‑topology mode, it keeps only those torsion modifications that appear in both ligand states. This ensures consistent torsion updates across end‑states, ideal for alchemical free‑energy simulations.

Usage
~~~~~

To run the script, use the following command:

.. code-block:: bash

   python update_topology.py -p TOPOLOGY.parm7 -i update_params_project.in [--dual-topology]

**Required arguments:**

- ``-p`` / ``--topology``: Path to your Amber GAFF/GAFF2 topology file (.parm7).
- ``-i`` / ``--update-in``: AFFDO-generated ParmEd torsion update script (.in file) from the workflow_files/ folder.

**Optional arguments:**

- ``--dual-topology``: Apply updates only to torsions common to two ligands (residues 1 and 2).
- ``-h`` / ``--help``: Display detailed help and examples.

Examples
~~~~~~~~

Single topology (standard usage):

.. code-block:: bash

   python update_topology.py -p my_system.parm7 -i update_params_myproject.in

Dual topology (common torsions only):

.. code-block:: bash

   python update_topology.py -p my_system.parm7 -i update_params_myproject.in --dual-topology

This generates a new topology file named **new.prmtop** incorporating the optimized multi-primitive torsion parameters.

**Notes:**

- Ensure Python 3 and ParmEd are installed and accessible from your command line.
- The update_topology.py script is provided in the AFFDO resources/ folder or can be downloaded separately.
- Use ``python update_topology.py -h`` to display the help message at any time.

Tips for Safe Topology Updates
-------------------------------

When you move from AFFDO's torsion reparameterization into your MD or RBFE workflows, keep these in mind:

1. **Use identical ligand coordinates**: The exact same .mol / .pdb / .mol2 you gave AFFDO must be the one your MD engine reads. Any atom order or numbering mismatch will cause ParmEd to silently skip torsion updates, so double-check file consistency. Use the <project>.mol file from AFFDO's output to ensure consistency.

2. **Inspect ParmEd logs for errors**: After running update_topology.py (or your own ParmEd invocation), always check the generated log (parmed_update.log) or console output for warnings. This ensures you don't inadvertently launch production runs with default GAFF/GAFF2 torsions.

3. **Understand multi-primitive format**: AFFDO uses multiple Fourier terms (typically n=1, 2, 3) for each torsion to provide better fitting to quantum mechanical energy profiles. When inspecting your updated topology or the .in file, you will see multiple addDihedral commands for the same atom quartet with different periodicities—this is expected and provides improved accuracy compared to single-term representations.

4. **(Optional) Dual-topology for RBFE**: If you're doing a two-end-state free-energy transform, we recommend updating only the torsions shared by both ligands. Our ``--dual-topology`` flag in update_topology.py makes this easy, but you're free to use ParmEd directly if you prefer a different strategy.

Those few checks will give you confidence that your AFFDO-refitted torsions made it into your final topology.

Disclaimer
----------

Please be advised that AFFDO is part of an active development project. While we strive to provide accurate and reliable results, the underlying technology is continuously evolving, and there may be occasional updates or changes.

*Last updated on* |UPDATE_DATE|.
