from helper.helper import *
from algorithm.Swarm import moving_swarm

def search_global_solution(swarm: Swarm, func: Func)->np.ndarray: # функция поиска глобального решения
    
    swarm.global_solution = swarm[0].x
    
    for particle in swarm:
        solution = func.value(particle.x)
        if solution - func.value(swarm.global_solution) < 0:
            swarm.global_solution = particle.x
    return swarm.global_solution
            

def chanding_vector(swarm: Swarm, ROI_SIZE)->Swarm: # расчет вектора скорости кажной частицы роя
    for i in range(ROI_SIZE):
        swarm[i].update_v(swarm.global_solution)
        
    return swarm
    

def algorithm(const: Constants, add_in_moving: bool = False)->Constants: # главная функция 
    
    const.swarm.global_solution = search_global_solution(const.swarm, const.FUNC) # расчет глобального значения для начальногго роя
    const.add_in_moving()
    N = 0
    while N < const.ITERATION:
        
        add_image(N, const.swarm)
        N += 1
        
        const.swarm = chanding_vector(const.swarm, const.ROI_SIZE)# расчет векторов скорости
        
        if add_in_moving:
            const.swarm = moving_swarm(const.swarm, const.ROI_SIZE, const.FUNC) # расчет новых координат точек
            const.add_in_moving()
            
        const.swarm.global_solution = search_global_solution(const.swarm, const.FUNC) # расчет глобального решения
    
    const.BEST_COORDINATE = const.swarm.global_solution # сохранение параметров последеного положения роя
    const.BEST_SOLUTION = const.FUNC.value(const.swarm.global_solution)
    
    return const