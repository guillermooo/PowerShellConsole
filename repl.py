import sublime
import sublime_plugin


class new_ps_console(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.new_file()
        v.set_name('~PowerShell Console~')
        v.set_scratch(True)
        v.run_command('append', {'characters': "> "})
        v.sel().clear()
        v.sel().add(sublime.Region(v.size()))
        v.set_syntax_file('Packages/PowerShellConsole/PowerShellConsole.sublime-syntax')


class PsEvaluate(sublime_plugin.TextCommand):
    def run(self, edit):
        cmd_line_region = self.view.line(self.view.sel()[0])
        text = self.view.substr(cmd_line_region)
        new_cmd_line = '\nOUT: evaluated: {}\n> '.format(text)
        target = min(cmd_line_region.end() + 1, self.view.size())
        self.view.insert(edit, target, new_cmd_line)
