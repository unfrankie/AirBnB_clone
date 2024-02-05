![AirBnB LOGO](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240205T161305Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=10967ace3b71b589adca1b1e0eee17c4043ff278c7bd834db6ba5d5b9e89bd80)

AirBnB clone - The console

▬ create your data model
▬ manage (create, update, destroy, etc) objects via a console / command interpreter
▬ store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
