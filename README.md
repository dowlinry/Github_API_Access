# Github API Visualisation Assignment

This program gathers data from multiple organisations using the GitHub API to compare the popularity of programmers versus the amount of languages they program in.

The aim of gathering this data was to see if knowing more languages makes you a more popular programmer, or is it better to specialise in just a handful.

Data was taken from Amazon, Apple, Intel and Facebook, but it is possible to use this for any organisation that has a GitHub repository.

Data was gathered using the GitHub API via PyGithub, and stored into Pandas DataFrames to be organised. DataFrames were then converted into JSON files, which were then converted into a Plotly Bar Chart and displayed using Plotly.

# Example of Graph
![](https://github.com/dowlinry/Github_API_Access/blob/master/images/full_graph.png)

Each full bar represents the average popularity of the users who know X amount of languages. Each section of the full bar represents how much each language of the X languages contributed to the total popularity.

# Example of hover text
![](https://github.com/dowlinry/Github_API_Access/blob/master/images/hover_text.gif)

# Requirements
- Python
- Pandas
- Plotly
- PyGithub

# User Guide
- By default, the graph displays pre-gathered information from Amazon, Apple, Intel and Facebook. 
- To add or remove organisations:
  - Generate a GitHub Access Token as seen here: https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line
  - In github_access.py, replace g = Github("") with g = Github("*Your Access Token*")
  - Use function add_organisation(*organisation name*) to add an organisation to the organisation list
  - Use function remove_organisation(*organisation name*) to remove an organisation from the organisation list
  - Run github_access.py to generate the data from the list of organisations
  - *Note: Adding one organisation and re-running the program will cause it to re-gather data from all organisations, not just the new one*
 - Run app.py to generate and display the graph of your gathered data
