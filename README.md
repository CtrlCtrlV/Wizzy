# Apache Wizard "Wizzy"

**Powered by Apache Blackout Studio’s WizKit, WizOS, Keybine V8, and DeepSense.
Made in collaboration with RXQuisite.**

---


## About
Apache Wizard or “Wizzy” is a personal assistant designed and built by Apache Blackout Studio and RXQuisite. Of its many iterations and variations, the best one, Wiz X, is designed to be run on the Discord platform. It is powered by Apache Blackout Studio’s software-WizKit (Wiz personal assistant templates), WizOS (Wiz personal assistant architecture), Keybine (command handling x for Wiz), and DeepSense (high-level intelligence and NLP for command processing).

Wizzy can be interacted with via text through the Discord platform, but also has a Siri Plugin to enable voice-based commands for iOS.

# Wiz X1.0 Features
Wizzy is currently in development (D1.0.0), and this is the feature list:
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

## More on Plugins
### Aliases
Namespace: `alias`

Create, use, switch, discard secured aliases. Aliases are like accounts and they are linked to your email address.

### Teamup
Namespace: `teamup`


### Clash warning
Namespace: `cwarn`

Warn of clash in task/event scheduling. Can be configured via:
```
wiz config --plugin cwarn "warn:tasks,events"
```

### GKit
Namespace: `gkit`

Everyone's favourite web tools are now accessible via Wiz X. Through the GKit plugin, you need to sign in to your Google Account and create automations to create, modify, and delete Google Documents. Activate it via:
```
wiz init --plugin gkit
```
and the bot will send you a private message asking for your email address and password. In this private message, you can also add collaborators with:
```
wiz !gkit add collaborators "<emailAddress>:<password>,..."
```
### Remote Listener
Namespace: `reml`

If you are working with text files (code, txt, rtf, md, etc.), then this plugin is for you. It allows you to track changes to files and the people making those changes, just by creating a minion (remote listener) in that directory.
