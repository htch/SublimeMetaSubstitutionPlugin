## Meta Substitution Plugin for Sublime Text 2/3

Enables replacing default Option+? key combinations in OS X for custom symbols.

Newly installed plugin retains default key combinations. To configure the plugin add "meta_substitutions" property in User Settings like so:

        {
            ... your other settings
            "meta_substitutions": [
                {
                    "from": "Key (sans the Option+ modifier) such as 'u', 'U' or '1'",
                    "to": "Desired symbol such as ₽ or £"
                },
                ... more keys
            ]
        }


### Configuration Variants

#### Scala unicode operators "←", "→", "⇒" in Sublime Text 

        "meta_substitutions": [
            {
                "from": ",",
                "to": "←"
            },
            {
                "from": ".",
                "to": "→"
            },
            {
                "from": "/",
                "to": "⇒"
            }
        ]