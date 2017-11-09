import pandas as pd
import numpy as np
import csv
from sklearn.cluster import KMeans

shot_df = pd.read_csv('new_shots.csv')

shot_array = np.array([shot_df['shot_0'].tolist(),
                      shot_df['shot_1'].tolist(),
                      shot_df['shot_2'].tolist(),
                      shot_df['shot_3'].tolist(),
                      shot_df['shot_4'].tolist(),
                      shot_df['shot_5'].tolist(),
                      shot_df['shot_6'].tolist(),
                      shot_df['shot_7'].tolist(),
                      shot_df['shot_8'].tolist(),
                      shot_df['shot_9'].tolist(),
                      shot_df['shot_10'].tolist(),
                      shot_df['shot_11'].tolist(),
                      shot_df['shot_12'].tolist(),
                      shot_df['shot_13'].tolist(),
                      shot_df['shot_14'].tolist(),
                      shot_df['shot_15'].tolist(),
                      ])

shot_array = shot_array.T

base = []
pred = KMeans(n_clusters=10).fit_predict(shot_array)

for [pr, pl] in zip(pred, shot_df['player']):
    base.append([pr, pl])

print(base)

base.sort(key=lambda x:(x[0], x[1]))
print(base)

with open('result.csv', 'w') as f:
    writer = csv.writer(f, lineterminator = '\n')
    writer.writerows(base)
