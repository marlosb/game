from typing import TypedDict

class EnemyProperties(TypedDict):
    max_life : int
    speed : int
    size : int
    color: str

class EnemyLevels(TypedDict):
    properties : EnemyProperties

enemy_level_1: EnemyProperties = {'max_life': 80, 'speed': 100, 'size': 15, 'color': 'red'}
enemy_level_2: EnemyProperties = {'max_life': 120, 'speed': 140, 'size': 15, 'color': 'red3'}
enemy_level_3: EnemyProperties = {'max_life': 180, 'speed': 180, 'size': 15, 'color': 'red4'}
enemy_level_4: EnemyProperties = {'max_life': 200, 'speed': 200, 'size': 15, 'color': 'brown4'}

enemies_properties : EnemyLevels = {1: enemy_level_1,
                                    2: enemy_level_1,
                                    3: enemy_level_2,
                                    4: enemy_level_2,
                                    5: enemy_level_3,
                                    6: enemy_level_3,
                                    7: enemy_level_4,
                                    8: enemy_level_4,
                                    9: enemy_level_4}

class StructureProperties(TypedDict):
    rate_of_fire : int
    damage : int
    range : int
    colot: str

class StructureLevels(TypedDict):
    properties : StructureProperties

structure_level_1: StructureProperties = {'rate_of_fire': 2, 'damage': 20, 'range': 100, 'color': 'deepskyblue'}
structure_level_2: StructureProperties = {'rate_of_fire': 3, 'damage': 25, 'range': 130, 'color': 'blue'}
structure_level_3: StructureProperties = {'rate_of_fire': 4, 'damage': 25, 'range': 160, 'color': 'blue4'}

structure_properties : EnemyLevels = {1: structure_level_1,
                                    2: structure_level_1,
                                    3: structure_level_2,
                                    4: structure_level_2,
                                    5: structure_level_2,
                                    6: structure_level_2,
                                    7: structure_level_3,
                                    8: structure_level_3,
                                    9: structure_level_3}