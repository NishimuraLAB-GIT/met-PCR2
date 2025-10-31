import os 
import matplotlib.pyplot as plt


from collections import defaultdict
class HIST():
    def __init__(self, dataname, amplicon_length, results_path) -> None:
        self.graph_data = defaultdict(dict)
        self.met_cls = ["CG","CHG","CHH"]
        self.save_path = os.path.join(results_path, dataname)
        self.length = amplicon_length

    # グラフ用のデータを登録する関数
    def registration(self, pos, met_rate, cls):
        self.graph_data[cls][pos] = met_rate

    # 作成したグラフを.pngで保存する関数
    def save_graph(self):
        graph_data, height_data = self._create_graph()
        plt.bar(graph_data[0],height_data[0], align="edge",width=-0.3)
        plt.bar(graph_data[1],height_data[1], align="center")
        plt.bar(graph_data[2],height_data[2], align="edge", width=0.3)

        plt.legend(self.met_cls)
        print(self.save_path)
        plt.savefig(self.save_path)
        plt.clf()
        

    # グラフ用のデータ作成関数
    def _create_graph(self):
        row_data = defaultdict(list)
        height_data = defaultdict(list)
        for cls in self.met_cls:
            for pos in self.graph_data[cls]:
                row_data[cls].append(pos)
                height_data[cls].append(self.graph_data[cls][pos] * 100)

                
            # for pos in range(self.length):
            #     if str(pos) in self.graph_data[cls]:
            #         met_rate = self.graph_data[cls][pos] * 100
            #         row_data[cls].append(met_rate)
            #     else:
            #         row_data[cls].append(0)
        graph_data = [row_data["CG"], row_data["CHG"], row_data["CHH"]]
        height_data = [height_data["CG"], height_data["CHG"], height_data["CHH"]]

        return graph_data, height_data
        
