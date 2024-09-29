# MalUrl2

Parsed URL Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**type** | **str** | Type of resource | [optional] 
**title** | **str** | Resource Name/Title | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 

## Example

```python
from jikan_openapi.models.mal_url2 import MalUrl2

# TODO update the JSON string below
json = "{}"
# create an instance of MalUrl2 from a JSON string
mal_url2_instance = MalUrl2.from_json(json)
# print the JSON string representation of the object
print(MalUrl2.to_json())

# convert the object into a dict
mal_url2_dict = mal_url2_instance.to_dict()
# create an instance of MalUrl2 from a dict
mal_url2_form_dict = mal_url2.from_dict(mal_url2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


