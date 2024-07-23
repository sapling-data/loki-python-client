# Overview

Lists all entities, resources and directories under the given parent urn.

# Service URL

/api/urn/com/loki/core/model/webServices/list/v/(urn)?(parameters)

# Methods

* GET - executes the list

# GET - Execute a list

## URL Parameters

* urn (in parameter of URL) - the parent urn whose children are to be listed
* format - the format of the data to be returned. ex: 'format=json'
* startMarker - a marker string used to begin where the last call to the service left off. Use the nextMarker returned from the previous call to begin where it left off.
* begin - for use in paging data.  Indicates the number of the first item to be returned.
* num - the number of items to be returned
* outputView - the view to be used to load the entity data.  If not provided then a list of item objects will be returned.
* urnTypes - the types of items to be returned ('entity','resource').
* excludeDirectories - exclude any items that are a directory with no associated entity. Default is false. If false, entities, resources and urn directories are returned and so you may need to check for the existance of an entity to tell the difference between a directory and an entity.
* dataSpaceUrn - the urn for the data space to run the list on.  Example: "urn:com:domain:myApp:model:dataSpaces:default"
* maxToProcess A performance hint that limits the number of items processed when counting the total.
        Setting this parameter will help guarantee that the estimated total returned is at least as accurate as maxToProcess.
        For example, if you need to show up to 10 pages of 10 items, you can set maxToProcess to 101 in order to know how many pages you need to show and if there is a page beyond 10.
        If set to null then the underlying implementation will decide how many to process.
        Set this to zero if you do not need an estimated total.

## Response Body

The results of the query including these fields:

* results - array of results
* begin - same as the input parameter.
* startMarker - a marker string used to begin where the last call to the service left off. Use the nextMarker returned from the previous call to begin where it left off.
* numRequested - same as the input parameter.
* nextMarker - a string that marks where to start to get the next set of results past numResults.
            The nextMarker can be used as the startMarker for the next call to the list api.
* totalFound - an estimate of the total including the items skipped by beginIndex as well as items beyond numResults, but not those skipped by startMarker.
            The total can be used along with beginIndex and numResults for paging and that is why it counts items before and after these parameters.
            The startMarker is independent of the beginIndex/numResults paging and is used as a fast index into large lists without the overhead of counting the total. This is why the total does not include items before startMarker.

## Required Permissions

* List Data Access (urn:com:loki:core:model:actions:list) - on the entity parent being listed
* Read Data Access (urn:com:loki:core:model:actions:read) - on each entity found if outputView is specified. Entities will be omitted from results if the permission test fails.

