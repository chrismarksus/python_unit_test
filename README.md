# Python unit test project 

This project is a demo project for teaching how to use unit testing in python.

The project has examples for vagrant with ansible provisioning and docker and docker-compose environments for demostrating how to use vagrant and docker as dev environments. 

## Getting Started

To get started to will need to have VM software installed or know how to setup python yourself.

### Use docker as a VM

```bash
# build the docker from the Dockerfile
docker build - cmarks/ubuntu_python_pip_3 .

# Run the 
docker run -it --rm -v $(pwd)/:/python_unit_test/ cmarks/ubuntu_python_pip_3 /bin/bash

# python is the name of the service in the Dockerfile
docker-compose run python bash

```
### Use vagrant as a VM

```bash
# start vagrant from the main directory
vagrant up

# if a change is made to the ansible playbook run
vagrant provision

# to stop the VM 
vagrant halt && vagrant destroy
```

Once the docker container is open in the terminal ```cd /python_unit_test/app``` and run the line ```python3 -m unittest discover``` this will run the unit tests in the ```/app``` directory.  


```bash
# move to the directory
cd basicproject/

# Run the python unittest
python3 -m unittest discover -v
# or
python3 test/test_basicfunction.py

```


### Prerequisites

To get start you will need to the following software:

* Virtualbox
* Vagrant
* Putty (Optional)

## Authors

* **Chris Marks** - *Initial work* - [chrismarksus](https://github.com/chrismarksus)

## Links
* [be pythonic](http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html)
* [python unit testing structuring your project](http://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/)
