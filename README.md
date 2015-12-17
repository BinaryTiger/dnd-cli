
<img src="https://img.shields.io/sonar/http/binarytiger.me:9000/03:dnd-cli/tech_debt.svg">

#Python cli for lazy DMs

##Working command

- Build a random city with the specified city name and with a population of 10 000

```shell
python3 dnd.py build city {cityName} --random
```

- Working flags
```shell
-h -> show help
-v -> verbose. Doesn't show much more as of right now
-V -> show program version
--overwrite -> overwrite the file if it already exist (default = false)
--random -> build a random object (Only working for city right now)
```

##Short Term Road Map

- Random NPC
- Parametered City
- Parametered NPC
- Showing built city by name
- Showing built npc by name 
