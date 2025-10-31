# met-PCR2

## setup
1. Pythonをインストール(ver-3.11.1で動作確認)
2. 任意の作業ディレクトリを作成
3. met-PCR2のインストールと必要ライブラリのインストール

```
git clone https://github.com/NishimuraLAB-GIT/met-PCR2

pip install -r requirements.txt
```

## analysis
- 必要なもの
    - Fastqシーケンスファイル
    - Batch.tomlファイル
        - インストールした`main`ディレクトリ内にテンプレートが存在するので参照
        - 不要な[[entry]]ブロック(`name amplicoon`,`fw_primer`,`rv_primer`からなるもの)は削除する

### GUIでの実行
1. 起動コマンド
```
python bs_seq.py
```

2. 表示された画面から準備した`Batch.toml`ファイルと`fastq`ファイルを選択またはファイルのパスを入力する

3. 出力先のディレクトリを選択する。(なにも指定しない場合、実行ディレクトリ直下に`result`フォルダが生成される)

4. `実行`ボタン押下で解析が実行される。

5. ターミナル上にlogが表示される。


### コマンドラインでの実行
1. 起動コマンド
```
bs_seq_CUI.py
```

2. コマンドラインの表示に従い、Batch.tomlファイル、fastqファイル、結果出力先ディレクトリのパスをそれぞれ入力する。(結果出力先フォルダは何も入力しない場合は実行ディレクトリ直下に`result`ディレクトリが作成される)

3. 入力後`Enter`キーで解析が実行

4. ターミナル上にlogが表示される。


## result
- それぞれの標的geneごとにtsvファイルで結果が出力される
     ```
        chx:メチル化の種類(mCG,mCHG,mCHH)
        pos:シーケンスデータのFW側からのメチル化の位置
        met_rate:C / C + T 
        C:標的メチル化サイトのCの数
        T:標的メチル化サイトのTの数
        ERR:標的メチル化サイトAかGの数
    ```
- `results.json`にカウントデータが保存される
- `log.txt`に解析のログが保存される