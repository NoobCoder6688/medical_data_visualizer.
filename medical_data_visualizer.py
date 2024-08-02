import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



 

# 1
filepath = 'medical_examination.csv'
df =pd.read_csv(filepath)

# 2
df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).astype(int)

# 3
df.loc[df['cholesterol'] == 1,'cholesterol'] = 0
df.loc[df['cholesterol'] != 0, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] !=0, 'gluc'] = 1
print(df['gluc'])
# 4
def draw_cat_plot():
    # 5
    df_cat =pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat =df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    cat_plot = sns.catplot(
        x='variable', y='total', hue='value', col='cardio',
        data=df_cat, kind='bar', height=5, aspect=1
    )


    # 8
    fig = cat_plot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))
                 ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(16, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
