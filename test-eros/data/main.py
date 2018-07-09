"""
The main function is defined here. It simply creates an instance of
tools.Control and adds the game states to its dictionary using
tools.setup_states.  There should be no need (theoretically) to edit
the tools.Control class.  All modifications should occur in this module
and in the prepare module.
"""

from . import settings, tools
from .states import main_menu, instructions_menu, instructions_menu_2, game, high_score

def main():
    """Add states to control here."""
    run_it = tools.Control(settings.TITLE)

    state_dict = {"MAIN_MENU" : main_menu.MainMenu(),
                  "INSTRUCTIONS"  : instructions_menu.InstructionsMenu(),
                  "INSTRUCTIONS_2"  : instructions_menu_2.InstructionsMenu2(),
                  "GAME" : game.Game(),
                  "HIGH_SCORE" : high_score.HighScore()
                  }

    run_it.setup_states(state_dict, "MAIN_MENU")
    run_it.main()
