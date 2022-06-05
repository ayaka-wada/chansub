import pandas as pd
import numpy as np
import sys
from time import sleep
import matplotlib.pyplot as plt
import subprocess as sp
from sklearn.metrics import r2_score as r2
import matplotlib.patches as mpatches

sp.call("wget https://github.com/ayaka-wada/chansub/blob/main/src/Number_of_channel_subscribers.csv",shell=True)
# sp.call("cat Number_of_channel_subscribers.csv|sed '2,$s/,-/,/g' >new",shell=True)
# sp.call("mv new Number_of_channel_subscribers.csv",shell=True)
# data=pd.read_csv("Number_of_channel_subscribers.csv")
# data.fillna(0,inplace=True)
# sp.call("rm Number_of_channel_subscribers.csv",shell=True)

def main():
    csv = pd.read_csv('Number_of_channel_subscribers.csv', parse_dates=['date'], index_col='date')
    # NaN値の補完
    df = csv.interpolate(limit_direction='both')
    fig, ax = plt.subplots()

    ax.plot(df.index, df['Tokino Sora'], label="Tokino Sora")
    ax.plot(df.index, df['Houshyou Marine'], label="Houshyou Marine")
    ax.plot(df.index, df['Shiranui Flare'], label="Shiranui Flare")
    ax.plot(df.index, df['Usada Pekora'], label="Usada Pekora")
    ax.plot(df.index, df['Shirogane Noel'], label="Shirogane Noel")
    ax.plot(df.index, df['Kiryu Coco'], label="Kiryu Coco")


    # ラベルの名前付け
    ax.set_xlabel('Date')
    ax.set_ylabel('channel subscribers')
    # y軸の範囲設定
    ax.set_ylim(0,2300000)
    # 指数表記から普通の表記に変換
    plt.ticklabel_format(style='plain',axis='y')
    # 凡例
    plt.legend(loc="upper left", fontsize=10)
    # x軸の文字を回転
    plt.xticks(rotation=60)
    plt.show()
    plt.savefig('../img.png')

if __name__ == '__main__':
    main()
