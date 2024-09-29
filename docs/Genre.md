# Genre

Genre Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**name** | **str** | Genre Name | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**count** | **int** | Genre&#39;s entry count | [optional] 

## Example

```python
from jikan_openapi.models.genre import Genre

# TODO update the JSON string below
json = "{}"
# create an instance of Genre from a JSON string
genre_instance = Genre.from_json(json)
# print the JSON string representation of the object
print(Genre.to_json())

# convert the object into a dict
genre_dict = genre_instance.to_dict()
# create an instance of Genre from a dict
genre_form_dict = genre.from_dict(genre_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


