import pandas as pd
import PTwithTimeTrend_AllStock as ptm

def test_python():
    file = pd.read_csv("check_data.csv",index_col= 0)
    file = file.to_numpy()
    table = ptm.refactor_formation_table(file)
    print(table)

if __name__ == "__main__":
    test_python()    