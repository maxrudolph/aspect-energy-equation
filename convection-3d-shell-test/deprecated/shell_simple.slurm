#!/bin/bash
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=20
#SBATCH --job-name=shell_simple_3d
#SBATCH --exclusive
#SBATCH --partition=medium
#SBATCH --time=4-00:00:00
#
module purge
module load impi local-gcc-6.3.0
#
time mpirun -n 80 ./aspect shell_simple_3d.prm
