.. include:: ../affdo_docs_common.rst

Installation Guide 
==================

AFFDO is a python based package which requires a number of dependencies. |AFFDO_VERSION| supports Linux and MacOS operating systems and 
requires python 3.8. The recommended way for the installation is through miniconda. 

**Step 1:** Contact ATTMOS through `info@attmosdiscovery.com <info@attmosdiscovery.com>`_ and obtain a copy of |AFFDO_VERSION|. Extract the content into your local hard drive.
We will refer to the main AFFDO folder (contains main.py, lib, resources, etc.) as AFFDO_HOME below.

**Step 2:** Install miniconda. Note that we assume Linux operating system here.  

.. code-block:: none

	mkdir -p ~/Apps/miniconda3
	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/Apps/miniconda3/miniconda.sh
	bash ~/Apps/miniconda3/miniconda.sh -b -u -p ~/Apps/miniconda3
	rm -rf ~/Apps/miniconda3/miniconda.sh
	~/Apps/miniconda3/bin/conda init bash

**Step 3:** Create a new conda environment and install dependencies.

.. code-block:: none

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


**Step 4:** Install `QUICK QM package <https://github.com/merzlab/QUICK>`_. GNU compiler tool chain is assumed here. Note that we compile serial CPU version only.
For installing other versions, users shall refer to `QUICK installation guide <https://quick-docs.readthedocs.io/en/23.8.0/installation-guide.html#installation>`_. 

.. code-block:: none

	cd ~/Apps
	git clone https://github.com/merzlab/QUICK.git -b QUICK-23.08-with-patches quick
	mkdir -p ./quick/build && cd ./quick/build
	cmake .. -DCOMPILER=GNU -DCMAKE_INSTALL_PREFIX=$(pwd)/../install
	make -j2 install
	. ~/Apps/quick/install/quick.rc

**Step 5:** Install `geomeTRIC package <https://github.com/leeping/geomeTRIC>`_.

.. code-block:: none

	cd ~/Apps
	git clone https://github.com/leeping/geomeTRIC.git
	cd geomeTRIC
	pip install .

**Step 6:** Install other python dependencies from AFFDO_HOME folder.

.. code-block:: none

	cd ${AFFDO_HOME}
	pip install .


**Step 7:** Source affdo.rc file to set the environment variables. It is recommended to add this command into your shell configuration file (.bashrc, .bash_profile, etc.)

.. code-block:: none

	. ${AFFDO_HOME}/affdo.rc
    

This completes the local AFFDO installation. You can follow the `hands on tutorial <hands-on-tutorials.html>`_ to proceed from here. 

**Step 8 (optional):** You can also use remote computers or cloud instanaces for computationally expensive steps of the workflow. In order to do so, install 
`AmberTools <https://ambermd.org/AmberTools.php>`_, `QUICK <https://github.com/merzlab/QUICK>`_, `geomeTRIC <https://github.com/leeping/geomeTRIC>`_, and `xtb <https://github.com/grimme-lab/xtb>`_ packages in those systems. Then create a host files for each system in AFFDO_HOME directory. These files must have the .host.json file extension
and must have the following format.

.. code-block:: none

	{
		"username":"attmos",
		"port_number":xx,
		"ip_address":"xx.xx.xx.xx",
		"amber_home":"~/Apps/amber/install",
		"xtb_path":"~/Apps/xtb-6.6.0/install/bin",
		"quick_home": "~/Apps/quick/install",
		"scratch_dir":"/tmp",
		"number_of_gpus":4,
		"pre_job_command":". /etc/profile && module load amber/23 quick/23.08 xtb/6.6.1 geometric/1.0.1",
		"post_job_command":"module unload amber/23 xtb/6.6.1 geometric/1.0.1"
	}

In jupyter-notebook cells that allows remote execution, you can specify the hostname (the file prefix eg., remote to use remote.host.json file) and select the sytem you want to use. 

*Last updated on 02/09/2024.*



