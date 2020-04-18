class WaterPump:

    power_consumption = 0
    producer = 'producer'
    volume_of_water_per_hour = 0

    price_in_uah = 0
    efficiency = 0
    pump_pressure = 0

    pump_id = 10

    def __init__(self, power_consumption=100, producer='Vasya', volume_of_water_per_hour=10000, price_in_uah=1000,
                 efficiency=10, pump_pressure=100):
        self.power_consumption = power_consumption
        self.producer = producer
        self.volume_of_water_per_hour = volume_of_water_per_hour
        self.price_in_uah = price_in_uah
        self.efficiency = efficiency
        self.pump_pressure = pump_pressure

    @staticmethod
    def get_pump_id():
        return WaterPump.pump_id

    def __str__(self):
        return "Power consumption: {}; Producer: {}; Volume of water pumped per hour: {}; Price in uah: {}; " \
               "Efficiency in %: {}; Pump pressure: {}." \
            .format(self.power_consumption, self.producer, self.volume_of_water_per_hour, self.price_in_uah,
                    self.efficiency, self.pump_pressure)

    def __del__(self):
        pass