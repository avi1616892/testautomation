from playwright.sync_api import APIRequestContext


class ChuckUtils:
    def __init__(self,api_request_context: APIRequestContext)->None:
        self.api_request_context=api_request_context

    def get_categories(self)->list:
        endpoint = "categories"
        response = self.api_request_context.get(endpoint)
        return response.json()

    def print_categories(self, categoires:list)->None:
        print("\nCategories:")
        for category in categoires:
            print(f"category is - {category}")
    def get_total_jokes_count(self,search_query:str)->int:
        endpoint = "search"
        my_params = dict(query=search_query)
        response =  self.api_request_context.get(endpoint, params=my_params)
        total=response.json()["total"]
        print(f"\nThe total of  {search_query}'s Jokes: {total}")
        return total
    def get_jokes_data(self)->dict:
        endpoint = "random"
        response = self.api_request_context.get(endpoint)
        joke_data = response.json()
        joke_url = joke_data["url"]
        joke_value = joke_data["value"]
        data={"url":joke_url,"value":joke_value,"status":response.status}
        return data

