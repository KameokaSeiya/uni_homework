import sys

import matplotlib.pyplot as plt
import pandas as pd

sys.path.append('C:\\Users\\81807\\OneDrive - 埼玉大学\\埼玉大学講義\\修士\\生産工学特論\\第13回課題')
import geneticAlgorithmTSP as geneticAlgorithm

# citiesの読み込み
cities_csv = pd.read_csv('./example.csv')
cities_df = cities_csv.iloc[:, :3]
print(cities_df)
cities = cities_df.values.tolist()
print(cities)

# パラメータ設定
pop_size = 20   # 個体群のサイズ
generations = 100  # 世代数
mutation_rate = 0.1  # 突然変異率

# 遺伝的アルゴリズムのインスタンスを作成
ga_tsp = geneticAlgorithm.GeneticAlgorithmTSP(pop_size, generations, cities, mutation_rate)

# アルゴリズムを実行
best_gene, best_distance = ga_tsp.run()


def plot_best_route(best_gene, cities):
    x = [cities[i][0] for i in best_gene]
    y = [cities[i][1] for i in best_gene]
    z = [cities[i][2] for i in best_gene]
    #x.append(x[0])  # 最初の都市へ戻る
    #y.append(y[0])
    
    fig=plt.figure(figsize=(8,6))
    ax=fig.add_subplot(111,projection='3d')
    ax.plot(x,y,z,marker='o')

    for i, city in enumerate(cities):
        ax.text(city[0], city[1], city[2], str(i), fontsize=12, ha='center', va='center')

    ax.set_title("Best Route")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_zlabel("Z Coordinate")
    plt.grid()
    plt.show()
    
def plot_cities(gene, cities):
    x = [cities[i][0] for i in gene]
    y = [cities[i][1] for i in gene]
    z = [cities[i][2] for i in gene]
    #x.append(x[0])  # 最初の都市へ戻る
    #y.append(y[0])
    
    fig=plt.figure(figsize=(8,6))
    ax=fig.add_subplot(111,projection='3d')
    ax.scatter(x,y,z)

    for i, city in enumerate(cities):
        ax.text(city[0], city[1], city[2], str(i), fontsize=12, ha='center', va='center')

    ax.set_title("Cities")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_zlabel("Z Coordinate")
    plt.grid()
    plt.show()
#
# 結果の出力
print("最適な経路:", best_gene)
print("最短距離:", best_distance)
plot_cities(best_gene, cities)
plot_best_route(best_gene, cities)