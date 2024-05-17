
from numpy import random, mean


params = {'world_size':(10,10),
          'num_agents':260,
          'same_pref' :0.4,
          'max_iter'  :100,
          'out_path'  :r'/Users/kongzidan/Documents/GitHub/lab9'}

class Agent():
    def __init__(self, world, kind, same_pref):
        self.world = world
        self.kind = kind
        self.same_pref = same_pref
        self.location = None

    def move(self):
        happy = self.am_i_happy()

        if not happy:
            vacancies = self.world.find_vacant(return_all=True)
            for patch in vacancies:
                i_moved = False
                will_i_like_it = self.am_i_happy(loc=patch)
                if will_i_like_it is True:
                    self.world.grid[self.location] = None 
                    self.location = patch                
                    self.world.grid[patch] = self         
                    i_moved = True
                    return 1
            if i_moved is False:
                return 2
        else:
            return 0

    def am_i_happy(self, loc=False, neighbor_check=False):

        if not loc:
            starting_loc = self.location
        else:
            starting_loc = loc

        neighbor_patches = self.locate_neighbors(starting_loc)
        neighbor_agents  = [self.world.grid[patch] for patch in neighbor_patches]
        neighbor_kinds   = [agent.kind for agent in neighbor_agents if agent is not None]
        num_like_me      = sum([kind == self.kind for kind in neighbor_kinds])

        if neighbor_check:
            return [kind == self.kind for kind in neighbor_kinds]

        if len(neighbor_kinds) == 0:
            return False

        perc_like_me = num_like_me / len(neighbor_kinds)

        if perc_like_me < self.same_pref:
            return False
        else:
            return True

    def locate_neighbors(self, loc):
        pass

class World():
    def __init__(self, params):
       pass

    def build_grid(self, world_size):
        pass
    
    def build_agents(self, num_agents, same_pref):
        pass

        

    def init_world(self):
        pass

    def find_vacant(self, return_all=False):

        pass
    def report_integration(self):
        pass 

    def run(self):
       pass 

    def report(self, to_file=True):
        pass
world = World(params)
world.run()
