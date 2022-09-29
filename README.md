# Audio Segment

## 目的
+ 為了節省需要重複分割一些音檔輸出的時間
+ 使用工具批量標注之後再批量產生


## 環境安裝

### 下載本份Code
```sh
git clone https://github.com/Keycatowo/audio_segment.git
cd audio_segment
pip install -r requirements.txt # 安裝相關套件
```

### 準備音訊檔案
將要分割的audio檔案批量放置在`data/`下

### 安裝Label Studio
```sh
# Install the package
pip install -U label-studio
```




## 使用說明

### Step1：開啟Label Studio
```sh
label-studio
```
開啟畫面![](/img/%E9%96%8B%E5%A7%8B%E7%95%AB%E9%9D%A2.jpg)

### Step2：建立Project

建立Project ![](/img/%E5%BB%BA%E7%AB%8BProject.jpg)

這邊我們選擇這個模版
![](/img/%E9%81%B8%E6%93%87%E6%A8%A1%E7%89%88.jpg)

並且添加你要標注的類型
![](/img/%E6%B7%BB%E5%8A%A0Label.jpg)

### Step3：開始標注
此時可以快速按鍵盤上的數字鍵切換要標注的類別，用滑鼠框選範圍
有需要的時候可以調整縮放大小來讓標注比較容易
![](/img/%E6%A8%99%E6%B3%A8%E5%AE%8C%E6%88%90.jpg)

### Step4：輸出標注結果
![](/img/%E8%BC%B8%E5%87%BA%E6%A8%99%E6%B3%A8.gif)

此時應該會看到一個名稱類似`project-18-at-2022-09-29-16-10-3d998863.csv`的檔案

開啟會得到如下的內容
![](/img/%E6%A8%99%E6%B3%A8%E6%AA%94%E6%A1%88%E5%85%A7%E5%AE%B9.jpg)

### Step5：分割檔案
```sh
# 這邊-i後面是接你的標注檔案，記得要修改
python main.py -i project-18-at-2022-09-29-16-10-3d998863.csv
```

+ 之後會根據原始音檔的名稱，每個音檔會建立一個資料夾
+ 每個音檔資料夾底下如果有複數類別，會各建立一個資料夾
+ 剩下的標注會按照編號順序從`1.wav`, `2.wav`, ...往下建立



## 相關資料
[Label Studio – Open Source Data Labeling](https://labelstud.io/)