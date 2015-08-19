#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime, sublime_plugin

class MetaSubstitutionCommand(sublime_plugin.TextCommand):
    # following https://github.com/dariusf/LambdaSubstitution/blob/master/Lambda%20Substitution.py
    def run(self, edit, key=None):
        assert(not key is None)
        list_to_map = lambda seq: dict([(el["from"], el["to"]) for el in seq])
        if not hasattr(self, "_settings"):
            default_settings = sublime.load_settings("MetaSubstitution.sublime-settings")
            user_settings = sublime.load_settings("Preferences.sublime-settings")
            meta_substitutions = list_to_map(default_settings.get("meta_substitutions", []))
            meta_substitutions.update(list_to_map(user_settings.get("meta_substitutions", [])))
            setattr(self, "_settings", meta_substitutions)
        selection = self.view.sel()
        stored_cursor_positions = []
        substitute_for = None

        for k, v in self._settings.items():
            if k == key:
                substitute_for = v
        
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