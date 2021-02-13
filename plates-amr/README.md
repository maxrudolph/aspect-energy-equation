# Plate-driven mantle flow with AMR

The files in this direcotry support global mantle flow simulations with prescribed plate motions and AMR.

convection-plates-spinup-base.prm : This file is a template from which input files for the spinup phase of the calculation are generated. The spinup phase consists of

1. Timestep 0, in which AMR is applied to the initial conditions
2. Spinup for 150 Myr, starting with the initial plate motion stage

The remainder of the calculation, with time-dependent plate motions, is then carried out using an input file generated from convection-plates-continue-base.prm

To generate the actual input files (.prm and .slurm), we run ``generate_input_files.py``. In this script you will need to specify
1. the number of MPI processes per node
2. number of nodes
3. initial refinement level

Potential issues
- during initial adaptive refinement, the Stokes solver can take a very long time to converge.
- 