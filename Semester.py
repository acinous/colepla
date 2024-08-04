class Semester:
    def __init__(self, season, year, classes=None):
        self.classes = classes if classes is not None else []
        self.season = season
        self.year = year


