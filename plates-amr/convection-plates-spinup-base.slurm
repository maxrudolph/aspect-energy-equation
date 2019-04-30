#!/bin/bash
#SBATCH --nodes=NNODE
#SBATCH --ntasks-per-node=TASKS_PER_NODE
#SBATCH --job-name=plates-ASPECTVER-REFINEMENT
#SBATCH --exclusive
#SBATCH --partition=medium
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#
module load impi gcc-8.2.0

#module load impi local-gcc-6.3.0
#

# Make the 0th timestep slurm file
cat convection-plates-spinup_ASPECTVER_amrREFINEMENT.prm > convection-plates-spinup_ASPECTVER_amrREFINEMENT_time0.prm
cat timestep_zero.prm >> convection-plates-spinup_ASPECTVER_amrREFINEMENT_time0.prm

time mpirun -n NCPU ./ASPECTVER convection-plates-spinup_ASPECTVER_amrREFINEMENT_time0.prm

time mpirun -n NCPU ./ASPECTVER convection-plates-spinup_ASPECTVER_amrREFINEMENT.prm

