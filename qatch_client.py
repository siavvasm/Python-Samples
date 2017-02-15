'''
---------------- Web API Client - QATCH ------------------------

This script is a client that uses the Web API provided by QATCH
in order to evaluate Java projects found on Github.

It demonstrates how to submit a GET request to a Web API and how
to parse a JSON response in order to retrieve useful information.

Tags: RESTfull API Client, GET Request, JSON Parser
'''

##

import json
import requests

def main():

    # Specify the URL of the GET request
    project = "https://github.com/siavvasm/testApp"
    url = "http://83.212.101.169:8080/OnlineProjectEvaluator/MessagesServlet?project=" + project

    # Send the request to QATCH and parse the data
    data = requests.get(url).text
    data = json.loads(data)

    # Print the total quality score of the project to the console
    print(data['tqi'])
    print(data['tqi']['eval'])
    print(type(data['tqi']))

    # Print the whole report
    nice_print(data)

def nice_print(data):

    # Print the overall quality score of the evaluated project
    print("")
    print("** TOTAL QUALITY SCORE: {}".format(data['tqi']['eval']))

    # Print the quality score of each characteristic
    print("")
    print("** CHARACTERISTICS **")
    for char in data["characteristics"]['characteristics']:
        print("{} : {}".format(char['name'], char['eval']))

    # Print the quality score of each property
    print("")
    print("** PROPERTIES **")
    for prop in data["properties"]['properties']:
        print("{} : {}".format(prop['name'], prop['eval']))

if __name__ == "__main__": main()



