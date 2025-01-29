import random

class GeneticAlgorithmTSP:
    def __init__(self, pop_size, generations, cities, mutation_rate=0.1):
        """ 初期化
            @oaram pop_size 個体群のサイズ
            @param generations 世代数
            @param cities  サポート点数
            @param mutation_rate 突然変異率
        """
        self.pop_size = pop_size
        self.generations = generations
        self.cities = cities
        self.gene_length = len(cities)
        self.mutation_rate = mutation_rate
        self.population = self.generate_initial_population()
    
    def generate_initial_population(self):
        """ 初期個体を生成する
            @param int gene_length 遺伝子内の数(サポート点数)
            @param int pop_size 個体数
            @return array 個体数分の遺伝子を作成
        """
        return [random.sample(range(self.gene_length), self.gene_length) for _ in range(self.pop_size)]
    
    def calculate_total_distance(self, gene):
        """ 遺伝子の適応度評価関数 
            例)総経路長、総関節角度変化量等
            
            @param array gene generate_initial_population()で生成したリストから1つずつ遺伝子を取り出したもの
            @return float total_distance 評価関数の長さ ([mm], [rad]等)
        """
        total_distance = 0
        for i in range(len(gene) - 1):
            x1, y1, z1 = self.cities[gene[i]]
            x2, y2, z2 = self.cities[gene[i + 1]]
            total_distance += ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** 0.5
        return total_distance
    
    def crossover(self, parent1, parent2):
        """ 遺伝子の交叉を処理する
            @param array parent1 1次元配列の遺伝子
            @param array parent2 1次元配列の遺伝子
            @return array child1  1次元配列の遺伝子
            @return array child2  1次元配列の遺伝子
        """
        
        crossover_point = random.randint(1, self.gene_length - 1)
        child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
        child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
        return child1, child2
    
    def mutate(self, gene):
        """ 突然変異を処理する
            1次元配列の遺伝子の中身を変える
            
            @param array gene 1次元配列の遺伝子
            @return array gene 1次元配列の遺伝子
        """
        if random.random() < self.mutation_rate:
            idx1, idx2 = random.sample(range(self.gene_length), 2)
            gene[idx1], gene[idx2] = gene[idx2], gene[idx1]
        return gene
    
    def run(self):
        """ 遺伝的アルゴリズムを実行する

            @return array best_gene 1次元配列の遺伝子 (研削順序等)
            @return float best_distance 評価項目の長さ ([mm], [deg]等)
        """
        for _ in range(self.generations):
            evaluated_population = [(gene, self.calculate_total_distance(gene)) for gene in self.population]
            evaluated_population.sort(key=lambda x: x[1])
            selected_parents = [gene for gene, _ in evaluated_population[:self.pop_size // 2]]
            
            new_population = selected_parents[:]
            while len(new_population) < self.pop_size:
                parent1, parent2 = random.sample(selected_parents, 2)
                child1, child2 = self.crossover(parent1, parent2)
                new_population.extend([self.mutate(child1), self.mutate(child2)])
            
            self.population = new_population[:self.pop_size]
        
        best_gene, best_distance = min(
            [(gene, self.calculate_total_distance(gene)) for gene in self.population],
            key=lambda x: x[1]
        )
        return best_gene, best_distance
