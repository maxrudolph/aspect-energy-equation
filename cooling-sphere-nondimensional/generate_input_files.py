#!/usr/bin/env python3
import subprocess
# Make a list of aspect versions
aspect_versions = ['aspect-head','aspect-e6af77b']
cluster = 'coeus'
if cluster is 'coeus':

    tasks_per_node = 20
    refinement_table = [[3,1],[4,5],[5,32]] # each entry is [refinement,number of nodes]
    mpirun_options = '--binding yes'
elif cluster is 'peloton2':
    tasks_per_node = 64
    refinement_table = [[3,1],[4,2],[5,8]] # each entry is [refinement,number of nodes]
    mpirun_options = '--bind-to hwthread --mca btl_openib_allow_ib 1 --mca btl openib,self,vader --report-bindings'


for aspect in aspect_versions:
    for refinement,nnode in refinement_table:
        #make new slurm file
        slurm_filename = "coolingsphere_" + aspect + "_gr{:d}".format(refinement) + ".slurm"
        prm_filename = "coolingsphere_" + aspect + "_gr{:d}".format(refinement) + ".prm"

        table = dict()
        table['ASPECTVER']=aspect
        table['NNODE']="{:d}".format(nnode)
        table['NCPU']="{:d}".format(int(nnode*tasks_per_node))
        table['PRMFILE']=prm_filename
        table['REFINEMENT']="{:d}".format(refinement)
        table['TASKS_PER_NODE']="{:d}".format(tasks_per_node)
        table['MPIRUN_OPTIONS']=mpirun_options

        subprocess.run(["cp","coolingsphere_base.prm",prm_filename])
        subprocess.run(["cp","coolingsphere_base.slurm",slurm_filename])
        for key in table.keys():
            subprocess.run(["sed","-i","s/"+key+"/"+table[key]+"/g",slurm_filename])
            subprocess.run(["sed","-i","s/"+key+"/"+table[key]+"/g",prm_filename])
        
