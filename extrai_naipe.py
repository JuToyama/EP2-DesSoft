def extrai_naipe(a):
    lista= [a]
    listinha = []
    if (lista[0] == "A♦" or lista[0] == "2♦"  or lista[0] == "3♦" or lista[0] == "4♦" or lista[0] == "5♦" or lista[0] == "6♦" or lista[0] == "7♦" or lista[0] == "8♦" or lista[0] == "9♦" or lista[0] == "10♦" or lista[0] == "J♦" or lista[0] == "Q♦" or lista[0] == "K♦"):
        return "♦"
    if (lista[0] == "A♥" or lista[0] == "2♥" or lista[0] == "3♥" or lista[0] == "4♥" or lista[0] == "5♥" or lista[0] == "6♥" or lista[0] == "7♥" or lista[0] == "8♥" or lista[0] == "9♥" or lista[0] == "10♥" or lista[0] == "J♥" or lista[0] == "Q♥" or lista[0] == "K♥"):
        return "♥"
    if (lista[0] == "A♣" or lista[0] == "2♣" or lista[0] == "3♣" or lista[0] == "4♣" or lista[0] == "5♣" or lista[0] == "6♣" or lista[0] == "7♣" or lista[0] == "8♣" or lista[0] == "9♣" or lista[0] == "10♣" or lista[0] == "J♣" or lista[0] == "Q♣" or lista[0] == "K♣"):
        return "♣"
    if (lista[0] == "A♠" or lista[0] == "2♠" or lista[0] == "3♠" or lista[0] == "4♠" or lista[0] == "5♠" or lista[0] == "6♠" or lista[0] == "7♠" or lista[0] == "8♠" or lista[0] == "9♠" or lista[0] == "10♠" or lista[0] == "J♠" or lista[0] == "Q♠" or lista[0] == "K♠"):
        return "♠"