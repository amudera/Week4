## Phase 1 Assessment Take Home Portion: Terminal Teller API Key

### Part 1
<!-- 
* Add a column called `api_key` to your user account table in the terminal teller
project. Add an appropriate property to the model class. The column should be
VARCHAR with at least 20 characters. -->

<!-- * Write an instance method `instance.generate_api_key()` to the User account
class. This method should set the instance's `api_key` property to a random
string of at least 20 numbers or characters. For this task you do not need
to guarantee that the generated key is unique as long as it is statistically
highly unlikely for a duplicate to occur. -->

for instance
```
joe = User()
joe.generate_api_key()
print(joe.api_key)

18347038749803240929
```

* Write a unit test that creates a user, sets the api key, saves the user
and then confirms that the api key still has the same value when the user
is loaded back a second time.
<!-- 
* Update your terminal application so that when a new user is created through 
the terminal interface, an api key is generated for that user before it is saved. -->
<!-- 
* Now add a new option to the main menu of your terminal application controller
<!-- and view. Called "See API Key" or something similar. -->

<!-- It should tell a user what their key is. Keep to the code organization you have
used in your controller and views (all print / input code in the view) --> -->

<!-- ### Part 2
returns
* Write a class method of Account called `api_authenticate` this will work
similarly to the login method, only instead of a username and password, it will
take an api key value as its argument. If the key exists in the users table,
the method returns the User object that matches that row, otherwise it 
none. -->

* Write unit tests to test that:
    * The object returned is or the Account class
    <!-- * The username and password are correct -->
    * If the balance is updated and the `.save` method is called, the balance 
    will update in the database