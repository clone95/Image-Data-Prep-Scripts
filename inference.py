import json
import numpy as np
import boto3
import os

img_dir = "./scraper/raw/bmw_ext/"
endpoint_name = "giacomo-output-ep--2019-05-30-12-06-45"
runtime = boto3.Session().client(service_name='runtime.sagemaker')


for file in os.listdir(img_dir): 
      
    with open(img_dir + file, 'rb') as f:
        payload = f.read()
        payload = bytearray(payload)
    response = runtime.invoke_endpoint(EndpointName=endpoint_name, 
                                    ContentType='application/x-image', 
                                    Body=payload)
    result = response['Body'].read()
    # result will be in json format and convert it to ndarray
    result = json.loads(result)
    # the result will output the probabilities for all classes
    # find the class with maximum probability and print the class index
    index = np.argmax(result)
    object_categories = ["exteriors", "interiors"]
    print("Result: label - " + object_categories[index] + ", probability - " + str(result[index]))  