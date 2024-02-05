![AirBnB LOGO](https://camo.githubusercontent.com/0abfd1a3534470d279dd6eaca57e0b4b81e23fb77afd81483d470c2f63ab51d3/68747470733a2f2f692e696d6775722e636f6d2f4d5171334142632e706e67)

AirBnB clone - The console

• create your data model

• manage (create, update, destroy, etc) objects via a console / command interpreter

• store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. 
This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. 
This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later,
you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.
