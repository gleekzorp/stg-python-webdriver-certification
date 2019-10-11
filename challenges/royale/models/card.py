class Card:
    def __init__(self, id: int, cost: int, icon: str, name: str, type: str, arena: int, rarity: str):
        self.id = id
        self.cost = cost
        self.icon = icon
        self.name = name
        self.type = type
        self.arena = arena
        self.rarity = rarity

    # def get_type(self, api_type: str) -> str:
    #     if api_type == 'tid_card_type_building':
    #         card_type = 'Building'
    #     elif api_type == 'tid_card_type_spell':
    #         card_type = 'Spell'
    #     elif api_type == 'tid_card_type_character':
    #         card_type = 'Troop'
    #     return card_type