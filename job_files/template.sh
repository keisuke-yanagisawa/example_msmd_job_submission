#$ -cwd
#$ -l f_node=1
#$ -l h_rt=12:00:00
#$ -N MSMD.{{PROTEIN}}.{{PROBE}}.{{ITER_INDEX}}

cd $HOME/workspace/0010_invmsmd_alignment/20230719_inverseMSMD_xiap2
module load singularity/3.6.3
singularity exec -B /gs -B /apps -B /scr --nv exprorer_msmd/.devcontainer/exprorer_msmd.sif exprorer_msmd/exprorer_msmd config_files/{{PROTEIN}}.{{PROBE}}.{{ITER_INDEX}}.yaml
