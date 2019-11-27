import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

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
        fig = go.Figure()
        count0 = 0
        while(count0 <= max_languages):
            count1 = 0
            while(count1 <= max_languages):
                tmp_dict = y[count1]
                try:
                    key = min(tmp_dict, key = tmp_dict.get)
                    tmp_x = []
                    tmp_y = []
                    tmp_x.append(count1)
                    tmp_y.append(tmp_dict[key])
                    fig.add_bar(x = tmp_x, y = tmp_y, name = str(key)) 
                    tmp_dict.pop(key)
                    y[count1] = tmp_dict                  
                except (ValueError, TypeError) as e:
                  pass
                count1 = count1 + 1
            count0 = count0 + 1 

        fig.update_layout(
            barmode = 'stack',
            xaxis_title = "Number of Languages Known",
            yaxis_title = "Average Popularity Score per Language Known",
            title = 'Popularity vs Languages Known',
            showlegend = False
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
            val = self.get_most_used_languages(count)
            y.append(val)
            count = count + 1
        return y

    def get_most_used_languages(self, num_languages):  
        if(self.calculate_avg_popularity_score(num_languages) == 0):
            return {}
        else:
            count = 0
            tmp_dict = {}
            tmp_df = self.lang_df.loc[self.lang_df['Number of Languages Known By User'] == num_languages]
            for index,row in tmp_df.iterrows():
                lang = row['Language']
                if(tmp_dict.get(lang) == None):
                    tmp_dict.update({lang : 1})
                else:
                    count = tmp_dict.get(lang)
                    count = count + 1
                    tmp_dict.update({lang: count})
            count = 0
            langs = {}
            while(count < num_languages):
                max_key = max(tmp_dict, key = tmp_dict.get)
                max_key_value = tmp_dict.get(max_key)
                langs.update({max_key: max_key_value})
                tmp_dict.pop(max_key, None)
                count = count + 1
            pop = self.calculate_avg_popularity_score(num_languages)
            total_val = sum(langs.values())
            for lang in langs:
                new_val = ((langs.get(lang)/total_val)*pop).round()
                langs.update({lang: new_val})
            return langs
    
    def create_dataframe(self):
        list = self.generate_y_axis(self.get_max_languages())
        df = pd.DataFrame(columns = ['Language','Approx. Popularity Score of Language','Languages Known by User'])
        count = 0
        index = 0
        while(count <= self.get_max_languages()):
            try:
                tmp_dict = list[count]
                key = min(tmp_dict, key = tmp_dict.get)
                df.loc[index] = [str(key)] + [tmp_dict[key]] + [count]
                tmp_dict.pop(key)
                list[count] = tmp_dict
                index = index + 1
            except(TypeError,ValueError):
                count = count + 1
        return df

