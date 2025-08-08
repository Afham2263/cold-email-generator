import pandas as pd

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.df = None

    def load_portfolio(self):
        self.df = pd.read_csv(self.file_path)

    def query_links(self, skills):
        if self.df is None:
            return []

        matches = set()
        for skill in skills:
            filtered = self.df[self.df["Techstack"].str.contains(skill, case=False, na=False)]
            matches.update(filtered["Links"].tolist())

        return list(matches)

