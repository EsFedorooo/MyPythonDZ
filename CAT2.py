class Cat:

    def __init__(self):
        self._energy: float = 0
        self._age: int = 0
        self._active: bool = True
        self._life: int = 3
        self._check()

    def _check(self):
        if (self._energy > self.__class__._max_energy() or self._age > self._max_age()
                or self._energy < self._min_energy()):
            self._life -= 1
            self._age = 0
            self._energy = 0
            self._astral()
            print(str(self.life) + ' left')

        return self

    def _astral(self):
        if self._life < self.__class__._min_life():
            self._deactivate()
        return self

    def _deactivate(self):
        self._active = False

    # def get_energy(self):
    #     return self._energy
    #
    # def get_age(self):
    #     return self._age

    @property
    def energy(self):
        return self._energy

    @property
    def energy_in_watt(self):
        return self.energy * 1000

    @property
    def age(self):
        return self._age

    @property
    def life(self):
        return self._life

    # It is possible to use property here, but unnecessary
    def __bool__(self):
        return self._active

    @staticmethod
    def _max_energy():
        return 100

    @staticmethod
    def _min_energy():
        return 0

    @staticmethod
    def _max_age():
        return 2

    @staticmethod
    def _min_life():
        return 1

    def sleep(self):
        if not self:
            return False
        if self.energy > self._max_energy() * 0.9:
            return False
        self._age_inc()
        self._change_energy(self._energy_sleep_inc())
        print('Котик спить')
        self._check()
        return True

    def _energy_sleep_inc(self):
        return (self.__class__._max_energy() - self.energy) * 0.5

    def _age_inc(self):
        self._age += 1

    def run(self):
        if not self:
            return False
        if (self.energy < self._max_energy() * 0.2 or
                self.age > self._max_age() * 0.8):
            return True
        self._change_energy(-self._energy_run_loss())
        print('Котик біжить')
        self._check()
        return True

    def _change_energy(self, amount: float):
        self._energy += amount

    def _energy_run_loss(self):
        return self.energy * 0.1 + 10

    def eat(self, food: float):
        if not self or food <= 0:
            return False
        if self.energy > self.__class__._max_energy * 0.9:
            return False
        print('Котик їсть')
        self._age_inc()
        self._change_energy(self._energy_eat_inc())

    def _energy_eat_inc(self):
        return (self.__class__._max_energy - self.energy) * 0.4


tom = Cat()

tom.sleep()
print(tom.energy, ';', tom.age, ';', tom.life)

tom.sleep()
print(tom.energy, ';', tom.age, ';', tom.life)

tom.sleep()
print(tom.energy, ';', tom.age, ';', tom.life)

tom.sleep()
print(tom.energy, ';', tom.age, ';', tom.life)

tom.sleep()
print(tom.energy, ';', tom.age, ';', tom.life)

tom.sleep()
print(tom.energy, ';', tom.age, ';', tom.life)

tom.sleep()
print(tom.energy, ';', tom.age, ';', tom.life)

tom.sleep()
print(tom.energy, ';', tom.age, ';', tom.life)

tom.sleep()
print(tom.energy, ';', tom.age, ';', tom.life)

tom.sleep()
print(tom.energy, ';', tom.age, ';', tom.life)

print(tom.energy, ';', tom.age, ';', tom.life, ';', tom.__bool__())

if not tom.__bool__():
    del tom
else:
    pass

