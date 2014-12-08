#TwySearch
=========

##About
TwySearch is a graphical user interface for accessing the Twitter Search API.

##Keyword Options
| Operator |	Finds tweets… |
|__________|________________|
| watching now	| containing both “watching” and “now”. This is the default operator. |
| “happy hour” |	containing the exact phrase “happy hour”. |
| love OR hate |	containing either “love” or “hate” (or both). |
| beer -root |	containing “beer” but not “root”. |
| #haiku |	containing the hashtag “haiku”. |
| from:alexiskold |	sent from person “alexiskold”. |
| to:techcrunch |	sent to person “techcrunch”. |
| @mashable |	referencing person “mashable”. |
| superhero | since:2010-12-27	containing “superhero” and sent since date “2010-12-27” (year-month-day). |
| ftw until:2010-12-27 |	containing “ftw” and sent before the date “2010-12-27”. |
| movie -scary :)	| containing “movie”, but not “scary”, and with a positive attitude. |
| flight :(	| containing “flight” and with a negative attitude. |
| traffic ?	| containing “traffic” and asking a question. |
| hilarious filter:links	| containing “hilarious” and linking to URL. |
| news source:twitterfeed	| containing “news” and entered via TwitterFeed |

##Options
* Keyword is the word you wish to search for.
* When saving a file you can choose to have it save as a .tsv (Tab Separated Value) or .json (native response format)
* 

##Dependencies
* Written in Python 3.4, probably works on 3.X
* Requires installing Twython (pip install twython)

##TO DO
* Package dependencies
* Expand error handling and saftey rails
* Provide exe from py2exe for easy of use on Windows


Further descriptions of what each parameter can take can be found here:

https://dev.twitter.com/rest/reference/get/search/tweets

Get your application credentials here to fill out the auth.json file:

https://dev.twitter.com/oauth/application-only

Default output is .json but you can manually save the file as .tsv
