# PersonMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**PeopleImages**](PeopleImages.md) |  | [optional] 
**name** | **str** | Entry name | [optional] 

## Example

```python
from jikan_openapi.models.person_meta import PersonMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PersonMeta from a JSON string
person_meta_instance = PersonMeta.from_json(json)
# print the JSON string representation of the object
print(PersonMeta.to_json())

# convert the object into a dict
person_meta_dict = person_meta_instance.to_dict()
# create an instance of PersonMeta from a dict
person_meta_form_dict = person_meta.from_dict(person_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


