import glob , json
import pandas as pd

files = glob.glob("data//*")
print(files)
df = { "site" : [] , "content" : [] , "json" : []}

for file in files :
    con , jsn = glob.glob(f"{file}/*.*")
    df["site"].append( file.split("/")[-1])
    with open(con , "r" , encoding="utf-8") as f :
        df["content"].append(f.read())
    with open(jsn , "r" , encoding="utf-8") as f :
        d = json.load(f)
        df["json"].append( d )

df = pd.DataFrame( df)
print(df.head())
df.to_csv("data.csv")
    
    