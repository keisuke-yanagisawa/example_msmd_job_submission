import jinja2
import os

def generate_a_config_file(pdbid, cid, iter_index):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
    template = env.get_template("template.yaml")
    with open(f"{pdbid}.{cid}.{iter_index}.yaml", "w") as fout:
        fout.write(template.render({
            "ITER_INDEX": iter_index,
            "PROTEIN": pdbid, 
            "PROBE": cid
        }))


cids   = "A17 E14 E15 E16 E17 E18 E19".split(" ")
pdbids = "2WEA 2CYB 1ZUA 1YMS 1WBI 1W4P 1TU6 1TT1 1JZF 1H60 1H4G 1E0X 1CXV 1BK9 1HEE".split(" ")

for cid in cids:
    for pdbid in pdbids:
        for iter_index in ["0-3", "4-7", "8-11", "12-15", "16-19"]:
            generate_a_config_file(pdbid, cid, iter_index)


