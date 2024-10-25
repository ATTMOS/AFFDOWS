<p align="left">
<img width="320" height="75" src="./source/dev/images/logo-no-background.png">
</p>
An Automated Force Field Developer and Optimizer developed by ATTMOS Inc. 

Building the documentation
--------------------------

AFFDO documentation can be built in .html format by following the steps below.  

1. Make sure python (v3.6>), pip and all python dependencies specified in requirements.txt in AFFDO root directory are installed in your system.
2. Inside the docs folder, run *make html*. The developer manual is not included in the documentation by default. To include it run *make devhtml*.
3. Open the generated documentation by running *open _build/html/index.html* in the terminal.

To generate the .pdf version of the documentation, follow the steps below. 

1. Inside the docs folder, run *make pdf*
2. Open the generated documentation by running *open _build/affdo.pdf* in the terminal.
