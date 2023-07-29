import os

def submit_a_job(pdbid, cid, iter_index):
    os.system(f"qsub -g tga-pharma $HOME/workspace/0010_invmsmd_alignment/20230719_inverseMSMD_xiap2/job_files/MSMD.{pdbid}.{cid}.{iter_index}.sh")


cids   = "A17 E14 E15 E16 E17 E18 E19".split(" ")
pdbids = "2WEA 2CYB 1ZUA 1YMS 1WBI 1W4P 1TU6 1TT1 1JZF 1H60 1H4G 1E0X 1CXV 1BK9 1HEE".split(" ")

for cid in cids:
    for pdbid in pdbids:
        for iter_index in ["0-3", "4-7", "8-11", "12-15", "16-19"]:
            submit_a_job(pdbid, cid, iter_index)


