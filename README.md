# alex_homeegramm_bridge
This project wants to connect the smart home control unit homee(hom.ee) with the Amzon Echo.

With my setup your code will be deploeyed to AWS using (zappa). Be carefull the AWS services is not for free and can create costs. Be careful using it.

Thing you need to start:
- Amazon Developer Account (https://developer.amazon.com)
- AWS Account (https://aws.amazon.com/de/) / or local webserver
- local python environment
- flask-ask inside your local environment
- zappa inside your local environment


Log into your amazon developer account and create a new custom skill:

Fill all your informations.

You can find the intent schema inside the project code (link zum schema)

Inside the Custom Slot Type you have to add every homee webhook name you want to trigger.

Sample Utterances are the ways you want to trigger the skill.

Use HTTPS endpoint.

The url under Europe you find after deploying the code with zappa.

SSL Certificate please use the subdomain part.
