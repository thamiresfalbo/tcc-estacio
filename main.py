import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

def main():
    excelsheet = "source/criptoativos_dados_abertos_02032023.xls"
    df = pd.DataFrame(pd.read_excel(excelsheet,sheet_name=1, skiprows=11))
    print(df.round(1).head(5))

main()