#!/bin/bash
#SBATCH -p medium
#SBATCH -n NCPU
#SBATCH --exclusive
#SBATCH --ntasks-per-node=TASKS_PER_NODE
#SBATCH --job-name=shell_simple_ASPECTVER_REFINEMENT
#SBATCH --exclusive
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#
mpirun -n NCPU MPIRUN_OPTIONS  ./ASPECTVER PRMFILE
