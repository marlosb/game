from typing import TypedDict

class EnemyProperties(TypedDict):
    max_life : int
    speed : int
    size : int
    color: str

class EnemyLevels(TypedDict):
    properties : EnemyProperties

levels_1_to_2: EnemyProperties = {'max_life': 80, 'speed': 100, 'size': 15, 'color': 'red'}
levels_3_to_5: EnemyProperties = {'max_life': 120, 'speed': 140, 'size': 15, 'color': 'red3'}
levels_6_to_9: EnemyProperties = {'max_life': 180, 'speed': 180, 'size': 15, 'color': 'red4'}

enemies_properties : EnemyLevels = {1: levels_1_to_2,
                                    2: levels_1_to_2,
                                    3: levels_3_to_5,
                                    4: levels_3_to_5,
                                    5: levels_3_to_5,
                                    6: levels_6_to_9,
                                    7: levels_6_to_9,
                                    8: levels_6_to_9,
                                    9: levels_6_to_9}