import pandas as pd
import csv
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetProductDetails(Action):
    def name(self) -> Text:
        return "action_get_price_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the filename of your CSV file
        filename = "Smarttv.csv"

        # Define the model name you want to search for
        model_name = tracker.get_slot('name')

        # Initialize a boolean variable to check if the model name is found
        found = False

        # Open the CSV file and read it
        with open(filename, 'r') as file:
            # Use the csv.reader method to read the file
            reader = csv.reader(file)

            # Skip the header row
            next(reader)

            # Loop through each row of the CSV file
            for row in reader:
                # Check if the model name matches the current row
                if row[3] == model_name:
                    # Print the values of other attributes in the same row
                    dispatcher.utter_message(text=f"The price for {model_name} is {row[1]}")

                    

                    # Set the found variable to True
                    found = True
                    # Exit the loop as we have found the model
                    break

        # If the model name is not found, print a message
        if not found:
            dispatcher.utter_message(text=f"No data found for {model_name}.")
            
        return []
        
class ActionGetProductDetails(Action):
    def name(self) -> Text:
        return "action_get_ratings_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the filename of your CSV file
        filename = "Smarttv.csv"

        # Define the model name you want to search for
        model_name = tracker.get_slot('name')

        # Initialize a boolean variable to check if the model name is found
        found = False

        # Open the CSV file and read it
        with open(filename, 'r') as file:
            # Use the csv.reader method to read the file
            reader = csv.reader(file)

            # Skip the header row
            next(reader)

            # Loop through each row of the CSV file
            for row in reader:
                # Check if the model name matches the current row
                if row[3] == model_name:
                    # Print the values of other attributes in the same row
                    dispatcher.utter_message(text=f"The ratings for {model_name} is {row[2]}")

                    # Set the found variable to True
                    found = True
                    # Exit the loop as we have found the model
                    break

        # If the model name is not found, print a message
        if not found:
            dispatcher.utter_message(text=f"No data found for {model_name}.")
            
        return []

class ActionGetProductDetails(Action):
    def name(self) -> Text:
        return "action_get_specifications_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define the filename of your CSV file
        filename = "Smarttv.csv"

        # Define the model name you want to search for
        model_name = tracker.get_slot('name')

        # Initialize a boolean variable to check if the model name is found
        found = False

        # Open the CSV file and read it
        with open(filename, 'r') as file:
            # Use the csv.reader method to read the file
            reader = csv.reader(file)

            # Skip the header row
            next(reader)

            # Loop through each row of the CSV file
            for row in reader:
                # Check if the model name matches the current row
                if row[3] == model_name:
                    # Print the values of other attributes in the same row
                    dispatcher.utter_message(text=f"The supported apps for {model_name} are {row[4]}, it has a {row[7]} {row[8]} display, {row[9]} storage memory, {row[10]} RAM storage, {row[12]} processor, and supports {row[13]} resolution.")

                    # Set the found variable to True
                    found = True
                    # Exit the loop as we have found the model
                    break

        # If the model name is not found, print a message
        if not found:
            dispatcher.utter_message(text=f"No data found for {model_name}.")
            
        return []

