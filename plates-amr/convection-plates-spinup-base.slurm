#!/bin/bash
#SBATCH --nodes=NNODE
#SBATCH --ntasks-per-node=TASKS_PER_NODE
#SBATCH --job-name=plates-ASPECTVER-REFINEMENT
#SBATCH --exclusive
#SBATCH --partition=high2
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#
#module load impi gcc-7.2.0
module load openmpi/4.0.1
# Make the 0th timestep slurm file
cat convection-plates-spinup_ASPECTVER_amrREFINEMENT.prm > convection-plates-spinup_ASPECTVER_amrREFINEMENT_time0.prm
cat timestep_zero.prm >> convection-plates-spinup_ASPECTVER_amrREFINEMENT_time0.prm

time mpirun -n NCPU --bind-to core --mca btl_openib_allow_ib 1 --mca btl openib,self,vader --report-bindings ./ASPECTVER convection-plates-spinup_ASPECTVER_amrREFINEMENT_time0.prm

time mpirun -n NCPU --bind-to core --mca btl_openib_allow_ib 1 --mca btl openib,self,vader --report-bindings ./ASPECTVER convection-plates-spinup_ASPECTVER_amrREFINEMENT.prm

