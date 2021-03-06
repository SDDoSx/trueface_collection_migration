import mysql.connector


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def readBLOB(emp_id, photo, collection):
    print("Reading BLOB data from visionbox_collection table")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='visionbox_collection',
                                             user='your_user_name',
                                             password='your_password')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from visionbox_collection where id = %s"""

        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Collection = ", row[1])
            image = row[2]
            print("Storing employee image on disk \n")
            write_file(image, photo)


    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


