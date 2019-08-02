# How to build a chat bot with Flask and Dialogflow

This is a demo application showing how to build a Chat bot using Flask and Dialogflow . I am using Indian government data to fetch information of temperature and rainfall of various cities in India and show it on the front-end. To show end to end integration of a chat-bot using dialogflow and flask. 


## Follow the instruction below to get this project running on your local environment

### Prerequisites

This project uses the following:

 - Python 3.6 (You should have python 3.6 or higher version installed)
 - JavaScript (jQuery)
 - Dialogflow (Create an account [here](https://dashboard.pusher.com/accounts/sign_up) or [login](https://dashboard.pusher.com/accounts/sign_in) here)
 - [Ngrok](https://ngrok.com/) ( [here](https://ngrok.com/download) )

### Settings

First of all, clone the repository to your local machine:

```
 $ git clone https://github.com/adam2411/dialogflow-chatbot.git
```


### Dialogflow

Create a Dialogflow account [here](https://console.dialogflow.com/api-client/#/login) or [login](https://console.dialogflow.com/api-client/#/login) if you have an account already.

Next,
  - Create a new agent.
  - Create an Intent.
  - Create an Entity.
  - Then enable the intent to use webhook
  - Finally, on your Dialogflow console page, click on Fulfillment then enable webhook. 

On [Google Cloud Console](https://console.cloud.google.com/apis/credentials/serviceaccountkey) get the Dialogflow API key

Then,
  - Select `Dialogflow integrations` under `Service account`. 
  - Then select `JSON` under `key type`. 
  - Next, make sure that the project id is same as in dialogflow console.
  - Finally, click on the Create button to download the your API key

Your API key will be downloaded automatically. It's a JSON file.

Next, copy the downloaded file to the root folder of the project - `chatbot`

Then, update the values in the `controllers/Constant.py` file with the correct information:
 ```
 DIALOGFLOW_KEY=*.json
 PROJECT_ID=project_id
 ```
 **Note**
   - `*.json` is the name of the JSON file you just copied to the root folder of the project.
   - To get your `project_id`, open the JSON file with your code editor, you will see a field - "project_id". The value is your `project_id`


#### Data Set

This application is using [Government Data](https://data.gov.in/resources/monthly-mean-maximum-minimum-temperature-and-total-rainfall-based-upon-1901-2000-data-3) to fetch details of a city rainfall and min and max temperature.
It is already present in app/controllers/data.json file.



### Running the App

To get the app running:

 - From a command line, cd into the project root folder - `chatbot`
 - It is recommended that you create your own virtual environment [here](https://docs.python.org/3/tutorial/venv.html) or use anaconda [here](https://www.anaconda.com/distribution/).

 - Install the dependencies:
 ```
 pip install -r requirements.txt
 ```
 - Finally run the app:
 ```
  python run.py
 ```
**Note**

If you face an error stating : 
````
ImportError: cannot import name 'resource_pb2'
````
then run
```
pip install -U googleapis-common-protos==1.5.10
```

and re run the application

Your Application is live on http://localhost:5000

