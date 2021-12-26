class Series:
    def __init__(self, title, genre, seasons, platform, actor):
        self.title = title
        self.genre = genre
        self.seasons = seasons
        self.platform = platform
        self.actor = actor

rnm = Series('Rick And Morty', 'Comedy', 4, 'Adult-Swim', 'Roiland')
print(vars(rnm))