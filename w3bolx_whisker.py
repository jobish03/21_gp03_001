import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size=10000)
gama_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal': normal_sample,
                   'random': random_sample,
                   'gamma': gama_sample})

print(df.describe())
# print(normal_sample.min())
plt.figure()
_ = plt.boxplot(df['normal'], whis=(0, 100))

plt.clf()
plt.boxplot([df['normal'], df['random'], df['gamma']], whis=(0, 100))

plt.clf()
plt.hist(df['gamma'], bins=100)

import mpl_toolkits.axes_grid1.inset_locator as mpl_il

plt.figure()
plt.boxplot([df['normal'], df['random'], df['gamma']],
            whis=(0, 100))
ax2 = mpl_il.inset_axes(plt.gca(), width='60%', height='40%', loc=2)
ax2.hist(df['gamma'], bins=100)
ax2.margins(x=0.5)
ax2.yaxis.tick_right()
plt.show()

plt.figure()
X = np.random.random(size=10000)
Y = np.random.normal(loc=0.0, scale=0.5, size=10000)
print(X, Y)
_ = plt.hist2d(X,Y, bins = 25)
_x = plt.hist2d(X,Y, bins = 125)
plt.colorbar()
plt.show()

