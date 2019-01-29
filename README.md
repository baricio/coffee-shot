# Coffee Shot

Program to choice one people in slack to do coffee

## Getting Started

 clone repo to start. git clone git@github.com:baricio/coffee-shot.git

### Prerequisites

Need to install python3.6, pip and pipenv

```
$ sudo add-apt-repository ppa:jonathonf/python-3.6
```

```
$ sudo apt-get update
```

```
$ sudo apt-get install python3.6
```

```
$ sudo apt-get install python-pip
```

```
$ pip install pipenv
```

### Installing

Now you need some configurations to run projec

install dependencies and run env into project path

```
pipenv install
```

```
pipenv shell
```

copy .env.exmaple to .env

```
cp .env.example .env
```

create incoming-webhooks api end point into slack [slack]https://api.slack.com/incoming-webhooks

fill .env variable with your end point

## Running

execute with `python shot.py`

## Authors

* **Fabricio Cunha** - *baricio* 

## License

This project is licensed under the MIT License