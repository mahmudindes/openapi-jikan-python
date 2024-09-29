# AnimeRelations

Anime Relations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AnimeFullRelationsInner]**](AnimeFullRelationsInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_relations import AnimeRelations

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeRelations from a JSON string
anime_relations_instance = AnimeRelations.from_json(json)
# print the JSON string representation of the object
print(AnimeRelations.to_json())

# convert the object into a dict
anime_relations_dict = anime_relations_instance.to_dict()
# create an instance of AnimeRelations from a dict
anime_relations_form_dict = anime_relations.from_dict(anime_relations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


