import csv
import os
from collections import defaultdict

class results():
    def __init__(self, results_path) -> None:
        self.result = dict()
        self.folder_path = results_path
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)
        
    def output_results(self, results, amplicon, hist=None):
        self.hist = hist
        for sample_name in results:
            self._create_tsv(sample_name)
            self.result[sample_name] = defaultdict(list)
            for idx in results[sample_name]:
                cls = self._classification(amplicon, idx)
                self.result[sample_name][cls].append({idx:results[sample_name][idx]})
            self._save(sample_name)
        return self.result
    
    # 保存用のtsvファイルの作成
    def _create_tsv(self, file_name):
        path = os.path.join(self.folder_path,file_name+".tsv")
        with open(path,"w") as f:
            pass
        return
    
    # tsvファイルを書き換え保存する関数
    def _save(self,file_name):
        path = os.path.join(self.folder_path,file_name+".tsv")
        with open(path, "a", newline="") as f:
            w = csv.writer(f, delimiter="\t")
            w.writerow(["chx", "pos", "met_rate", "C", "T", "ERR"])
            self._tsv_writer(w,file_name)
        return

    # メチル化Cの種類の判定する関数
    def _classification(self, sequence, C_index):
        ret = ["CG","CHG","CHH"]
        C_index = int(C_index)
        if sequence[C_index+1] == "G":
            return ret[0]
        elif sequence[C_index+2] == "G":
            return ret[1]
        else:
            return ret[2]
        
    # tsvに一行ずつ書き込む関数
    def _tsv_writer(self, writer, file_name):
        res = self.result[file_name]
        ret = ["CG","CHG","CHH"]
        for cls in ret:
            for rec in res[cls]:
                for key, value in rec.items():
                    C = rec[key]["C"]
                    T = rec[key]["T"]
                    ERR = rec[key]["ERR"]
                    if C + T == 0:
                        continue
                    met_rate = C / (C + T)
                    line = [cls, key, met_rate, C, T, ERR]
                    self.hist.registration(key,met_rate,cls)
                    writer.writerow(line)