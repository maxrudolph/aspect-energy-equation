#!/bin/bash
#SBATCH --nodes=NNODE
#SBATCH --ntasks-per-node=TASKS_PER_NODE
#SBATCH --job-name=cont-plates-ASPECTVER-REFINEMENT
#SBATCH --exclusive
#SBATCH --partition=high2
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#
module unload openmpi
export PATH=/home/rudolph/sw/openmpi-4.0.2/bin:$PATH
#module load impi local-gcc-6.3.0
#
time mpirun -n NCPU \
	--bind-to core \
	--mca btl_openib_allow_ib 1 \
	--mca btl openib,self,vader \
	./ASPECTVER convection-plates-continue_ASPECTVER_grREFINEMENT.prm

