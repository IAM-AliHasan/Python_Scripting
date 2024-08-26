import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        objects = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' not in objects:
            try:
                # Delete all versions of all objects in the bucket
                versions = s3.list_object_versions(Bucket=bucket_name)
                if 'Versions' in versions:
                    for version in versions['Versions']:
                        s3.delete_object(Bucket=bucket_name, Key=version['Key'], VersionId=version['VersionId'])
                if 'DeleteMarkers' in versions:
                    for marker in versions['DeleteMarkers']:
                        s3.delete_object(Bucket=bucket_name, Key=marker['Key'], VersionId=marker['VersionId'])
                
                # Delete the bucket
                s3.delete_bucket(Bucket=bucket_name)
                print(f"Deleted bucket: {bucket_name}")
            except Exception as e:
                print(f"Error deleting bucket {bucket_name}: {e}")
        else:
            print(f"Bucket {bucket_name} is not empty, skipping deletion.")

