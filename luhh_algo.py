class Luhn:  
    def __init__(self, card_num):
        
        self.card_num = card_num[::-1].replace(" ", "")
        
        
    def valid(self):
        if not self.card_num.isdigit() or len(self.card_num) <= 1:
            return False
        result = []
        card = self.card_num
        if card[-1] == 0:
            card = card[:-1]
        for i, num in enumerate(card):
            num = int(num)
            if not i % 2 == 0:
                num *= 2
            if num > 9:
                num = num - 9
            result.append(num)
        if sum(result) % 10 == 0:
            return True
        return False