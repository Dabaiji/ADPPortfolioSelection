from matplotlib import pyplot as plt

from adp.plot.slopes import FirstSlopeAx
from adp.plot.test import GrossTestPlotter
from adp.plot.value_function import PWLValueFunctionPlotter
from adp.plot.wealth import FinalReturnPlotter
from adp.pwladp.trainer import ADPStrategyTrainer
from adp.strategy import ADPStrategy
from adp.value_function import PWLDynamicFunction
from parameters import S, repeat

# Value Function
strategy = ADPStrategy(value_function_class=PWLDynamicFunction)

# Process trainer
trainer = ADPStrategyTrainer(strategy)

# Plotters
plt.ion()
plotters = [PWLValueFunctionPlotter(i, strategy) for i in []] \
           + [FinalReturnPlotter(trainer, lengths=(10, 50)),
              # FinalPositionsPlotter(trainer),
              # SlopesNumberPlotter(V),
              # MeanSlopesPlotter(V),
              # MeanBreaksPlotter(V)
              GrossTestPlotter(trainer)
              ]

firstSlopeAx = FirstSlopeAx(strategy)

for s in range(S):
    print(s)
    next(trainer)
    if s % repeat == 1:
        for plotter in plotters:
            plotter.draw()
        plt.pause(0.001)
        firstSlopeAx.plot()

plt.ioff()