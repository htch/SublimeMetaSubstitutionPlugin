#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime, sublime_plugin

class MetaSubstitutionCommand(sublime_plugin.TextCommand):
    # following https://github.com/dariusf/LambdaSubstitution/blob/master/Lambda%20Substitution.py
    def run(self, edit, key=None):
        assert(not key is None)
        if not hasattr(self, "_settings"):
            setattr(self, "_settings", sublime.load_settings("MetaSubstitution.sublime-settings"))
        selection = self.view.sel()
        stored_cursor_positions = []
        substitute_for = None

        for pair in self._settings.get("meta_substitutions"):
            if pair["from"] == key:
                substitute_for = pair["to"]
        
        if substitute_for is None:
            return
        
        for subselection in selection:
            if subselection.empty():
                self.view.insert(edit, subselection.a, substitute_for)
            else:
                stored_cursor_positions.append(sublime.Region(subselection.begin() + 1))
                self.view.replace(edit, subselection, substitute_for)

        if stored_cursor_positions:
            selection.clear()
            for cursor_position in new_cursor_positions:
                selection.add(cursor_position)