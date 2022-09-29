"""
    讀取label studio標記好的檔案
"""

#%%
import pandas as pd
import librosa
import soundfile as sf
import json
from pathlib import Path
from urllib.parse import unquote
from rich.console import Console
console = Console()
# %%
# add arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, default="export_data.csv", help="input labeded file path")
# parser.add_argument("-o","--output", type=str, default="output/", help="output file path")



# %%
def split_autio(row):
    # read audio
    filepath = row["file_name"]
    filename = Path(filepath).name.split(".")[0]
    audio, sr = librosa.load(filepath)
    print(f"Load audio file [{filepath}], sample rate: {sr}, duration: {len(audio)/sr:.2f} sec")
    
    Path(f"output/{filename}").mkdir(exist_ok=True) # 建立音檔資料夾
    # split audio
    label_count = {}
    for index, label_dict in enumerate(row["label_list"]):

        start = int(label_dict["start"] * sr) # 開始的時間點
        end = int(label_dict["end"] * sr) # 結束的時間點
        label = label_dict["labels"][0] # 標記的類別
        output = audio[start:end] # 切割音檔

        # 計算不同類別的數量
        
        if label in label_count:
            label_count[label] += 1
        else:
            Path(f"output/{filename}/{label}").mkdir(exist_ok=True) # 建立類別資料夾
            label_count[label] = 1
        
        # 輸出音檔
        
        sf.write(f"output/{filename}/{label}/{label_count[label]}.wav", output, sr)
    print(f"Total label counts: {label_count}")
# %%
if __name__ == "__main__":
    # get arguments
    args = vars(parser.parse_args())
    print(f"Labeled fiel: {args['input']}")

    # load label
    df = pd.read_csv(args["input"])
    print(f"load {len(df)} data")

    ## Preprocess of column
    df["file_name"] = df["audio"].apply(unquote).apply(lambda x: x.split("/")[-1][9:]).apply(lambda x: f"data/{x}") # Convert file name and path
    df["label_list"] = df["label"].apply(json.loads) # Convert json to dict



    # df.apply(split_autio, axis=1)
# %%
