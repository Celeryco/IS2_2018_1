"""
The main function is defined here. It simply creates an instance of
tools.Control and adds the game states to its dictionary using
tools.setup_states.  There should be no need (theoretically) to edit
the tools.Control class.  All modifications should occur in this module
and in the prepare module.
"""

from .import settings, tools
from .states import main_menu, instructions_menu, game


def main():
    """Add states to control here."""
    run_it = tools.Control(settings.TITLE)

    state_dict = {"MAIN_MENU" : main_menu.MainMenu(),
                  "INSTRUCTIONS"  : instructions_menu.InstructionsMenu(),
                  "GAME" : game.Game()
                  }
    run_it.setup_states(state_dict, "MAIN_MENU")
    
    run_it.main()
