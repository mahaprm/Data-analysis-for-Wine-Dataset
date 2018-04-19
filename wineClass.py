import pandas as pa
import matplotlib.pyplot as plt

plt.style.use('ggplot')


class Wine():
    def __init__(self):
        # Reading the data from dataset file
        self.data = pa.read_csv("wine_dataset.csv")

    #
    def group_by_df(self, wine):
        white_gb = wine.groupby(['quality', 'style'])
        white_counts = white_gb.size().to_frame(name='counts')
        white_counts = (
            white_counts
                .join(white_gb.agg({'fixed_acidity': 'mean'}).rename(columns={'fixed_acidity': 'fixed_acidity_mean'}))
                .join(white_gb.agg({'fixed_acidity': 'median'}).rename(columns={'fixed_acidity': 'fixed_acidity_median'}))
                .join(white_gb.agg({'volatile_acidity': 'mean'}).rename(columns={'volatile_acidity': 'volatile_acidity_mean'}))
                .join(white_gb.agg({'volatile_acidity': 'median'}).rename(columns={'volatile_acidity': 'volatile_acidity_median'}))
                .join(white_gb.agg({'alcohol': 'mean'}).rename(columns={'alcohol': 'alcohol_mean'}))
                .join(white_gb.agg({'alcohol': 'median'}).rename(columns={'alcohol': 'alcohol_median'}))
                .join(white_gb.agg({'total_sulfur_dioxide': 'mean'}).rename(columns={'total_sulfur_dioxide': 'total_sulfur_dioxide_mean'}))
                .join(white_gb.agg({'total_sulfur_dioxide': 'median'}).rename(columns={'total_sulfur_dioxide': 'total_sulfur_dioxide_median'}))
                .reset_index())
        return white_counts

    def plot_bar(self, wine, color, plot_color):
        # Red wine Bar chart
        plt.figure()
        wine['counts'].plot.bar(color=plot_color)
        plt.title(color)
        plt.ylabel('Observations')
        plt.xlabel('Quality')
        plt.grid([])
        plt.legend()
        return

    def plot_chart(self, wine, name,display_name, color, plot_color):
        fig, ax = plt.subplots()
        ax.plot(wine['quality'], wine[name + '_mean'], 'k--', label='Mean', color=plot_color)
        ax.plot(wine['quality'], wine[name + '_median'], 'k', label='Median', color=plot_color)
        plt.title(color)
        plt.ylabel(display_name)
        plt.xlabel('Quality')
        plt.legend()
        ax.grid(False)
        return

    def split_wine_type(self, color, plot_color):
        wine_type = myObject1.data.loc[myObject1.data['style'] == color]
        grouped_by_df = myObject1.group_by_df(wine_type)
        myObject1.plot_bar(grouped_by_df, color, plot_color)
        myObject1.plot_chart(grouped_by_df, 'fixed_acidity', 'Fixed Acidity', color, plot_color)
        myObject1.plot_chart(grouped_by_df, 'volatile_acidity','Volatile Acidity', color, plot_color)
        myObject1.plot_chart(grouped_by_df, 'alcohol', 'Alcohol', color, plot_color)
        myObject1.plot_chart(grouped_by_df, 'total_sulfur_dioxide', 'Tatal So2', color, plot_color)
        return


if __name__ == '__main__':
    myObject1 = Wine()
    myObject1.split_wine_type('red', 'brown')
    myObject1.split_wine_type('white', 'yellow')
    plt.show()
