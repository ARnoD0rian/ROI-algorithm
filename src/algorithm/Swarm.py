from algorithm.Particle import Particle

class Swarm(list): # класс роя
    def __init__(self, *args):
        super().__init__(*args)
        self.global_solution = 0
        
def create_swarm(min_coor, max_coor, max_speed, inertion, f_p, f_g, k, x, roi_size): # инициализация начального роя
    return Swarm([Particle(min_coor, max_coor, max_speed, inertion, f_p, f_g, k, x) for _ in range(roi_size)])

def moving_swarm(swarm: Swarm, ROI_SIZE, func)->Swarm: # расчет новых координат точек роя
    for i in range(ROI_SIZE):
        swarm[i].update_x()
        swarm[i].update_local_solution(func)

    return swarm