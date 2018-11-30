# ui-consul-request
Web ui curl for consul

## Getting Started

### Prerequisites
You must have it if you will run in docker:
* [docker](https://www.docker.com/) -  is a tool designed to make it easier to create, deploy, and run applications by using containers.
* [docker-compose](https://docs.docker.com/compose/) - is a tool for defining and running multi-container Docker applications.
* change server and port of your consul in docker compose file or you can build image manually and run it.

You must have it if you will run python manually:
* [python3](https://www.python.org/) - is a programming language that lets you work more quickly and integrate your systems more effectively.
* [python3-pip](https://pypi.org/project/pip/) - is a package management system

### Commands
```sh
$ docker-compose up -d  # docker-compose run
```
or
```sh
$ cd srv
$ chmod +x consul.py  # add permission for execute
$ ./consul.py --help  # show help
$ ./consul.py --server=localhost --port=9100  # run with you server ip and port
```


## Author
Matusevych Yevhenii 
* [LinkedIn](https://www.linkedin.com/in/ygritte/)
* [Telegram](https://t.me/YevheniiMatusevich)
