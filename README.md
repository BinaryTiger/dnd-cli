
<!--<img src="https://img.shields.io/sonar/http/binarytiger.me:9000/03:dnd-cli/tech_debt.svg">-->

#Python cli for lazy DMs

PLEASE NOTE THAT THIS PROGRAM IS STILL UNDER HEAVY DEVELOPEMENT. YOU SOULDN'T RELY ON IT OR EXPECT IT TO STAY AS IT IS.

##Working command

- Build a random city with the specified city name

```shell
python3 dnd.py build city {cityName} --random
```

- Build a random NPC with the specified npc name

```shell
python3 dnd.py build npc {npcName} --random
```

- Show a city by its name (name of the file without the extension)

```shell
python3 dnd.py show city {cityName}
```

- Show a npc by its name (name of the file without the extension)

```shell
python3 dnd.py show npc {npcName}
```

- Working flags
```shell
-h -> show help
-v -> verbose
-V -> show program version
--overwrite -> overwrite the file if it already exist (default = false)
--random -> build a random object
--forcename -> force the program to use the specified name. To use with --random (Only working with cities)
```

##Short Term Functionality Road Map

- Parametered City
- Parametered NPC
- Random NPC names (by race)
- NPC races

##Programming Road map

- Split city into city object and city builder class
- Make build_random static when city name table is there