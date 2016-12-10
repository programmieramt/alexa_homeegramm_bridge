# alex_homeegramm_bridge
This project wants to connect the smart home control unit homee(hom.ee) with the Amzon Echo.

With my setup your code will be deploeyed to AWS using (zappa). Be carefull the AWS services is not for free and can create costs. Be careful using it.

Thing you need to start:
- Amazon Developer Account (https://developer.amazon.com)
- AWS Account (https://aws.amazon.com/de/) / or local webserver
- local python environment
- flask-ask inside your local environment (https://github.com/johnwheeler/flask-ask)
- zappa inside your local environment (https://github.com/Miserlou/Zappa)


Log into your amazon developer account and create a new custom skill:
![alt tag](https://raw.githubusercontent.com/programmieramt/alexa_homeegramm_bridge/master/pictures/alexa1.png)

Fill all your informations.
![alt tag](https://raw.githubusercontent.com/programmieramt/alexa_homeegramm_bridge/master/pictures/skill1.png)
You can find the intent schema inside the project code (https://github.com/programmieramt/alexa_homeegramm_bridge/blob/master/intent_schema)
![alt tag](https://raw.githubusercontent.com/programmieramt/alexa_homeegramm_bridge/master/pictures/interaction.png)
Inside the Custom Slot Type you have to add every homee webhook name you want to trigger.(https://github.com/programmieramt/alexa_homeegramm_bridge/blob/master/custom_slots)
Sample Utterances are the ways you want to trigger the skill.(https://github.com/programmieramt/alexa_homeegramm_bridge/blob/master/utterance)
Use HTTPS endpoint.
The url under Europe you find after deploying the code with zappa.
![alt tag](https://raw.githubusercontent.com/programmieramt/alexa_homeegramm_bridge/master/pictures/configuration.png)
SSL Certificate please use the subdomain part.
![alt tag](https://raw.githubusercontent.com/programmieramt/alexa_homeegramm_bridge/master/pictures/ssl.png)
