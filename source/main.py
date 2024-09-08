import pandas as pd
from matplotlib import pyplot as plt
import os


class DrawingPlots:
    @staticmethod
    def scatter_plot(dataframe, x, y, title, filename):
        plt.figure()
        dataframe.plot(kind='scatter', x=x, y=y, s=12, alpha=1)
        plt.title(title)
        filepath = os.path.abspath(f'../plots/{filename}.png')
        plt.savefig(filepath)
        plt.close()
        return filepath

    @staticmethod
    def histogram_plot(dataframe, column, title, filename, bins=20):
        plt.figure()
        dataframe[column].plot(kind='hist', bins=bins, title=title)
        filepath = os.path.abspath(f'../plots/{filename}.png')
        plt.savefig(filepath)
        plt.close()
        return filepath

    @staticmethod
    def draw_plots(dataframe):
        plots = []

        plots.append(DrawingPlots.scatter_plot(dataframe, 'gt_corners', 'rb_corners',
                                               'gt_vs_rb_corners', 'gt_vs_rb_corners'))
        plots.append(DrawingPlots.scatter_plot(dataframe, 'max', 'min',
                                               'max_vs_min_corners', 'max_vs_min_corners'))
        plots.append(DrawingPlots.scatter_plot(dataframe, 'mean', 'max',
                                               'mean_vs_max_corners', 'mean_vs_max_corners'))

        plots.append(DrawingPlots.histogram_plot(dataframe, 'gt_corners',
                                                 'gt_corners', 'gt_corners_hist'))
        plots.append(DrawingPlots.histogram_plot(dataframe, 'rb_corners',
                                                 'rb_corners', 'rb_corners_hist'))
        plots.append(DrawingPlots.histogram_plot(dataframe, 'mean', 'mean', 'mean_hist'))
        plots.append(DrawingPlots.histogram_plot(dataframe, 'max', 'max', 'max_hist'))
        plots.append(DrawingPlots.histogram_plot(dataframe, 'min', 'min', 'min_hist'))

        dataframe['diff_mean'] = (dataframe['floor_mean'] - dataframe['ceiling_mean']).abs()
        plots.append(DrawingPlots.histogram_plot(dataframe, 'diff_mean',
                                                 'floor_mean - ceiling_mean', 'diff_mean'))

        dataframe['diff_min'] = (dataframe['floor_min'] - dataframe['ceiling_min']).abs()
        plots.append(DrawingPlots.histogram_plot(dataframe, 'diff_min',
                                                 'floor_min - ceiling_min', 'diff_min'))

        dataframe['diff_max'] = (dataframe['floor_max'] - dataframe['ceiling_max']).abs()
        plots.append(DrawingPlots.histogram_plot(dataframe, 'diff_max',
                                                 'floor_max - ceiling_max', 'diff_max'))

        return plots


if __name__ == '__main__':
    df1 = pd.read_json("../jsons/deviation.json")
    print(DrawingPlots.draw_plots(df1))
