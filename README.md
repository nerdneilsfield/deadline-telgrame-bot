# deadline-telgrame-bot
A very simple telegram bot to remind deadlines

## Run

1. `clone` the repository

```
git clone https://github.com/nerdneilsfield/deadline-telgrame-bot.git
```

2. create your configuration

```
make config

vim config/config.yml
```

the configuration file is very simple:

```
telegram_token: "" // your telegram token here
time_zone : "Asia/Shanghai" // your timezone here, see the list of all avaliable timezone: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
```

3. build the docker container

```
make build
```

4. run the robot

```
make up
```
