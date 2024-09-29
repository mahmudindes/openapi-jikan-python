# AnimeReviewsAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList review URL | [optional] 
**type** | **str** | Entry type | [optional] 
**reactions** | [**MangaReviewReactions**](MangaReviewReactions.md) |  | [optional] 
**var_date** | **str** | Review created date ISO8601 | [optional] 
**review** | **str** | Review content | [optional] 
**score** | **int** | Number of user votes on the Review | [optional] 
**tags** | **List[str]** | Review tags | [optional] 
**is_spoiler** | **bool** | The review contains spoiler | [optional] 
**is_preliminary** | **bool** | The review was made before the entry was completed | [optional] 
**episodes_watched** | **int** | Number of episodes watched | [optional] 
**user** | [**UserMeta**](UserMeta.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_reviews_all_of_data import AnimeReviewsAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeReviewsAllOfData from a JSON string
anime_reviews_all_of_data_instance = AnimeReviewsAllOfData.from_json(json)
# print the JSON string representation of the object
print(AnimeReviewsAllOfData.to_json())

# convert the object into a dict
anime_reviews_all_of_data_dict = anime_reviews_all_of_data_instance.to_dict()
# create an instance of AnimeReviewsAllOfData from a dict
anime_reviews_all_of_data_form_dict = anime_reviews_all_of_data.from_dict(anime_reviews_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


