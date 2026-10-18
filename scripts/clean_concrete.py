# Concrete compressive strength - cleaning script
# raw/Concrete_Data.xls  ->  processed/concrete_clean.csv
# Run this from inside the concrete-strength folder.

import pandas as pd

# 1) Ham veriyi oku
df = pd.read_excel('raw/Concrete_Data.xls')

# 2) Uzun sütun adlarını kısa adlarla değiştir (birimler metadata.yaml'da)
df.columns = ['cement', 'slag', 'fly_ash', 'water', 'superplasticizer',
              'coarse_agg', 'fine_agg', 'age', 'strength']

# 3) Tekrarlanan satırları sil
df = df.drop_duplicates()

# 4) Temiz veriyi kaydet
df.to_csv('processed/concrete_clean.csv', index=False)
print("Saved:", df.shape)