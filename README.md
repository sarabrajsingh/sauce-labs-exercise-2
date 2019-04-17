# Raj's Sauce Lab Exercise 2 Interview Technical Test

The purpose of this project is to build, containerize, test and deploy a simple RESTful API service
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python3, Pip3, Virtualenv

```bash
sudo apt-get install python3.7 -y
sudo apt-get install pip3 -y
sudo apt install virtualenv -y
```

Minikube
```
https://kubernetes.io/docs/tasks/tools/install-minikube
```

Helm
```
https://helm.sh/docs/using_helm
```

Flask and Ansible
```bash
pip3 install -r requirements.txt
```

## Deployment

The entire ci/cd stack can be executed via an ansible playbook. The following command can be ran from the root directory of the project.

Step   | Action
-------|-------
Build  | Creates application container, pushes container to dockerhub, runs unit tests
Deploy | Leverages HELM to deploy the chart against a local minikube k8s cluster
Smoke  | Leverages Selenium, and the CHROME webdriver to perform a basic test against the deployment

***note - runtime user has to know the ansible-vault password***

```bash
ansible-playbook -i non-production --ask-vault-pass setup.yaml
```

## Running the tests

Unit testing and smoke testing are integrated into the ansible playbook. If you want to execute them induvidually, please execute the following commands.

***unit tests***
```bash
python3 tests/unit_test.py
```

***smoke tests***
```bash
python3 tests/selenium_tests.py
```

***please note that your helm deployment into a minikube k8s cluster must have been successful prior to executing the smoke tests manually***

## Built With

***hyperlinks are wrong i didn't have time to update them***

* [Ansible](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Python](https://maven.apache.org/) - Dependency Management
* [Flask](https://rometools.github.io/rome/) - Used to generate RSS Feeds
* [Selenium](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Pytest](https://maven.apache.org/) - Dependency Management

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Sarabraj Singh** - *Initial work* - [sarabrajsingh](https://github.com/sarabrajsingh)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* geerlingguy
* stackedoverflow