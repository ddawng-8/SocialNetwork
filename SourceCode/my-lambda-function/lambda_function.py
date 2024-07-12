import boto3
import joblib
import json
import os

# Khởi tạo S3 client
s3 = boto3.client('s3')

# Định nghĩa biến toàn cục để lưu trữ mô hình sau khi tải từ S3
model = None

def download_model(bucket, key):
    global model
    if model is None:
        s3.download_file(bucket, key, '/tmp/predictShareModel.joblib')
        model = joblib.load('/tmp/predictShareModel.joblib')

def lambda_handler(event, context):
    # Định nghĩa bucket và key cho mô hình
    bucket = 'twitter-data-905418222357'
    key = 'predictShareModel.joblib'
    
    # Tải mô hình nếu chưa tải
    download_model(bucket, key)
    
    # Nhận dữ liệu đầu vào từ event
    input_data = json.loads(event['body'])
    
    # Chuẩn bị dữ liệu để dự đoán
    features = input_data['features']
    
    # Thực hiện dự đoán
    prediction = model.predict([features]).tolist()
    
    # Trả kết quả dự đoán
    return {
        'statusCode': 200,
        'body': json.dumps({prediction})
    }
