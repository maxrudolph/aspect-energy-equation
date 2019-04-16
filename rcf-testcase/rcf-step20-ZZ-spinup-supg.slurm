#!/bin/bash
#SBATCH --nodes=25
#SBATCH --ntasks-per-node=20
#SBATCH --job-name=rcf-step20-ZZ-spinup-supg
#SBATCH --exclusive
#SBATCH --exclude=compute038
#SBATCH --partition=medium
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#
module purge
module load impi local-gcc-6.3.0
#
time mpirun -n 500 ./aspect-supg rcf-step20-ZZ-spinup-supg.prm
