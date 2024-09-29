# Relation

Related resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** | Relation type | [optional] 
**entry** | [**List[MalUrl]**](MalUrl.md) | Related entries | [optional] 

## Example

```python
from jikan_openapi.models.relation import Relation

# TODO update the JSON string below
json = "{}"
# create an instance of Relation from a JSON string
relation_instance = Relation.from_json(json)
# print the JSON string representation of the object
print(Relation.to_json())

# convert the object into a dict
relation_dict = relation_instance.to_dict()
# create an instance of Relation from a dict
relation_form_dict = relation.from_dict(relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


