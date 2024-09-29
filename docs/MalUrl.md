# MalUrl

Parsed URL Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**type** | **str** | Type of resource | [optional] 
**name** | **str** | Resource Name/Title | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 

## Example

```python
from jikan_openapi.models.mal_url import MalUrl

# TODO update the JSON string below
json = "{}"
# create an instance of MalUrl from a JSON string
mal_url_instance = MalUrl.from_json(json)
# print the JSON string representation of the object
print(MalUrl.to_json())

# convert the object into a dict
mal_url_dict = mal_url_instance.to_dict()
# create an instance of MalUrl from a dict
mal_url_form_dict = mal_url.from_dict(mal_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


