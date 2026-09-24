class Glassware:
    def __init__(self):
        pass

    def show_info(self):
        print("Glassware")


class Beaker(Glassware):
    def __init__(self):
        super().__init__()

    def show_info(self):
        print("Beaker")


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker(),
            Beaker(),
            Beaker(),
            Beaker(),
            Beaker()
        ]

    def show_beakers(self):
        print("Tray contains 5 beakers:")
        for beaker in self.beakers:
            beaker.show_info()
