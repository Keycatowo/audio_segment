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
# %%

# %%
def split_autio(row):
    filepath = row["file_name"]
    filename = Path(filepath).name.split(".")[0]
    audio, sr = librosa.load(filepath)
    for index, label in enumerate(row["label_list"]):
        start = int(label["start"] * sr)
        end = int(label["end"] * sr)
        output = audio[start:end]
        Path(f"output/{filename}").mkdir(exist_ok=True)
        sf.write(f"output/{filename}/{index}.wav", output, sr)
# %%
if __name__ == "__main__":
    # load label
    df = pd.read_csv("label_data.csv")

    # Preprocess of column
    df["file_name"] = df["audio"].apply(unquote).apply(lambda x: f"data/{x[25:]}")
    df["label_list"] = df["label"].apply(json.loads)


    df.apply(split_autio, axis=1)
# %%
