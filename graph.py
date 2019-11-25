import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot,iplot

class Graph:
    pop_df = pd.DataFrame()
    lang_df = pd.DataFrame()

    def __init__(self,file_name_1,file_name_2):
        self.pop_df = pd.read_json(file_name_1)
        self.lang_df = pd.read_json(file_name_2)

    def create_graph(self):
        max_languages = self.get_max_languages()
        x = self.generate_x_axis(max_languages)
        y = self.generate_y_axis(max_languages)
        fig = go.Figure(data = [go.Bar(
                        x = x, y = y                    
        )])
        fig.update_layout(
            title = "Title",
            xaxis_title = "Number of Languages Known",
            yaxis_title = "Average Popularity Score per Language Known",
        )
        plot(fig)
        return fig
 
    def calculate_avg_popularity_score(self, num_languages):
        tmp_df = self.pop_df
        avg_popularity_score = (tmp_df.loc[tmp_df['Number of Known Languages'] == num_languages])['Popularity Score'].mean()
        if(pd.isna(avg_popularity_score)):
            return 0
        else:
            return avg_popularity_score.round()
        
    def get_max_languages(self):
        max = self.pop_df['Number of Known Languages'].max()
        return max

    def generate_x_axis(self, max_languages):
        x = []
        count = 0;
        while(count <= max_languages):
            x.append(count)
            count = count + 1
        return x

    def generate_y_axis(self,max_languages):
        y = []
        count = 0
        while(count <= max_languages):
            val = self.calculate_avg_popularity_score(count)
            y.append(val)
            count = count + 1
        return y

    def get_most_used_languages(self, num_languages):  
        count = 0
        langs = {}
        tmp_df = self.lang_df.loc[self.lang_df['Number of Languages Known By User'] == num_languages]
        for index,row in tmp_df.iterrows():
            lang = row['Language']
            



            count = count + 1

        return langs
