import pandas as pd
from pathlib import Path

def write_report(rows,outfile):
    Path(outfile).parent.mkdir(parents=True,exist_ok=True)
    pd.DataFrame(rows).to_csv(outfile,index=False)
