.. include:: ../affdo_docs_common.rst

Known Issues of Current Version 
===============================================
*Current version:* |AFFDO_VERSION|

AFFDO is under continous development and as of the latest version, we have detected
the issues listed below. If you find anything other than these, please feel free to
report any bugs or issues through: `affdo@attmosdiscovery.com <affdo@attmosdiscovery.com>`_.

* Interactive widgets not showing up in jupyter-notebook version

If the widgets are not showing up in the jupyter-notebook version, you may have to enable the corresponding extension in jupyter. This can be done by executing the following commands in the terminal.

.. code-block:: none

    jupyter nbextension install --py widgetsnbextension --user
    jupyter nbextension enable widgetsnbextension --user --py

* QUICK/geomeTRIC torsional scans fail with:

.. code-block:: none

    subprocess.CalledProcessError: Command 'quick.mpi quick.qkin > quick.out' returned non-zero exit status 127.

QUICK compilation results in four executables (quick, quick.cuda, quick.MPI, quick.cuda.MPI) but geomeTRIC looks for an executable named quick.mpi. While this problem has to be fixed from geomeTRIC side, the easiest workaround to get the calculations running is by creating a symlink to the executable we want. For eg. a symlink for quick.cuda can be created by running the following command in the terminal, inside the QUICK bin directory.

.. code-block:: none

    ln -s quick.mpi quick.cuda

* QUICK/geomeTRIC torsional scans fail with:

.. code-block:: none

    RuntimeError: Valid values of engine are: tera, qchem, psi4, gmx, molpro, openmm, qcengine, gaussian, ase.

Support for QUICK engine in geomeTRIC is currently enabled only in the development version of geomeTRIC. If you encounter this error, it is very likely that you installed geomeTRIC using pip rather than building from the source. To fix the issue, uninstall the geomeTRIC, clone latest code from GitHub and build.


*Last updated on 01/31/2024.*
