# GetAnimeById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Anime**](Anime.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.get_anime_by_id200_response import GetAnimeById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnimeById200Response from a JSON string
get_anime_by_id200_response_instance = GetAnimeById200Response.from_json(json)
# print the JSON string representation of the object
print(GetAnimeById200Response.to_json())

# convert the object into a dict
get_anime_by_id200_response_dict = get_anime_by_id200_response_instance.to_dict()
# create an instance of GetAnimeById200Response from a dict
get_anime_by_id200_response_form_dict = get_anime_by_id200_response.from_dict(get_anime_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


