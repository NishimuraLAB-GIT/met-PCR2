from Bio.Seq import Seq


class ConfirmMatch:
    def __init__(self) -> None:
        pass
    

    # 未完成により使用不可
    def barcode_match(self, fw_seq:str, fastq:dict, task='f') -> list:
        primer_length = len(fw_seq)
        match_seq = []
        for ID in fastq:
            fastq_seq = fastq[ID]
            fastq_length = len(fastq_seq)
            if task == "f":
                barcode = fastq_seq[:primer_length]
            else:
                barcode = fastq_seq[fastq_length - primer_length:]
            if barcode == fw_seq:
                match_seq.append(fastq_seq)
        return match_seq
    
    def solve_Y_R(self, dir) -> bool:
        # bool -> 配列が一致していると戻り値がTrue,そうでないときFalse
        if dir == "F":
            primer = self.primer
            fastq = self.fastq_seq
        else:
            # Rvのprimerは逆配列にして相補鎖で比較する
            primer = self.crate_complementary_strand(self.primer[::-1])
            fastq = self.fastq_seq[::-1]
        # Y_Rが入っている場合の配列一致の確認処理
        for idx in range(self.primer_length):
            if primer[idx] == "Y":
                if fastq[idx] == "C" or fastq[idx] == "T":
                    continue
                else:
                    return False
            elif primer[idx] == "R":
                if fastq[idx] == "A" or fastq[idx] == "G":
                    continue
                else:
                    return False
            elif primer[idx] == "C":
                if fastq[idx] == "C" or fastq[idx] == "T":
                    continue
                else:
                    return False
            elif primer[idx] != fastq[idx]:
                return False
            
        return True


    def primer_match(self, primer:str, fastq:dict, task="F") -> dict:
        self.primer = primer
        self.primer_length = len(primer)
        match_seq = dict()
        for ID in fastq:
            self.fastq_seq = fastq[ID]
            self.fastq_length = len(self.fastq_seq)
            if self.solve_Y_R(task):
                match_seq[ID] = self.fastq_seq
        
        return match_seq


    # 入力された配列の相補鎖を返す関数
    def crate_complementary_strand(self, sequence:str) -> str:
        sample_seq = Seq(sequence)
        seq_c = str(Seq(sample_seq).reverse_complement())
        return seq_c
    
    def length_match(self, amplicon:str, fw_primer:str, rv_primer:str, fastq:dict) -> dict:
        amplicon_length = len(fw_primer + amplicon + rv_primer)
        match_length_seq = dict()
        self.match_primer = fastq
        # self.macth_fw = self.primer_match(fw_primer, fastq)
        # self.macth_primer = self.primer_match(rv_primer, self.macth_fw, task="R")
        for ID in self.match_primer:
            match_seq = self.match_primer[ID]
            length = len(match_seq)
            if length == amplicon_length:
                match_length_seq[ID] = match_seq

        return match_length_seq

    def _find_C(self, amplicon:str) -> list:
        index_C = []
        dic_C = dict()
        for idx in range(len(amplicon)):
            if amplicon[idx] == "C":
                index_C.append(idx)
                dic_C[idx] = {"C":0, "T":0, "ERR":0}
        return index_C, dic_C
    
    def count_met_c(self, amplicon:str, fw_primer:str, rv_primer:str, pcr_products:dict):
        length_fw = len(fw_primer)
        length_rv = len(rv_primer)
        index_C, results = self._find_C(amplicon)
        for ID in pcr_products:
            seq = pcr_products[ID]
            len_seq = len(seq)
            comp_seq = seq[length_fw:len_seq - length_rv]
            # print(len(comp_seq))
            # print(len(amplicon))
            # print("#############################")
            for idx in index_C:
                if comp_seq[idx] == "C":
                    results[idx]["C"] += 1
                elif comp_seq[idx] == "T":
                    results[idx]["T"] += 1
                else:
                    results[idx]["ERR"] += 1
        
        return results

    def run(self):
        pass 