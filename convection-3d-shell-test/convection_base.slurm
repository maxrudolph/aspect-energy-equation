#!/bin/bash
#SBATCH -p high2
#SBATCH -n NCPU
#SBATCH --exclusive
#SBATCH --ntasks-per-node=TASKS_PER_NODE
#SBATCH --job-name=JOBNAME
#SBATCH --exclusive
#SBATCH --partition=high2
#SBATCH --time=4-00:00:00
#SBATCH --switches=1
#

mpirun -n NCPU --bind-to hwthread --mca btl_openib_allow_ib 1 --mca btl openib,self,vader --report-bindings ./ASPECTVER PRMFILE
