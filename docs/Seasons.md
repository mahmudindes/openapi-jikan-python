# Seasons

List of available seasons

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SeasonsDataInner]**](SeasonsDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.seasons import Seasons

# TODO update the JSON string below
json = "{}"
# create an instance of Seasons from a JSON string
seasons_instance = Seasons.from_json(json)
# print the JSON string representation of the object
print(Seasons.to_json())

# convert the object into a dict
seasons_dict = seasons_instance.to_dict()
# create an instance of Seasons from a dict
seasons_form_dict = seasons.from_dict(seasons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


