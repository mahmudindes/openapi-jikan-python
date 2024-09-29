# PersonAnimeDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | Person&#39;s position | [optional] 
**anime** | [**AnimeMeta**](AnimeMeta.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.person_anime_data_inner import PersonAnimeDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonAnimeDataInner from a JSON string
person_anime_data_inner_instance = PersonAnimeDataInner.from_json(json)
# print the JSON string representation of the object
print(PersonAnimeDataInner.to_json())

# convert the object into a dict
person_anime_data_inner_dict = person_anime_data_inner_instance.to_dict()
# create an instance of PersonAnimeDataInner from a dict
person_anime_data_inner_form_dict = person_anime_data_inner.from_dict(person_anime_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


