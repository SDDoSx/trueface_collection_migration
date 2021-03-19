# trueface_collection_migration
A base example on building a database that contains images and identities for the purpose of migrating and re-enrolling collections from an older to a newer version of the Visionbox (with different models)

# Setup
```
pip install -r requirements.txt
```
Setup and start a MYSQL server and create this table:
```
CREATE TABLE `visionbox_collection` ( `id` INT NOT NULL , `collection` TEXT NOT NULL , `photo` BLOB NOT NULL , PRIMARY KEY (`id`))
```
Note that in my example I'm using INT as identifiers, modify it to your use case

# What it does
This repository contains 3 python files, each does a specific action to help migrating a collection from an old Version of the Visionbox to a new one
* database_inserter.py
  * This file will help put into a database all of your pictures from a specific folder while also assigning an ID and Collection. The program converts the picture to binary data before inserting it to the database. You can use this method along with a recursive loop to add all of your pictures to the database in an efficient way while also assigning the collection name.
  * Why use it? This method will allow you to store your collection and binary data into a MYSQL database, it can serve you later and ease collection migration no matter what other version you decide to use.
  * How to use it? Calling the method insertBLOB, will requiere you to pass the ID, Collection name, and folder location of the picture + picture name
* database_retriever.py
  * This file will help retrieve the picture from the databse, basically it converts the binary data and outputs the real picture in a desired folder. You can also use this method along with a recursive loop to extract all the components of the database.
  * Why use it? This method will allow you to retrieve all your collection into one place of your choice (After having the collection inserted on the db using the inserter method) And this is the key of facilitating migration from one version to another.
  * How to use it? Calling method readBLOB, will require you to pass the ID, and folder desired location + desired picture naming
* collection_enroller.py
  * I created this script as an example how I would use my saved BLOB collection on the MYSQL db and retrieve from it the identities, then enroll them using a recursive loop to the latest Visionbox
