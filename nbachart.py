from nba_api.stats.endpoints import shotchartdetail
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from court import draw_court

pd.set_option('display.max_rows', None)
player=shotchartdetail.ShotChartDetail(player_id='1628366', team_id='1610612740')
table=player.get_data_frames()[0]
#print(table.LOC_X)

sns.set_style("white")
sns.set_color_codes()
# plt.figure(figsize=(12,11))
# draw_court(outer_lines=True)
# plt.scatter(table.LOC_X, table.LOC_Y,s=10)
# plt.xlim(300,-300)
# plt.ylim(-100,500)
# plt.show()

cmap=plt.cm.gist_heat_r
joint_chart=sns.jointplot(table.LOC_X,table.LOC_Y,stat_func=None,kind='hex',space=0,color=cmap(0.2),cmap=cmap)
joint_chart.fig.set_size_inches(12,11)
axis=joint_chart.ax_joint
draw_court(axis)
axis.set_xlim(250,-250)
axis.set_ylim(422.5,-47.5)
axis.set_xlabel('')
axis.set_ylabel('')
axis.tick_params(labelbottom='off',labelleft='off')
plt.savefig("nbaapp\static/shot_chart.png")