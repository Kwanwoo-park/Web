from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df_exchange = pd.read_csv('DEXKOUS.csv', header=1,
                              names=['DATE', 'DEXKOUS'], skipinitialspace=True, index_col=0)
    years = {}
    output = []

    for index in df_exchange.index:
        year = int(index.split('-')[0])
        if (year not in years) and (1981 < year < 2014):
            if df_exchange.DEXKOUS[index] != '.':
                years[year] = True
                output.append([year, float(df_exchange.DEXKOUS[index])])

    df_exchange = pd.DataFrame(output)

    df_jobs = pd.read_excel('gugik.xlsx')
    output = []
    stacked = df_jobs.stack()[7]
    for index in stacked.index:
        try:
            if 1981 <= int(index) <= 2014:
                output.append([int(index), float(stacked[index])])
        except:
            pass

    df_jobs = pd.DataFrame(output)

    plt.subplot(2, 1, 1)
    plt.plot(df_exchange[0], df_exchange[1], label='won/dollar')
    plt.xlim(1981, 2014)
    plt.ylim(500, 2500)
    plt.legend(loc='best')

    plt.subplot(2, 1, 2)
    plt.plot(df_jobs[0], df_jobs[1], label='hire percentage(%)')
    plt.xlim(1981, 2014)
    plt.ylim(0, 100)
    plt.legend(loc='best')
    plt.savefig('historical_data.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    main()