#!/bin/bash
#SBATCH --nodes=NNODE
#SBATCH --ntasks-per-node=TASKS_PER_NODE
#SBATCH --job-name=cont-plates-ASPECTVER-REFINEMENT
#SBATCH --exclusive
#SBATCH --partition=high2
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#
#module unload openmpi
module load slurm
module load openmpi/4.1.0-mpi-io
#module load impi local-gcc-6.3.0
#
time mpirun -n NCPU ./ASPECTVER convection-plates-continue_ASPECTVER_grREFINEMENT.prm

