# RandomDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**PeopleImages**](PeopleImages.md) |  | [optional] 
**trailer** | [**TrailerBase**](TrailerBase.md) |  | [optional] 
**approved** | **bool** | Whether the entry is pending approval on MAL or not | [optional] 
**titles** | [**List[Title]**](Title.md) | All Titles | [optional] 
**title** | **str** | Title | [optional] 
**title_english** | **str** | English Title | [optional] 
**title_japanese** | **str** | Japanese Title | [optional] 
**title_synonyms** | **List[str]** | Other Titles | [optional] 
**type** | **str** | Anime Type | [optional] 
**source** | **str** | Original Material/Source adapted from | [optional] 
**episodes** | **int** | Episode count | [optional] 
**status** | **str** | Publishing status | [optional] 
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
**chapters** | **int** | Chapter count | [optional] 
**volumes** | **int** | Volume count | [optional] 
**publishing** | **bool** | Publishing boolean | [optional] 
**published** | [**Daterange**](Daterange.md) |  | [optional] 
**authors** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**serializations** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**name** | **str** | Name | [optional] 
**name_kanji** | **str** | Name | [optional] 
**nicknames** | **List[str]** | Other Names | [optional] 
**about** | **str** | Biography | [optional] 
**website_url** | **str** | Person&#39;s website URL | [optional] 
**given_name** | **str** | Given Name | [optional] 
**family_name** | **str** | Family Name | [optional] 
**alternate_names** | **List[str]** | Other Names | [optional] 
**birthday** | **str** | Birthday Date ISO8601 | [optional] 

## Example

```python
from jikan_openapi.models.random_data_inner import RandomDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of RandomDataInner from a JSON string
random_data_inner_instance = RandomDataInner.from_json(json)
# print the JSON string representation of the object
print(RandomDataInner.to_json())

# convert the object into a dict
random_data_inner_dict = random_data_inner_instance.to_dict()
# create an instance of RandomDataInner from a dict
random_data_inner_form_dict = random_data_inner.from_dict(random_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


