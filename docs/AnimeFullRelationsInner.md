# AnimeFullRelationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** | Relation type | [optional] 
**entry** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_full_relations_inner import AnimeFullRelationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeFullRelationsInner from a JSON string
anime_full_relations_inner_instance = AnimeFullRelationsInner.from_json(json)
# print the JSON string representation of the object
print(AnimeFullRelationsInner.to_json())

# convert the object into a dict
anime_full_relations_inner_dict = anime_full_relations_inner_instance.to_dict()
# create an instance of AnimeFullRelationsInner from a dict
anime_full_relations_inner_form_dict = anime_full_relations_inner.from_dict(anime_full_relations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


