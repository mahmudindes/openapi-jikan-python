# ClubRelationsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**manga** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**characters** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.club_relations_data import ClubRelationsData

# TODO update the JSON string below
json = "{}"
# create an instance of ClubRelationsData from a JSON string
club_relations_data_instance = ClubRelationsData.from_json(json)
# print the JSON string representation of the object
print(ClubRelationsData.to_json())

# convert the object into a dict
club_relations_data_dict = club_relations_data_instance.to_dict()
# create an instance of ClubRelationsData from a dict
club_relations_data_form_dict = club_relations_data.from_dict(club_relations_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


