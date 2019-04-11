#!/bin/bash
#SBATCH --nodes=25
#SBATCH --ntasks-per-node=20
#SBATCH --job-name=shell_simple_3d_suev_gr4
#SBATCH --exclusive
#SBATCH --partition=medium
#SBATCH --time=4-00:00:00
#
module purge
module load impi local-gcc-6.3.0
#
time mpirun -n 500 ./aspect-suev shell_simple_3d_suev-gr4.prm
