import os

from test import Exe

def initial_value():
    while True:
        print("使用するBatch.tomlファイルのパスを入力")
        Batch_path = input()
        if os.path.exists(Batch_path):
            break
        else:
            print("pathが正しくありません")
            print("再度入力をお願いします")

    while True:
        print("使用するfastqファイルを入力")
        fastq_path = input()
        if os.path.exists(fastq_path):
            break
        else:
            print("pathが正しくありません")
            print("再度入力をお願いします")

    print("** 指定したフォルダ直下にresultフォルダが生成されます **")
    results_path = input("出力先フォルダパスを入力")

    if results_path == "":
        results_path = "./"
        
    
    # output = "./results"
    # if not os.path.exists:
    #     os.makedirs(output)


    exe = Exe(fastq_path, Batch_path, results_path)
    exe.run()
    exit()

if __name__ == "__main__":
    initial_value()