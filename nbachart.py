from nba_api.stats.endpoints import shotchartdetail
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_rows', None)
player=shotchartdetail.ShotChartDetail(player_id='1628366', team_id='1610612740')
table=player.get_data_frames()
#headers = table['resultSets'][0]['headers']
#shots = table['resultSets'][0]['rowSet']
#df = pd.DataFrame(shots, columns=headers)
print(df.LOC_X)
#sns.set_style("white")
#sns.set_color_codes()
#plt.figure(figsize=(12,11))
#plt.scatter(table.LOC_X, table.LOC_Y)
#plt.show()
