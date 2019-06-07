#!/bin/bash
#SBATCH --nodes=NNODE
#SBATCH --ntasks-per-node=TASKS_PER_NODE
#SBATCH --job-name=plates-ASPECTVER-REFINEMENT
#SBATCH --exclusive
#SBATCH --partition=high2
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#
#module unload openmpi

#module load impi local-gcc-6.3.0
#
time mpirun -n NCPU --bind-to hwthread --mca btl_openib_allow_ib 1 --mca btl openib,self,vader ./ASPECTVER convection-plates-spinup_ASPECTVER_grREFINEMENT.prm

