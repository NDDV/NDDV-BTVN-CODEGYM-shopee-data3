#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")
df.info()

# %%
df= df.dropna()
df.info()

# %%
df

# %%
#Vẽ biểu đồ tần số số lượng shop gia nhập theo các năm.
sns.countplot(x = "join_year", data = df)
# %%
#Vẽ biểu đồ xu hướng thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt.
df_response_rate = df[['response_rate','rating_good']]
sns.lmplot(x="response_rate", y="rating_good",data = df_response_rate)

# %%
#Vẽ biểu đồ xu hướng thể hiện mối quan hệ giữa thời gian phản hồi (đơn vị giây) với số lượt khách hàng đánh giá xấu.
df_rating_bad = df[['response_time','rating_bad']]
df_rating_bad['Second']=pd.to_datetime(df_rating_bad['response_time'],format=' %H:%M:%S').dt.second
df_rating_bad = df_rating_bad[['Second','rating_bad']]
sns.lmplot(x="Second", y="rating_bad",data = df_rating_bad)
# %%
#Vẽ biểu đồ thể hiện phân bố của điểm đánh giá trung bình. 
sns.violinplot(y = "rating_normal", data=df)

# %%
#Vẽ biểu đồ tần số của cửa hàng chính thức và không chính thức. 
sns.countplot(x = "is_official_shop", data = df)

# %%
#Vẽ biểu đồ tần số của cửa hàng được xác thực với chưa xác thực. 
sns.countplot(x = "is_shopee_verified", data = df)

# %%
