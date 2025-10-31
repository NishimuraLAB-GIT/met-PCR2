import os
from load_file import load_file

class log():
    def __init__(self, batch, fastq, output_dir) -> None:
        self.output_dir = output_dir
        self.batch = batch
        self.fastq = fastq
        self.log_file = os.path.join(output_dir,"log.txt")
        with open(self.log_file, "a") as f:
            f.writelines("used file\n")
            f.writelines(self.fastq+"\n")
            f.writelines(self.batch+"\n\n")
            f.write("File contents"+"\n")

    def outputlog(self, batch, fastq, output_dir):
        self.batch = batch
        self.fastq = fastq
        log_file = os.path.join(output_dir,"log.txt")
        with open(log_file, "a") as f:
            f.writelines("used file\n")
            f.writelines(self.fastq+"\n")
            f.writelines(self.batch+"\n\n")
            self._createdata(f)
    
    def _createdata(self, f_obj):
        batch_load = load_file()
        batch_dict = batch_load.load_toml(self.batch)
        f_obj.writelines("File contents\n")
        for entry in batch_dict["entries"]:
            f_obj.writelines("\n".join(str(k)+","+str(v) for k, v in entry.items()))
            f_obj.write("\n\n")
        
    def add_log(self, textlist:list):
        # log.txtに書き込み
        with open(self.log_file, "a") as f:
            for text in textlist:
                if isinstance(text, str):
                    f.write(text+"\n")
                else:
                    f.write(str(text) + "\n")
            f.write("\n\n")
