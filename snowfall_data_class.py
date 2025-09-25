class SnowfallDataEntry:
    def __init__(self, month, day, amount):
        self.month = month.strip()
        self.day = day.strip()
        self.amount = amount.strip()