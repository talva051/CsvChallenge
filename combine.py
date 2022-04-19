import pandas as pd
import glob
import os

globbed_files = glob.glob("*.csv")

data = []
for csv in globbed_files:
    frame = pd.read_csv(csv)
    frame['filename'] = os.path.basename(csv)
    data.append(frame)

bigframe = pd.concat(data, ignore_index=True)
bigframe.to_csv("withFileName.csv", columns = ['email_hash', 'category', 'filename'] ,index = False)
