from model.WaterPump import *


def main():
    first_water_pump = WaterPump()
    second_water_pump = WaterPump(200, 'Kolya', 20000)
    third_water_pump = WaterPump(300, 'Petya', 30000, 2000, 20, 200)

    print(first_water_pump.__str__())
    print(second_water_pump.__str__())
    print(third_water_pump.__str__())

    print('Static field: Pump ID: {}'.format(WaterPump.get_pump_id()))


if __name__ == '__main__':
    main()