#!/usr/bin/env python3
import subprocess
# Make a list of aspect versions
aspect_versions = ['aspect-head','aspect-e6af77b']
tasks_per_node = 64
refinement_table = [[4,4],[5,16]] # each entry is [refinement,number of nodes]

for aspect in aspect_versions:
    for refinement,nnode in refinement_table:
        #make new slurm file
        slurm_filename = "convection-plates-spinup_" + aspect + "_gr{:d}".format(refinement) + ".slurm"
        prm_filename = "convection-plates-spinup_" + aspect + "_gr{:d}".format(refinement) + ".prm"
        
        table = dict()
        table['ASPECTVER']=aspect
        table['NNODE']="{:d}".format(nnode)
        table['NCPU']="{:d}".format(int(nnode*tasks_per_node))
        table['PRMFILE']=prm_filename
        table['REFINEMENT']="{:d}".format(refinement)
        table['JOBNAME']=prm_filename
        table['TASKS_PER_NODE']="{:d}".format(tasks_per_node)
                
        subprocess.run(["cp","convection-plates-spinup-base.prm",prm_filename])
        subprocess.run(["cp","convection-plates-spinup-base.slurm",slurm_filename])
        for key in table.keys():
            subprocess.run(["sed","-i","s/"+key+"/"+table[key]+"/g",slurm_filename])
            subprocess.run(["sed","-i","s/"+key+"/"+table[key]+"/g",prm_filename])
        
