import boto
import boto.s3.connection
import sys

accesskey = 'azhoulin'
secretkey = 'szhoulin'

conn = boto.connect_s3(
        aws_access_key_id = accesskey,
        aws_secret_access_key = secretkey,
        host = sys.argv[1],
        is_secure=False,               # uncommmnt if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
		
if(sys.argv[2]=='listbucket'):
    for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )
elif(sys.argv[2]=='listobject'):
    bucket = conn.get_bucket(sys.argv[3])
    for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
            name = key.name,
            size = key.size,
            modified = key.last_modified,
            )
elif(sys.argv[2]=='delbucket'):
    bucket = conn.get_bucket(sys.argv[3])
    for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
            name = key.name,
            size = key.size,
            modified = key.last_modified,
            )
        bucket.delete_key(key.name)		
    bucket = conn.delete_bucket(sys.argv[3])
    print"======================"	
    for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )
elif(sys.argv[2]=='delobject'):
    bucket = conn.get_bucket(sys.argv[3])
    bucket.delete_key(sys.argv[4])
    print"Delete object" + sys.argv[4]
elif(sys.argv[2]=='createbucket'):
    bucket = conn.create_bucket(sys.argv[3])
    for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )
