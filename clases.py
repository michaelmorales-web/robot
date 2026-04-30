class robot():
    def __init__(self):
        self.__name = ""
        self.__batery = 100

    def get_name(self):
        return self.__name

    def get_batery(self):
        return self.__batery

    def get_shield(self):
        return self.__shield
    
    def set_batery(self, new_batery):
        self.__batery = new_batery  

    def set_shield(self, new_shield):
        self.__shield = new_shield

    def setName(self, new_name):
        self.__name = new_name

class RobotAtaque(robot):
    def __init__(self):
        self.__ataque = 30
    
    def get_ataque(self):
        return self.__ataque

class RobotDefesa(robot):
    def __init__(self):
        self.__shield = 60
    
    def get_shield(self):
        return self.__shield
    def set_shield(self, new_shield):
        self.__shield = new_shield