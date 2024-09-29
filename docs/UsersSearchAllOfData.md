# UsersSearchAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | MyAnimeList URL | [optional] 
**username** | **str** | MyAnimeList Username | [optional] 
**images** | [**UserImages**](UserImages.md) |  | [optional] 
**last_online** | **str** | Last Online Date ISO8601 | [optional] 

## Example

```python
from jikan_openapi.models.users_search_all_of_data import UsersSearchAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSearchAllOfData from a JSON string
users_search_all_of_data_instance = UsersSearchAllOfData.from_json(json)
# print the JSON string representation of the object
print(UsersSearchAllOfData.to_json())

# convert the object into a dict
users_search_all_of_data_dict = users_search_all_of_data_instance.to_dict()
# create an instance of UsersSearchAllOfData from a dict
users_search_all_of_data_form_dict = users_search_all_of_data.from_dict(users_search_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


