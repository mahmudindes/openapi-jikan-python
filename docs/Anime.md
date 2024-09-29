# Anime

Anime Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**AnimeImages**](AnimeImages.md) |  | [optional] 
**trailer** | [**TrailerBase**](TrailerBase.md) |  | [optional] 
**approved** | **bool** | Whether the entry is pending approval on MAL or not | [optional] 
**titles** | [**List[Title]**](Title.md) | All titles | [optional] 
**title** | **str** | Title | [optional] 
**title_english** | **str** | English Title | [optional] 
**title_japanese** | **str** | Japanese Title | [optional] 
**title_synonyms** | **List[str]** | Other Titles | [optional] 
**type** | **str** | Anime Type | [optional] 
**source** | **str** | Original Material/Source adapted from | [optional] 
**episodes** | **int** | Episode count | [optional] 
**status** | **str** | Airing status | [optional] 
**airing** | **bool** | Airing boolean | [optional] 
**aired** | [**Daterange**](Daterange.md) |  | [optional] 
**duration** | **str** | Parsed raw duration | [optional] 
**rating** | **str** | Anime audience rating | [optional] 
**score** | **float** | Score | [optional] 
**scored_by** | **int** | Number of users | [optional] 
**rank** | **int** | Ranking | [optional] 
**popularity** | **int** | Popularity | [optional] 
**members** | **int** | Number of users who have added this entry to their list | [optional] 
**favorites** | **int** | Number of users who have favorited this entry | [optional] 
**synopsis** | **str** | Synopsis | [optional] 
**background** | **str** | Background | [optional] 
**season** | **str** | Season | [optional] 
**year** | **int** | Year | [optional] 
**broadcast** | [**Broadcast**](Broadcast.md) |  | [optional] 
**producers** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**licensors** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**studios** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**genres** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**explicit_genres** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**themes** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**demographics** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime import Anime

# TODO update the JSON string below
json = "{}"
# create an instance of Anime from a JSON string
anime_instance = Anime.from_json(json)
# print the JSON string representation of the object
print(Anime.to_json())

# convert the object into a dict
anime_dict = anime_instance.to_dict()
# create an instance of Anime from a dict
anime_form_dict = anime.from_dict(anime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


