
from math import comb

class TcgProbabilityCalculator:

  def __init__(self, deck_size=60, hand_size=7):
    """
    Configure with standard deck size, hand size unless otherwise instructed
    """
    self.deck_size = deck_size
    self.hand_size = hand_size


  def opening_hand_probability(self, copies: int):
    """
    Determine the likelihood at least one copy of a specified group of 
    one or more cards to appear in your opening hand
  
    This allows for more than just determining if you will start with one of your
    4 Ultra Ball in deck. But one of your 4 Ultra Ball or 4 Nest ball
    This is achieved by not enforcing a maximum of 4 copies 
    """

    print("Hello Dan")

    # Validate the provided num of copies we are checking for
    if copies <= 0 or copies >= self.deck_size:
      return 0.0
    
    # Calculate the probability of 0 copies appearing in the first 7 cards
    no_copy_prob = comb(self.deck_size - copies, self.hand_size) / comb(self.deck_size, self.hand_size)

    return 1 - no_copy_prob