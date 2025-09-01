

#######################################
#
# Calculates the probability of a single event occuring when calculated n times
#
# Maybe I could use a built in library, but it's a simple enough formula
########################################
def calculate_single_event_probability(favorable_outcomes, total_outcomes, num_trials):
    return 1 - (1 - favorable_outcomes / total_outcomes) ** num_trials; 