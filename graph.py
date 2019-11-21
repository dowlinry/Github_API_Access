import pandas as pd
import numpy as np

class Graph:
    file_name = ""
    df = pd.DataFrame()

    def __init__(self,file_name):
        self.file_name = file_name

    def create_dataframe(self):
        self.df = pd.read_json(self.file_name)

    def get_dataframe(self):
        return self.df

    def create_graph(self):
        test_df = self.df
    
    def calculate_avg_popularity_score(self, num_languages):
        tmp_df = self.df
        avg_popularity_score = (tmp_df.loc[tmp_df['Number of Known Languages'] == 1])['Popularity Score'].mean()
        return avg_popularity_score
        
    def get_most_used_languages(self, num_languages):
        count = 0