from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace

# Khởi tạo Spark Session
spark = SparkSession.builder.appName("TwitterDataProcessing").getOrCreate()

file_path = 's3://twitter-data-905418222357/twitter_data.csv'
# Đọc dữ liệu từ S3
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Hiển thị dữ liệu ban đầu
print("Dữ liệu ban đầu:")
df.show(5)

# Loại bỏ các bản ghi nếu tất cả các cột đều là null
df = df.na.drop(how='all')

# Loại bỏ các bản ghi nếu bất kỳ cột nào có giá trị null
df = df.na.drop(how='any')

# Hoặc thay thế các giá trị null bằng một giá trị khác, ví dụ như 0 cho các cột số
df = df.na.fill({'followers_count': 0, 'Following_count': 0, 'likes': 0, 'retweets': 0, 'comments': 0})

# Hiển thị dữ liệu sau khi xử lý null
print("Dữ liệu sau khi xử lý null:")
df.show(5)


# Loại bỏ các ký tự không cần thiết, ví dụ: loại bỏ dấu chấm câu trong cột 'text'
df = df.withColumn('text', regexp_replace(col('text'), '[^\w\s]', ''))

# Chuyển đổi kiểu dữ liệu nếu cần, ví dụ: chuyển đổi cột 'date' và 'account_creation_date' sang kiểu DateType
df = df.withColumn('date', col('date').cast('date'))
df = df.withColumn('account_creation_date', col('account_creation_date').cast('date'))

# Hiển thị dữ liệu sau khi làm sạch
print("Dữ liệu sau khi làm sạch:")
df.show(5)

# Đếm số lượng bản ghi sau khi xử lý
record_count = df.count()
print(f"Total records after cleaning: {record_count}")

# Lưu kết quả trở lại S3
output_path = "s3://twitter-data-905418222357/cleaned_twitter_data.csv"
df.write.csv(output_path, header=True)

# Dừng Spark Session
spark.stop()
