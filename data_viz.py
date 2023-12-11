
# ------------------------------------------------------------------------------
# Neues Skript
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates


file_path_1 = '~/Desktop/data_20231124-115426.csv'
# file_path_2 = '~/Desktop/data_20231124-145308.csv'
# file_path_2 = '~/Desktop/data_20231127-104614.csv'
file_path_2 = '~/Desktop/data_20231127-110020.csv'


save_path = 'plot_image.png'

start = 1740
finish = 1960
offset = 315 # Offset to align the two plots using the x position as reference

x_axis = range(start, finish)


locator = mdates.MinuteLocator()

# Load data
df_1 = pd.read_csv(file_path_1, parse_dates=['Timestamp'])
df_2 = pd.read_csv(file_path_2, parse_dates=['Timestamp'])

# Load df from 50 to avoid outliers and achieve better visualization
df_1 = df_1[start:finish]
df_2 = df_2[start-offset:finish-offset]


fig, axs = plt.subplots(5, 1, figsize=(15, 25))



# Plot the position in the first subplot
axs[0].plot(x_axis, df_1['ActPosX'], label='ActPosX_1', color='purple')
axs[0].plot(x_axis, df_1['ActPosY'], label='ActPosY_1', color='brown')
axs[0].plot(x_axis, df_1['ActPosZ'], label='ActPosZ_1', color='black')
axs[0].plot(x_axis, df_2['ActPosX'], label='ActPosX_2', color='red', linestyle='dashed')
axs[0].plot(x_axis, df_2['ActPosY'], label='ActPosY_2', color='green', linestyle='dashed')
axs[0].plot(x_axis, df_2['ActPosZ'], label='ActPosZ_2', color='blue', linestyle='dashed')
axs[0].set_title('Actual Position Over Time')
axs[0].legend()


# Plot the speed in the second subplot
axs[1].plot(x_axis, df_1['ActSpeedX'], label='ActSpeedX_1', color='purple')
axs[1].plot(x_axis, df_1['ActSpeedY']/20, label='ActSpeedY_1', color='brown')
axs[1].plot(x_axis, df_1['ActSpeedZ'], label='ActSpeedZ_1', color='black')

axs[1].plot(x_axis, df_2['ActSpeedX'], label='ActSpeedX_2', color='red', linestyle='dashed')
axs[1].plot(x_axis, df_2['ActSpeedY']/20, label='ActSpeedY_2', color='green', linestyle='dashed')
axs[1].plot(x_axis, df_2['ActSpeedZ'], label='ActSpeedZ_2', color='blue', linestyle='dashed')
axs[1].set_title('Actual Speed Over Time (Y values divided by 20 for better visualization)')
axs[1].legend()


# Plot the current in the third subplot
axs[2].plot(x_axis, df_1['ActCurrentX'], label='ActCurrentX_1', color='purple')
axs[2].plot(x_axis, df_1['ActCurrentY'], label='ActCurrentY_1', color='brown')
# axs[2].plot(x_axis, df_1['ActCurrentSpindle'], label='ActCurrentSpindle_1', color='black')
axs[2].plot(x_axis, df_2['ActCurrentX'], label='ActCurrentX_2', color='red', linestyle='dashed')
axs[2].plot(x_axis, df_2['ActCurrentY'], label='ActCurrentY_2', color='green', linestyle='dashed')
# axs[2].plot(x_axis, df_2['ActCurrentSpindle'], label='ActCurrentSpindle_2', color='blue', linestyle='dashed')
axs[2].set_title('Actual Axis Current Over Time')
axs[2].legend()

# Plot the current in the fourth subplot
axs[3].plot(x_axis, df_1['ActCurrentSpindle'], label='ActCurrentSpindle_1', color='black')
axs[3].plot(x_axis, df_2['ActCurrentSpindle'], label='ActCurrentSpindle_2', color='blue', linestyle='dashed')
axs[3].set_title('Actual Spindle Current Over Time')
axs[3].legend()

# Plot the current in the fifth subplot
axs[4].plot(x_axis, df_1['ActCurrentX'], label='ActCurrentX_1', color='purple')
axs[4].plot(x_axis, df_1['ActCurrentY'], label='ActCurrentY_1', color='brown')
axs[4].plot(x_axis, df_1['ActCurrentSpindle'], label='ActCurrentSpindle_1', color='black')
axs[4].plot(x_axis, df_2['ActCurrentX'], label='ActCurrentX_2', color='red', linestyle='dashed')
axs[4].plot(x_axis, df_2['ActCurrentY'], label='ActCurrentY_2', color='green', linestyle='dashed')
axs[4].plot(x_axis, df_2['ActCurrentSpindle'], label='ActCurrentSpindle_2', color='blue', linestyle='dashed')
axs[4].set_title('Actual Current Over Time')
axs[4].legend()


plt.tight_layout()
plt.savefig(save_path)

plt.show()





# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import matplotlib.dates as mdates


# file_path = '~/Desktop/data_20231124-113655.csv'
# save_path = 'plot_image.png'


# locator = mdates.MinuteLocator()

# # Load data
# df = pd.read_csv(file_path, parse_dates=['Timestamp'])
# # Load df from 50 to avoid outliers and achieve better visualization
# df = df[50:]

# fig, axs = plt.subplots(3, 1, figsize=(15, 15))

# # Plot the position in the first subplot
# axs[0].plot(df['Timestamp'], df['ActPosX'], label='ActPosX', color='red')
# axs[0].plot(df['Timestamp'], df['ActPosY'], label='ActPosY', color='green')
# axs[0].set_title('Actual Position Over Time')
# axs[0].legend()
# axs[0].xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))
# axs[0].xaxis.set_major_locator(locator)

# # Plot the speed in the second subplot
# axs[1].plot(df['Timestamp'], df['ActSpeedX'], label='ActSpeedX', color='blue')
# axs[1].plot(df['Timestamp'], df['ActSpeedY']/20, label='ActSpeedY', color='orange')
# axs[1].set_title('Actual Speed Over Time (Y values divided by 20 for better visualization)')
# axs[1].legend()
# axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))
# axs[1].xaxis.set_major_locator(locator)

# # Plot the current in the third subplot
# axs[2].plot(df['Timestamp'], df['ActCurrentX'], label='ActCurrentX', color='purple')
# axs[2].plot(df['Timestamp'], df['ActCurrentY'], label='ActCurrentY', color='brown')
# axs[2].plot(df['Timestamp'], df['SpindelDriveLoad'], label='SpindelDriveLoad', color='black')
# axs[2].set_title('Actual Current Over Time')
# axs[2].legend()
# axs[2].xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))
# axs[2].xaxis.set_major_locator(locator)

# plt.tight_layout()
# plt.savefig(save_path)

# plt.show()

