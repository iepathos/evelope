
class Piles():
    def getGeneral(total,piles):
        for pile in piles:
            total = total - piles[pile]
        return total
