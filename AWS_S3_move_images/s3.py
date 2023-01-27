import boto3
# we can create the simple source code for this project using AWS lambda funcition.
# when we create the lambda function, we should give the permission to the lambda function for 
# the source and target buckets so that our function can access and operate with those buckets.

#checking image is trasparency.
def has_transparency(img):
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

    return False


#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='Your Access Key ID',
aws_secret_access_key='Your Secret access key'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

srcbucket = s3.Bucket('your_source_bucket_name')

destbucket = s3.Bucket('your_target_bucket_name')

# Iterate All Objects in Your S3 Bucket Over the for Loop
for file in srcbucket.objects.all():
    
    #Create a Soucre Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
    copy_source = {
    'Bucket': 'your_source_bucket_name',
    'Key': file.key
    }
    if has_transparency:
        destbucket.copy(copy_source, file.key)
    
    print(file.key +'- File Copied')