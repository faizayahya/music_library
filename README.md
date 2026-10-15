# {{PROBLEM}} Class Music Library Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._
Properties: tracks, list of strings

```python
# EXAMPLE

class MusicLibrary:
    # User-facing properties: tracks, list of strings 
    #   name: string

    def __init__(self):
        # Parameters: none 
        # Side effects:
        #   Sets self.tracks as an empty list
        pass # No code here yet

    def add(self, track):
        # Parameters:
        # track: string represnting a single track e.g happy by pharell 
        # Returns: Nothing
        # Side-effects: Add a track to self.track
        pass # No code here yet

    def list_track(self):
        #Parameters: nothing
        # Returns: A list of tracks (string)
        # Side-effects: No
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Starts with an empty track list
"""
library = MusicLibrary()
library.list_tracks() ==> []

"""
Add track
"""
library = MusicLibrary()
library.add("Superbase")
library.list_track() ==> "Superbase"

"""
Add multiple tracks, and return in order
"""
library = MusicLibrary()
library.add("Superbase")
library.add("No Scrubs")
library.add("Thriller")
library.list_track() ==> ["Superbase", "No Scrubs", "Thriller]

"""

"""
Raises an error if there is nothing in the empty list
"""
library.add(" ")
raises error "Library can't be empty"

"""
Raises an error if it isn't a string
"""
library.add(321)
raises error "Track must be string"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
