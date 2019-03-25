#!/usr/bin/env python3
import subprocess
# Make a list of aspect versions
aspect_versions = ['aspect-head','aspect-e6af77b']
tasks_per_node = 64
refinement_table = [[3,1],[4,2],[5,4]] # each entry is [refinement,number of nodes]

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
                
        subprocess.run(["cp","coolingsphere_base.prm",prm_filename])
        subprocess.run(["cp","coolingsphere_base.slurm",slurm_filename])
        for key in table.keys():
            subprocess.run(["sed","-i","s/"+key+"/"+table[key]+"/g",slurm_filename])
            subprocess.run(["sed","-i","s/"+key+"/"+table[key]+"/g",prm_filename])
        
