# UserClubsAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**name** | **str** | Club Name | [optional] 
**url** | **str** | Club URL | [optional] 

## Example

```python
from jikan_openapi.models.user_clubs_all_of_data import UserClubsAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of UserClubsAllOfData from a JSON string
user_clubs_all_of_data_instance = UserClubsAllOfData.from_json(json)
# print the JSON string representation of the object
print(UserClubsAllOfData.to_json())

# convert the object into a dict
user_clubs_all_of_data_dict = user_clubs_all_of_data_instance.to_dict()
# create an instance of UserClubsAllOfData from a dict
user_clubs_all_of_data_form_dict = user_clubs_all_of_data.from_dict(user_clubs_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


