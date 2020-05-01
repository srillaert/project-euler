from collections import Counter
from enum import IntEnum

class Rank(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

card_value_to_int = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class PlayerHand:
    def __init__(self, str):
        self.sorted_card_values = sorted(card_value_to_int[str[i]] for i in range(0, 13, 3))

        are_consecutive_values = all(self.sorted_card_values[i] == self.sorted_card_values[0] + i for i in range(1, 5))
        are_same_suit = all(str[i] == str[1] for i in range(4, 14, 3))
        if are_same_suit:
            self.rank_value = self.sorted_card_values[4]
            if are_consecutive_values:
                if self.sorted_card_values[4] == 14:
                    self.rank = Rank.ROYAL_FLUSH
                else:
                    self.rank = Rank.STRAIGHT_FLUSH
            else:
                self.rank = Rank.FLUSH
        elif are_consecutive_values:
            self.rank_value = self.sorted_card_values[4]
            self.rank = Rank.STRAIGHT
        else:
            counter = Counter(self.sorted_card_values)
            two_most_common = counter.most_common(2)
            count_most_common = two_most_common[0][1]
            self.rank_value = two_most_common[0][0]
            count_second_most_common = two_most_common[1][1]
            if count_most_common == 4:
                self.rank = Rank.FOUR_OF_A_KIND
            elif count_most_common == 3:
                if count_second_most_common == 2:
                    self.rank = Rank.FULL_HOUSE
                else:
                    self.rank = Rank.THREE_OF_A_KIND
            elif count_most_common == 2:
                if count_second_most_common == 2:
                    self.rank = Rank.TWO_PAIRS
                else:
                    self.rank = Rank.ONE_PAIR
            else:
                self.rank = Rank.HIGH_CARD

def is_win_for_player1(player1, player2):
    if player1.rank == player2.rank:
        if player1.rank_value == player2.rank_value:
            for i in range(4,-1,-1):
                if player1.sorted_card_values[i] != player2.sorted_card_values[i]:
                    return player1.sorted_card_values[i] > player2.sorted_card_values[i]
            return False # Players' hands are the same
        return player1.rank_value > player2.rank_value
    else:
        return player1.rank > player2.rank

if __name__ == "__main__":
    result = 0
    with open("p054.input") as input_file:
        for line in input_file:
            player1 = PlayerHand(line[0:14])
            player2 = PlayerHand(line[15:29])
            if is_win_for_player1(player1, player2):
                result += 1
    print(result)

def test_royal_flush():
    player = PlayerHand("TD AD JD QD KD")
    assert player.rank == Rank.ROYAL_FLUSH

def test_straight():
    straight = PlayerHand("TD AC JC QS KH")
    assert straight.rank == Rank.STRAIGHT

def test_hand1():
    player1 = PlayerHand("5H 5C 6S 7S KD") # Pair of Fives
    assert player1.rank == Rank.ONE_PAIR
    player2 = PlayerHand("2C 3S 8S 8D TD") # Pair of Eights
    assert player2.rank == Rank.ONE_PAIR
    assert not is_win_for_player1(player1, player2)

def test_hand2():
    player1 = PlayerHand("5D 8C 9S JS AC") # Highest card Ace
    assert player1.rank == Rank.HIGH_CARD
    player2 = PlayerHand("2C 5C 7D 8S QH") # Highest card Queen
    assert player2.rank == Rank.HIGH_CARD
    assert is_win_for_player1(player1, player2)

def test_hand3():
    player1 = PlayerHand("2D 9C AS AH AC") # Three Aces
    assert player1.rank == Rank.THREE_OF_A_KIND
    player2 = PlayerHand("3D 6D 7D TD QD") # Flush with Diamonds
    assert player2.rank == Rank.FLUSH
    assert not is_win_for_player1(player1, player2)

def test_hand4():
    player1 = PlayerHand("4D 6S 9H QH QC") # Pair of Queens, Highest card Nine
    assert player1.rank == Rank.ONE_PAIR
    player2 = PlayerHand("3D 6D 7H QD QS") # Pair of Queens, Highest card Seven
    assert player2.rank == Rank.ONE_PAIR
    assert is_win_for_player1(player1, player2)

def test_hand5():
    player1 = PlayerHand("2H 2D 4C 4D 4S") # Full House with Three Fours
    assert player1.rank == Rank.FULL_HOUSE
    player2 = PlayerHand("3C 3D 3S 9S 9D") # Full House with Three Threes
    assert player2.rank == Rank.FULL_HOUSE
    assert is_win_for_player1(player1, player2)