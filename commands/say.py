from evennia import Command
import random
from language.english.commands.say import *


class CmdSay(Command):
    """
    speak as your character in a certain tongue

    Usage:
      say <message>

    Talk to those in your current location.
    """
    key = "say"
    aliases = ['"', "'"]
    locks = "cmd:all()"

    def func(self):
        # Run the speak command

        caller = self.caller

        if not self.args:
            word = SAY_NOTHING.split()
            words = list(word)
            new_sentence = " ".join(random.shuffle(words, len(words)))
            caller.msg(new_sentence)
            return

        speech = self.args

        # calling the speech hook on the location
        speech = caller.location.at_say(caller, speech)

        # Feedback for the object doing the talking
        caller.msg('You say, "%s{n"' % speech)

        # Build the string to emit to neighbors
        emit_string = '%s says, "%s{n"' % (caller.name,
                                           speech)
        # sends message to everyone in the location except the caller
        caller.location.msg_contents(emit_string,
                                     exclude=caller)
