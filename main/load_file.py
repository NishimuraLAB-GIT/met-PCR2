import toml

from tomllib import load
from Bio import SeqIO

class load_file:
    def __init__(self) -> None:
        pass

    def fastq_load(self, fastq_path:str) -> dict:
        fastq_dic = dict()
        for recs in SeqIO.parse(fastq_path,"fastq"):
            fastq_dic[recs.id] = recs.seq

        return fastq_dic
    
    def load_toml(self, toml_path:str) -> dict:
        # with open(toml_path,"rb") as f:
        #     toml = load(f)
        dict_toml = toml.load(open(toml_path,encoding="utf-8"))

        return dict_toml
    
    
