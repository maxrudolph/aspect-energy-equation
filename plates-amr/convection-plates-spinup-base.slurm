#!/bin/bash
#SBATCH --nodes=NNODE
#SBATCH --ntasks-per-node=TASKS_PER_NODE
#SBATCH --job-name=plates-ASPECTVER-REFINEMENT
#SBATCH --exclusive
#SBATCH --partition=high2
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#
module unload openmpi
module load openmpi/4.0.5-mpi-io
# Make the 0th timestep slurm file
cat convection-plates-spinup_ASPECTVER_amrREFINEMENT.prm > convection-plates-spinup_ASPECTVER_amrREFINEMENT_time0.prm
cat timestep_zero.prm >> convection-plates-spinup_ASPECTVER_amrREFINEMENT_time0.prm

time mpirun -n NCPU --bind-to core \
	./ASPECTVER convection-plates-spinup_ASPECTVER_amrREFINEMENT_time0.prm

time mpirun -n NCPU --bind-to core \
	./ASPECTVER convection-plates-spinup_ASPECTVER_amrREFINEMENT.prm

