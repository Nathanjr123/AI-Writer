from configparser import ConfigParser

config = ConfigParser ()

config ["DEFAULT"] = {

"APIkey": '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',

"Model": 'gpt-3.5-turbo',

"PromptWords": 'write me a detailed article using these keywords'

}
with open("default.ini", "w") as f:
    config.write(f)