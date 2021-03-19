import mysql.connector


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(emp_id, collection, photo):
    print("Inserting BLOB into visionbox_collection table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='visionbox_collection',
                                             user='your_user_name',
                                             password='your_password')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO visionbox_collection
                          (id, collection, photo) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)


        # Convert data into tuple format
        insert_blob_tuple = (emp_id, collection, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into visionbox_collection table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "Eric", "D:\Python\Articles\my_SQL\images\eric_photo.png",
           "D:\Python\Articles\my_SQL\images\eric_bioData.txt")
insertBLOB(2, "Scott", "D:\Python\Articles\my_SQL\images\scott_photo.png",
           "D:\Python\Articles\my_SQL\images\scott_bioData.txt")
