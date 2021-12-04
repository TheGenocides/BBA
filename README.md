<h2 align="center">BBA</h2>

BBA is An object oriented, synchronous api wrapper for BreadBotAPI.

# Usages

```py
import bba

#Generate Random Sentence

client = bba.Client("YOUR API KEY HERE")
word = client.get_sentence()
print(word.response)

#Calculator

res = client.calculator("AnsxAns+10", "10")
print(res.result)
```

# Important Links

- [get api key](https://api.breadbot.me/login)
- [support server](https://discord.gg/nbWfGT6PFR) 
- [Documentations](https://api.breadbot.me)