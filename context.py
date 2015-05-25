import sublime
import sublime_plugin

from PowerShellConsole.lib.contexts import PsContexts


class PsContextListener(sublime_plugin.EventListener):

    def __init__(self, *args, **kwargs):
        self.contexts = PsContexts()
        super().__init__(*args, **kwargs)

    def on_query_context(self, view, key, operator, operand, match_all):
        return self.contexts.check(view, key, operator, operand, match_all)
