
#this file will contains user's classed and methods

class UserLevel:
    def __init__(self) -> None:
        self.levels_and_exp = {1: 1, 2: 2}
        self.build_levels_and_exp()
        
    def build_levels_and_exp(self):
        #fibonacci to lvl 9, then slow down
        for i in range(3, 51):
            if i < 10:
                self.levels_and_exp[i] = self.levels_and_exp[i-1] + self.levels_and_exp[i-2]
            else:
                self.levels_and_exp[i] = int(self.levels_and_exp[i-1] * 0.5 + self.levels_and_exp[i-2])

        #print(self.levels_and_exp)
    
    # define a function to get the experience points required to reach the next level
    def exp_to_next_level(self, exp):
        for level, threshold in self.levels_and_exp.items():
            if exp < threshold:
                return threshold - exp
        return 0

if __name__ == '__main__':
    test = UserLevel()
    test.build_levels_and_exp()
    print(test.exp_to_next_level(123))