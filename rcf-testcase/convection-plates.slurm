#!/bin/bash
#SBATCH --nodes=16
#SBATCH --ntasks-per-node=64
#SBATCH --job-name=rcf-step20-ZZ-spinup-supg
#SBATCH --exclusive
#SBATCH --partition=high2
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#
module unload openmpi

#module load impi local-gcc-6.3.0
#
time mpirun -n 1024 --bind-to hwthread --mca btl_openib_allow_ib 1 --mca btl openib,self,vader ./aspect-e* convection-plates.prm

