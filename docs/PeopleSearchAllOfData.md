# PeopleSearchAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**website_url** | **str** | Person&#39;s website URL | [optional] 
**images** | [**PeopleImages**](PeopleImages.md) |  | [optional] 
**name** | **str** | Name | [optional] 
**given_name** | **str** | Given Name | [optional] 
**family_name** | **str** | Family Name | [optional] 
**alternate_names** | **List[str]** | Other Names | [optional] 
**birthday** | **str** | Birthday Date ISO8601 | [optional] 
**favorites** | **int** | Number of users who have favorited this entry | [optional] 
**about** | **str** | Biography | [optional] 

## Example

```python
from jikan_openapi.models.people_search_all_of_data import PeopleSearchAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleSearchAllOfData from a JSON string
people_search_all_of_data_instance = PeopleSearchAllOfData.from_json(json)
# print the JSON string representation of the object
print(PeopleSearchAllOfData.to_json())

# convert the object into a dict
people_search_all_of_data_dict = people_search_all_of_data_instance.to_dict()
# create an instance of PeopleSearchAllOfData from a dict
people_search_all_of_data_form_dict = people_search_all_of_data.from_dict(people_search_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


