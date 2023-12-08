import pandas as pd
from preproc import preproc_class  # đảm bảo rằng lớp này được định nghĩa trong tệp preprocessing.py

# Đọc dữ liệu từ tệp Excel
df = pd.read_excel(r"E:\DAP1\modified_train_nor_811_no_imbalance.xlsx")

# Khởi tạo lớp preproc_class với DataFrame
preprocessor = preproc_class(df=df, header='Sentence')

# Tiền xử lý văn bản
df['Sentence'] = preprocessor.preprocessing()

# Lưu DataFrame đã tiền xử lý vào một tệp mới
df.to_excel(r"E:\DAP1\train_nor_811_preprocessed_modified.xlsx", index=False)
