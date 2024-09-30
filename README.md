<p align="right">
<img src="https://github.com/ATTMOS/AFFDOWS/actions/workflows/update-docs.yml/badge.svg">
</p>
<p align="left">
<img width="320" height="75" src="./resources/logo-no-background.png">
</p>
An Automated Force Field Developer and Optimizer developed by ATTMOS Inc. 

Features
--------
* Allows generating improved ligand-specific Generalized Amber Force Field (GAFF) parameters. 

Installation
------------
Please follow these steps for installing jupyter-notebook version of AFFDO. 

**Step 1:** Clone the AFFDO repository into your local hard drive. Note that all AFFDO developers are expected to have their ssh keys set up in the GitHub account. We will refer to the main AFFDO folder (contains main.py, lib, resources, etc.) as AFFDO_HOME below. 

```bash
git clone git@github.com:ATTMOS/AFFDO.git
```

**Step 2:** Install miniconda. Note that we assume Linux operating system here.

```bash
mkdir -p ~/Apps/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -O ~/Apps/miniconda3/miniconda.sh
bash ~/Apps/miniconda3/miniconda.sh -b -u -p ~/Apps/miniconda3
rm -rf ~/Apps/miniconda3/miniconda.sh
~/Apps/miniconda3/bin/conda init bash
```

**Step 3:** Create a new conda environment and install dependencies.

```bash
conda create -n "env38" python=3.8
conda activate env38

# Install AmberTools
conda install -c conda-forge ambertools --update-deps << EOF
y
EOF

# Install xtb
conda config --add channels conda-forge
conda install xtb-python << EOF
y
EOF
```

**Step 4:** Install [QUICK QM package] (https://github.com/merzlab/QUICK). GNU compiler tool chain is assumed here. Note that we compile serial CPU version only. For installing other versions, users shall refer to [QUICK installation guide](https://quick-docs.readthedocs.io/en/23.8.0/installation-guide.html#installation).

```bash
cd ~/Apps
git clone https://github.com/merzlab/QUICK.git -b QUICK-23.08-with-patches quick
mkdir -p ./quick/build && cd ./quick/build
cmake .. -DCOMPILER=GNU -DCMAKE_INSTALL_PREFIX=$(pwd)/../install
make -j2 install
. ~/Apps/quick/install/quick.rc
```

**Step 5:** Install [geomeTRIC package](https://github.com/leeping/geomeTRIC).

```bash
cd ~/Apps
git clone https://github.com/leeping/geomeTRIC.git
cd geomeTRIC
pip install .
```

**Step 6:** Install other python dependencies from AFFDO_HOME folder.

```bash
cd ${AFFDO_HOME}
pip install .
```

**Step 7:** Source affdo.rc file to set the environment variables. It is recommended to add this command into your shell configuration file (.bashrc, .bash_profile, etc.)

```bash
. ${AFFDO_HOME}/affdo.rc
```


**Step 8 (optional):** You can also use remote computers or cloud instanaces for computationally expensive steps of the workflow. In order to do so, install AmberTools, QUICK, geomeTRIC, and xtb packages in those systems. Then create a host files for each system in AFFDO_HOME directory. These files must have the .host.json file extension and must have the following format.

```json 
{
        "username":"attmos",
        "port_number":22,
        "ip_address":"xx.xx.xx.xx",
        "amber_home":"~/Apps/amber/install",
        "xtb_path":"~/Apps/xtb-6.6.0/install/bin",
        "quick_home": "~/Apps/quick/install",
        "scratch_dir":"/tmp",
        "number_of_gpus":4,
        "pre_job_command":". /etc/profile && module load amber/23 quick/23.08 xtb/6.6.1 geometric/1.0.1",
        "post_job_command":"module unload amber/23 xtb/6.6.1 geometric/1.0.1"
}
```

This completes the AFFDO installation. 

Usage
-----
Launch AFFDO using jupyter-notebook as: `jupyter-notebook main.ipynb` and follow this [hands on tutorial](https://attmos.github.io/AFFDO-docs/user/hands-on-tutorials.html). 

Limitations
-----------
Currently supports Linux and macOS systems only. 

Citation
--------
Please cite AFFDO-24.01 as follows.

Manathunga, M.; Aktulga H. M.; Blanco-Gonzalez, A.; Götz, A. W.; Merz, K. M.; York, D. M. AFFDO-24.01 ATTMOS Inc. East Lansing, MI, 2024.

Known issues
------------
* Antechamber tool of AmberTools fails to run on macOS\
  If you installed AmberTools using miniconda, it is possible that antechamber fails to run properly on new macOS versions. To prevent this issue, compile AmberTools from the source rather than installing the miniconda version.

* Interactive widgets not showing up in jupyter-notebook version\
   If the widgets are not showing up in the jupyter-notebook version, you may have to enable the corresponding extension in jupyter. This
   can be done by executing the following commands in the terminal.\
   *jupyter nbextension install --py widgetsnbextension --user*\
   *jupyter nbextension enable widgetsnbextension --user --py*

* QUICK/geomeTRIC torsional scans fail with: *subprocess.CalledProcessError: Command 'quick.mpi quick.qkin > quick.out' returned non-zero exit status 127.*\
   QUICK compilation results in four executables (quick, quick.cuda, quick.MPI, quick.cuda.MPI) but geomeTRIC looks for an executable named *quick.mpi*. While this problem has to be fixed from geomeTRIC side, the easiest workaround to get the calculations running is by creating a symlink to the executable we want. For eg. a symlink for *quick.cuda* can be created by running the following command in the terminal, inside the QUICK bin directory.\
   *ln -s quick.mpi quick.cuda*
* QUICK/geomeTRIC torsional scans fail with: *RuntimeError: Valid values of engine are: tera, qchem, psi4, gmx, molpro, openmm, qcengine, gaussian, ase.*\
   Support for QUICK engine in geomeTRIC is currently enabled only in the development version of geomeTRIC. If you encounter this error, it is very likely that you installed geomeTRIC using pip rather than building from the source. To fix the issue, uninstall the geomeTRIC, clone latest code from GitHub and build. 

Bug reports and comments
------------------------
 If you experience any installation or runtime issues, please report them to us through the issues section of this repository. We appreciate any feedback.

License
-------
This program is subject to commercial license. A copy of the license can be found [here](./LICENSE).




