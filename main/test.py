import json
import os

from log import log
from load_file import load_file
from read_match import ConfirmMatch
from graph.hist import HIST
from results import results
from Bio.Seq import Seq

# out.extendedFrags.fastqのファイルをmainフォルダ内に保存
# fastqファイルはパスじゃなくてファイル名を指定する

# Batch.tomlファイルをmainフォルダ内に保存

fastq_path = "out.extendedFrags.fastq"
toml_path = "./Batch.toml"

class Exe():
    def __init__(self, fastq_path, batch_path, out_path=None) -> None:
        self.fastq_path = fastq_path
        self.batch_path = batch_path
        self.out_path = os.path.join(out_path,"results")

    def run(self):
        # print(file_reader.fastq_load(fastq_path))

        # print(file_reader.load_toml(toml_path))



        # print(fastq)
        # print(type(toml_dict["entries"][0]))
        results_path = os.path.join(self.out_path,"results.json")
        if self.out_path == None:
            results_path = "./results.json"
        
        # インスタンスの生成
        file_reader = load_file()
        matching_read = ConfirmMatch()
        results_writer = results(self.out_path)
        log_writer = log(self.batch_path, self.fastq_path, self.out_path)

        # 設定ファイルのロード
        toml_dict = file_reader.load_toml(self.batch_path)
        # fastqファイルのロード
        fastq = file_reader.fastq_load(self.fastq_path)
        fastq_log = [
            "\n",
            "total_read",
            len(fastq)
        ]
        log_writer.add_log(fastq_log)

        with open(results_path,"w") as f:
            pass

        # sampleの取り出し
        sample = toml_dict["entries"]

        # 解析実行
        for record_dic in sample:
            # 必要な情報を変数に集める
            fw_primer = record_dic["fw_primer"]
            rv_primer = record_dic["rv_primer"]
            amplicon = record_dic["amplicon"]
            amplicon_length = len(amplicon)

            # ヒストグラム作成用のクラスのインスタンス
            hist_saver = HIST(record_dic["name"], amplicon_length, self.out_path)

            # ampliconとprimerの一致確認
            fw_macth_seq = matching_read.primer_match(fw_primer, fastq)
            # Rv側のprimerの一致確認
            match_seq = matching_read.primer_match(rv_primer, fw_macth_seq, task = "R")
            # 一致配列の長さで選抜
            match_length_seq = matching_read.length_match(amplicon,fw_primer,rv_primer, match_seq)
            # 目的配列でのmethylationを計算
            results_analyze = matching_read.count_met_c(amplicon,fw_primer,rv_primer,match_length_seq)

            # resultsの表示
            print(record_dic["name"])
            print("fw_primer")
            print(len(fw_macth_seq))
            print("rv_primer")
            print(len(match_seq))
            print("length")
            print(len(match_length_seq))
            log_text = [
                record_dic["name"],
                "amplicon" + ":" + record_dic["amplicon"],
                "fw_primer" + ":" + fw_primer,
                "rv_primer" + ":" + rv_primer,
                "Selection",
                "fw_primer",
                len(fw_macth_seq),
                "rv_primer",
                len(match_seq),
                "length",
                len(match_length_seq)
            ]
            log_writer.add_log(log_text)
            # print("results")
            # print(results)

            # resultsをjsonファイルに保存
            with open(results_path, "a") as f:
                result_json = {record_dic["name"]:results_analyze}
                json.dump(result_json, f, indent=2)

            # jsonをtsvファイルに変換
            rv_primer = str(Seq(rv_primer).reverse_complement())
            result = results_writer.output_results(result_json, amplicon+rv_primer, hist_saver)
            # ヒストグラムを.pngで保存
            hist_saver.save_graph()
            # print(result)

        # logger = log()
        # logger.outputlog(self.batch_path, self.fastq_path, self.out_path)
        # B = ["A", "T","G","C"]

