# Apache Wizard "Wizzy"

**Powered by Apache Blackout Studio’s WizKit, WizOS, Keybine V8, and DeepSense.
Made in collaboration with RXQuisite.**

---


## About
Apache Wizard or “Wizzy” is a personal assistant designed and built by Apache Blackout Studio and RXQuisite. Of its many iterations and variations, the best one, Wiz X, is designed to be run on the Discord platform. It is powered by Apache Blackout Studio’s software-WizKit (Wiz personal assistant templates), WizOS (Wiz personal assistant architecture), Keybine (command handling x for Wiz), and DeepSense (high-level intelligence and NLP for command processing).

Wizzy can be interacted with via text through the Discord platform, but also has a Siri Plugin to enable voice-based commands for iOS.

---

# Wiz X Features
Wizzy is currently in development (D1.0.0), but this is the complete feature list:
## Task Tracking Engine
- Name
- Due Date
- Assigned Date
- List
- Tags
- Notes
- Priority
## Event Tracking Engine
- Name
- Date, time
- Repeat
- Colour Code
- Notes
## Sorting Engine
- Chronological (due)
- Chronological (assigned)
- List
- Tags
- Text in Notes
- Colour Code
- Priority
## Configs
- Configurations
## Plugins
- Teamup
- Clash warning
- Aliases
- GKit
- Remote Listener

---

# Wiz X1 Features

These are the features of Wiz X v1:

- Task Tracking
    - Add task
    - View tasks (All)
    - Modify Task
- Event Tracking
    - Add events 
    - Modify Event 
    - View Events (All)

---

## More on Plugins
### Aliases
Namespace: `alias`

Create, use, switch, discard secured aliases. Aliases are like accounts and they are linked to your email address.

### Teamup
Namespace: `teamup`
Interact with Teamup API to fetch calendar events.


### Clash warning
Namespace: `cwarn`

Warn of clash in task/event scheduling. Can be configured via:

### GKit
Namespace: `gkit`

Everyone's favourite web tools are now accessible via Wiz X. Through the GKit plugin, you need to sign in to your Google Account and create automations to create, modify, and delete Google Documents.

### Remote Listener
Namespace: `reml`

If you are working with text files (code, txt, rtf, md, etc.), then this plugin is for you. It allows you to track changes to files and the people making those changes, just by creating a minion (remote listener) in that directory.

### Reaction Engine
Namespace: `reactor`

When Wizzy lists out your tasks as separate messages, you can use quick reactions such as a checkmark or clock emoji to mark the task as done or open up rescheduling options.


# Documentation
Do note that even though the documentation uses "wiz" for all the commands, replacing "wiz" with "orto" at the start will make no difference.
## Tap
```
wiz tap <your custom string here>
```
`customString`: the string to be echoed by the bot (can contain spaces)

The first command root, tap, is used as a sanity check to test if the bot is working at all. Your custom string, spanning multiple lines, will be echoed by the bot if everything is ok.

## Configurations
```
wiz config "<key>:<value>"
```
`key`: Key of the configuration to change

`value`: value of the new configuration

`-plugin`: raise this flag between config and the key value pair only if you need to configure a plugin:
```shell
wiz config -plugin "<key>:<value>"
```

You can use this to modify wizard configurations, plugin configurations, and 