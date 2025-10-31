# met-PCR-2

## Setup
1. Install Python (verified to work with version 3.11.1).
2. Create a designated working directory.
3. Install met-PCR2 along with the necessary libraries.

```
git clone https://github.com/NishimuraLAB-GIT/met-PCR2

pip install -r requirements.txt
```


## Analysis
- Requirements
    - FASTQ sequence file
    - Batch.toml configuration file
        - A template is included in the main directory created during installation. Use this as a reference.
        - Remove any unnecessary [[entry]] blocks, as they may cause errors during execution.

## Running via GUI
1.	Launch Command
```
python bs_seq.py
```

2.	Select Input Files
In the displayed window, select the prepared `Batch.toml` file and `FASTQ` file, or manually enter their file paths.
3.	Specify Output Directory
Choose the directory where the analysis results should be saved.
If no directory is specified, a `result` folder will be automatically created in the current working directory.
4.	Execute Analysis
Click the `Run` button to start the analysis.
5.	View Logs
Logs will be displayed in the terminal during execution.
________________________________________
## Running via Command-Line Interface (CLI)
1.	Launch Command
```
bs_seq_CUI.py
```
2.	Provide Required Paths
Follow the prompts in the terminal to input the paths for the following:
    - `Batch.toml` file
    - `FASTQ` file
    - Output directory for results
If the output directory is left blank, a result folder will be created in the current working directory.
3.	Start Analysis
Press the `Enter` key after entering the required paths to begin the analysis.
4.	View Logs
Logs will be displayed in the terminal during execution.

## Results
- Results are output as TSV files for each target gene, containing the following columns:
    - chx: Type of methylation (mCpG, mCpHpG, mCpHpH)
    - pos: Position of the methylation from the forward (FW) end of the sequence data
    - met_rate: Methylation rate calculated as C / (C + T)
    - C: Number of cytosines at the target methylation sites
    - T: Number of thymines at the target methylation sites
    - ERR: Number of adenines or guanines at the target methylation sites
- Raw analysis data is saved in `results.json`.
- Analysis logs are saved in `log.txt`.


