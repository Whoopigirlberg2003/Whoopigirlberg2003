import boto3

textract = boto3.client("textract", region_name="sa-east-1")

def extract(local_file):
    with open(local_file, "rb") as f:
        response = textract.analyze_document(
            Document={"Bytes": f.read()},
            FeatureTypes=["TABLES", "FORMS"]
        )
    return response
