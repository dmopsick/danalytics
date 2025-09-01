from singleEventProbability import calculate_single_event_probability
import sys

FAVORABLE_OUTCOMES_NO_SHINY_CHARM = 1
FAVORABLE_OUTCOMES_YES_SHINY_CHARM = 3
TOTAL_OUTCOMES = 8192

def calcualte_soft_rest_probability(has_shiny_charm, pokemon_name, num_encounters):
    favorable_outcomes =  FAVORABLE_OUTCOMES_NO_SHINY_CHARM

    if has_shiny_charm.lower() == 'true':
        favorable_outcomes = FAVORABLE_OUTCOMES_YES_SHINY_CHARM
    
    shiny_chance_by_now = calculate_single_event_probability(favorable_outcomes, TOTAL_OUTCOMES, num_encounters)

    shiny_percentage_by_now = round(shiny_chance_by_now, 4) * 100

    print("The likelihood you would have caught a shiny " + pokemon_name + " after " + str(int(num_encounters)) + " encounters is " + str(shiny_percentage_by_now) + "%. #DANalytics")



# TODO Add some validation

# Take in the arguments
has_shiny_charm = sys.argv[1]
pokemon_name = sys.argv[2]
num_encounters = float(sys.argv[3])

calcualte_soft_rest_probability(has_shiny_charm, pokemon_name, num_encounters)