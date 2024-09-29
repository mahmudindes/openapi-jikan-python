# Club

Club Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**name** | **str** | Club name | [optional] 
**url** | **str** | Club URL | [optional] 
**images** | [**CommonImages**](CommonImages.md) |  | [optional] 
**members** | **int** | Number of club members | [optional] 
**category** | **str** | Club Category | [optional] 
**created** | **str** | Date Created ISO8601 | [optional] 
**access** | **str** | Club access | [optional] 

## Example

```python
from jikan_openapi.models.club import Club

# TODO update the JSON string below
json = "{}"
# create an instance of Club from a JSON string
club_instance = Club.from_json(json)
# print the JSON string representation of the object
print(Club.to_json())

# convert the object into a dict
club_dict = club_instance.to_dict()
# create an instance of Club from a dict
club_form_dict = club.from_dict(club_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


