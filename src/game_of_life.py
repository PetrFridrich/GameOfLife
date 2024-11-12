import numpy as np


class GameOfLife():

    def __init__(self, resolution):

        self.width = resolution[1]
        self.height = resolution[0]
        
        self.generation = None
        
        pass


    def init_life(self, probability=0.25):

        self.generation = (np.random.rand(self.height, self.width) < probability).astype(int)

        return None


    def next_generation(self):

        if self.generation is None:
            raise Exception('need to call init_life()')

        next_generation = np.zeros_like(self.generation)

        for i in range(self.height):
            for j in range(self.width):
                
                local_area = self.generation.take(range(i - 1, i + 2), axis=0, mode='wrap').take(range(j - 1, j + 2), axis=1, mode='wrap')

                next_generation[i,j] = self.rule_B3_S23(local_area)

        self.generation = next_generation.copy()

        return None


    def rule_B3_S23(self, local_area):

        population = np.sum(local_area)

        underpopulation = 1
        overpopulation = 4
        birth = 3

        # Alive
        if local_area[1,1] == 1:
            # Survive ?
            if underpopulation < population - 1 < overpopulation:
                return 1
            else:
                return 0
        # Dead
        else:
            # Born ? 
            if population == birth:
                return 1
            return 0


if __name__ == '__main__':
    
    print('Hello, home!')