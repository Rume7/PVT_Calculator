
class PVTCalculator():

    def __init__(self, name, brief, fluid_type, unit):
        this.name = name
        this.brief = brief
        this.fluid_type = fluid_type
        this.unit = unit

    def get_Rsb(self):
        return rsb;

    def set_Rsb(self, rsb):
        this.rsb = rsb;

    def get_sg_oil(self):
        return sg_oil;

    def set_sg_oil(self, sg_oil):
        self.sg_oil = sg_oil;

    def get_sg_gas(self):
        return self.sg_gas;

    def set_sg_gas(self, sg_gas):
        self.sg_gas = sg_gas;

    def get_sg_water(self):
        return self.sg_water;

    def set_sg_water(self, sg_water):
        self.sg_water = sg_water;

    def get_reservoir_pressure(self):
        return self.reservoir_pressure

    def set_reservoir_pressure(self, press):
        self.reservoir_pressure = press;

    def get_reservoir_temp(self):
        return self.reservoir_temperature

    def set_reservoir_temp(self, temp):
        self.reservoir_temperature = temp;