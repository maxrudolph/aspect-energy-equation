#!/bin/bash
#SBATCH -p high2
#SBATCH -n 128
#SBATCH --exclusive
#SBATCH --ntasks-per-node=64
#SBATCH --job-name=shell_simple_ASPECTVER
#SBATCH --exclusive
#SBATCH --partition=high2
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#

mpirun -n 128 --bind-to hwthread --mca btl_openib_allow_ib 1 --mca btl openib,self,vader --report-bindings ASPECTVER CASE.prm
