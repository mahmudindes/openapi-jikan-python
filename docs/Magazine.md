# Magazine

Magazine Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**name** | **str** | Magazine Name | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**count** | **int** | Magazine&#39;s manga count | [optional] 

## Example

```python
from jikan_openapi.models.magazine import Magazine

# TODO update the JSON string below
json = "{}"
# create an instance of Magazine from a JSON string
magazine_instance = Magazine.from_json(json)
# print the JSON string representation of the object
print(Magazine.to_json())

# convert the object into a dict
magazine_dict = magazine_instance.to_dict()
# create an instance of Magazine from a dict
magazine_form_dict = magazine.from_dict(magazine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


