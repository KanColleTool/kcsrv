# This is our custom levels list.
# It defines the exp values for levels to use.
# To get the amount of exp required for a level, use sum(levels[:level+1]) as defined in get_exp_required
levels = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900,
          2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700,
          3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5200, 5400, 5600, 5800, 6000,
          6200, 6400, 6600, 6800, 7000, 7200, 7600, 8000, 8400, 8800, 9200, 9600, 10000, 10400, 10800, 11200, 11600,
          12000, 12400, 12800, 13200, 13600, 14000, 14400, 14800, 15200, 15600, 16000, 16400, 16800, 17200, 17600,
          18000, 18400, 18800, 19200, 19600, 20000, 20400, 20800, 21200, 21600, 22000, 22400, 134300]

def get_exp_required(level, current_exp):
    """
    Gets the exp required for the next level.
    :param level: The level to attain.
    :param current_exp: Your current exp.
    """
    total = sum(levels[:level+1])
    return total - current_exp
