import numpy as np, pandas as pd, matplotlib as plt

def main():
    cpi_data = pd.read_csv(
        '/Users/oleg/Documents/uni/2-sem/ML/assign/data/A1_Descriptive_Analysis/new_CPI/cpi-2020.csv', sep=";")
    cpi_data.rename(columns={"CPI score 2020": "cpi"})
    print()
if __name__ == '__main__':
    main()