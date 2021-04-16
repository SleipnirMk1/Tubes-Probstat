#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pylab 
import scipy.stats as stats
import math

print("Anggota: ")
print("Ilyasa Salafi Putra Jamal 13519023")
print("Mahameru Ds 13519014")

df = pd.read_csv("Gandum.csv")


# In[2]:


df.describe()


# In[3]:


print("Skewness: ")
df.skew()


# In[4]:


print("Variance: ")
df.var()


# In[5]:


print("Kurtosis: ")
df.kurt()


# In[6]:


print("Modus: ")
print("Beberapa data memiliki 500 modus karena setiap datanya unik")
df.mode()


# In[7]:


print("Interquartile Range (IQR):")
val_list = df["Daerah"].values.tolist()
iqr = stats.iqr(val_list)
print("Daerah\t\t: ", iqr)
val_list = df["SumbuUtama"].values.tolist()
iqr = stats.iqr(val_list)
print("Sumbu Utama\t: ", iqr)
val_list = df["SumbuKecil"].values.tolist()
iqr = stats.iqr(val_list)
print("Sumbu Kecil\t: ", iqr)
val_list = df["Keunikan"].values.tolist()
iqr = stats.iqr(val_list)
print("Keunikan\t: ", iqr)
val_list = df["AreaBulatan"].values.tolist()
iqr = stats.iqr(val_list)
print("Area Bulatan\t: ", iqr)
val_list = df["Diameter"].values.tolist()
iqr = stats.iqr(val_list)
print("Diameter\t: ", iqr)
val_list = df["KadarAir"].values.tolist()
iqr = stats.iqr(val_list)
print("Kadar Air\t: ", iqr)
val_list = df["Keliling"].values.tolist()
iqr = stats.iqr(val_list)
print("Keliling\t: ", iqr)
val_list = df["Bulatan"].values.tolist()
iqr = stats.iqr(val_list)
print("Bulatan\t\t: ", iqr)
val_list = df["Ransum"].values.tolist()
iqr = stats.iqr(val_list)
print("Ransum\t\t: ", iqr)
val_list = df["Kelas"].values.tolist()
iqr = stats.iqr(val_list)
print("Kelas\t\t: ", iqr)


# In[8]:


df.hist(column="Daerah")


# In[9]:


df.boxplot(column="Daerah")


# In[10]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Daerah"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Gagal menolak, perlu dilakukan tes Shapiro-Wilk")


# In[11]:


print("Pengujian normal dengan tes Shapiro-Wilk")
val_list = df["Daerah"].values.tolist()
tset, pval = stats.shapiro(val_list)
print("Pval: ", pval)
if pval > 0.05:
    print("Pval lebih besar dari 0.05, Kesimpulan: Berdistribusi normal")
else:
    print("Pval lebih kecil dari 0.05, Kesimpulan: Tidak berdistribusi normal") #Ans


# In[12]:


df.hist(column="SumbuUtama")


# In[13]:


df.boxplot(column="SumbuUtama")


# In[14]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["SumbuUtama"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Gagal menolak, perlu dilakukan tes Shapiro-Wilk")


# In[15]:


print("Pengujian normal dengan tes Shapiro-Wilk")
val_list = df["SumbuUtama"].values.tolist()
tset, pval = stats.shapiro(val_list)
print("Pval: ", pval)
if pval > 0.05:
    print("Pval lebih besar dari 0.05, Kesimpulan: Berdistribusi normal")
else:
    print("Pval lebih kecil dari 0.05, Kesimpulan: Tidak berdistribusi normal")#Ans


# In[16]:


df.hist(column="SumbuKecil")


# In[17]:


df.boxplot(column="SumbuKecil")


# In[18]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["SumbuKecil"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Gagal menolak, perlu dilakukan tes Shapiro-Wilk")


# In[19]:


print("Pengujian normal dengan tes Shapiro-Wilk")
val_list = df["SumbuKecil"].values.tolist()
tset, pval = stats.shapiro(val_list)
print("Pval: ", pval)
if pval > 0.05:
    print("Pval lebih besar dari 0.05, Kesimpulan: Berdistribusi normal") #Ans
else:
    print("Pval lebih kecil dari 0.05, Kesimpulan: Tidak berdistribusi normal")


# In[20]:


df.hist(column="Keunikan")


# In[21]:


df.boxplot(column="Keunikan")


# In[22]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Keunikan"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal")


# In[23]:


df.hist(column="AreaBulatan")


# In[24]:


df.boxplot(column="AreaBulatan")


# In[25]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["AreaBulatan"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Gagal menolak, perlu dilakukan tes Shapiro-Wilk")


# In[26]:


print("Pengujian normal dengan tes Shapiro-Wilk")
val_list = df["AreaBulatan"].values.tolist()
tset, pval = stats.shapiro(val_list)
print("Pval: ", pval)
if pval > 0.05:
    print("Pval lebih besar dari 0.05, Kesimpulan: Berdistribusi normal")
else:
    print("Pval lebih kecil dari 0.05, Kesimpulan: Tidak berdistribusi normal") #Ans


# In[27]:


df.hist(column="Diameter")


# In[28]:


df.boxplot(column="Diameter")


# In[29]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Diameter"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Gagal menolak, perlu dilakukan tes Shapiro-Wilk")


# In[30]:


print("Pengujian normal dengan tes Shapiro-Wilk")
val_list = df["Diameter"].values.tolist()
tset, pval = stats.shapiro(val_list)
print("Pval: ", pval)
if pval > 0.05:
    print("Pval lebih besar dari 0.05, Kesimpulan: Berdistribusi normal") #Ans
else:
    print("Pval lebih kecil dari 0.05, Kesimpulan: Tidak berdistribusi normal")


# In[31]:


df.hist(column="KadarAir")


# In[32]:


df.boxplot(column="KadarAir")


# In[33]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["KadarAir"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal")


# In[34]:


df.hist(column="Keliling")


# In[35]:


df.boxplot(column="Keliling")


# In[36]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Keliling"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Gagal menolak, perlu dilakukan tes Shapiro-Wilk")


# In[37]:


print("Pengujian normal dengan tes Shapiro-Wilk")
val_list = df["Keliling"].values.tolist()
tset, pval = stats.shapiro(val_list)
print("Pval: ", pval)
if pval > 0.05:
    print("Pval lebih besar dari 0.05, Kesimpulan: Berdistribusi normal") 
else:
    print("Pval lebih kecil dari 0.05, Kesimpulan: Tidak berdistribusi normal") #Ans


# In[38]:


df.hist(column="Bulatan")


# In[39]:


df.boxplot(column="Bulatan")


# In[40]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Bulatan"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Gagal menolak, perlu dilakukan tes Shapiro-Wilk")


# In[41]:


print("Pengujian normal dengan tes Shapiro-Wilk")
val_list = df["Bulatan"].values.tolist()
tset, pval = stats.shapiro(val_list)
print("Pval: ", pval)
if pval > 0.05:
    print("Pval lebih besar dari 0.05, Kesimpulan: Berdistribusi normal") 
else:
    print("Pval lebih kecil dari 0.05, Kesimpulan: Tidak berdistribusi normal")#Ans


# In[42]:


df.hist(column="Ransum")


# In[43]:


df.boxplot(column="Ransum")


# In[44]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Ransum"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal")


# In[45]:


df.hist(column="Kelas")


# In[46]:


df.boxplot(column="Kelas")


# In[47]:


print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Kelas"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal")


# In[48]:


#Korelasi
#Target adalah kolom "Kelas", yang memiliki nilai 1 atau 2
print("Correlation")


# In[49]:


#Kelas-Daerah
df.plot.scatter("Kelas", "Daerah")


# In[50]:


print("Korelasi negatif kuat (0.6-0.79)")
print("Nilai korelasi: ")
df["Kelas"].corr(df["Daerah"])


# In[51]:


#Kelas-SumbuUtama
df.plot.scatter("Kelas", "SumbuUtama")


# In[52]:


print("Korelasi negatif kuat (0.6-0.79)")
print("Nilai korelasi: ")
df["Kelas"].corr(df["SumbuUtama"])


# In[53]:


#Kelas-SumbuKecil
df.plot.scatter("Kelas", "SumbuKecil")


# In[54]:


print("Korelasi negatif sangat lemah (0.0-0.19)")
print("Nilai korelasi: ")
df["Kelas"].corr(df["SumbuKecil"])


# In[55]:


#Kelas-Keunikan
df.plot.scatter("Kelas", "Keunikan")


# In[56]:


print("Korelasi negatif kuat (0.6-0.79)")
print("Nilai korelasi: ")
df["Kelas"].corr(df["Keunikan"])


# In[57]:


#Kelas-AreaBulatan
df.plot.scatter("Kelas", "AreaBulatan")


# In[58]:


print("Korelasi negatif kuat (0.6-0.79)")
print("Nilai korelasi: ")
df["Kelas"].corr(df["AreaBulatan"])


# In[59]:


#Kelas-Diameter
df.plot.scatter("Kelas", "Diameter")


# In[60]:


print("Korelasi negatif kuat (0.6-0.79)")
print("Nilai korelasi: ")
df["Kelas"].corr(df["Diameter"])


# In[61]:


#Kelas-KadarAir
df.plot.scatter("Kelas", "KadarAir")


# In[62]:


print("Korelasi positif sangat lemah (0.0-0.19)")
print("Nilai korelasi: ")
df["Kelas"].corr(df["KadarAir"])


# In[63]:


#Kelas-Keliling
df.plot.scatter("Kelas", "Keliling")


# In[64]:


print("Korelasi negatif kuat (0.6-0.79)")
print("Nilai korelasi: ")
df["Kelas"].corr(df["Keliling"])


# In[65]:


#Kelas-Bulatan
df.plot.scatter("Kelas", "Bulatan")


# In[66]:


print("Korelasi positif sedang (0.4-0.59)")
print("Nilai korelasi: ")
df["Kelas"].corr(df["Bulatan"])


# In[67]:


#Kelas-Ransum
df.plot.scatter("Kelas", "Ransum")


# In[68]:


print("Korelasi negatif sangat kuat (0.8-1.0)")
print("Nilai korelasi: ")
df["Kelas"].corr(df["Ransum"])


# In[69]:


print("Tes Hipotesis 1 Sampel")
print("4.a: Nilai rata-rata Daerah di atas 4700?")
print("h0: rata-rata = 4700")
print("h1: rata-rata > 4700")
print("alpha = 0.05")
print("Tes yang digunakan: One Sample One-Tailed Normal test")
print("Daerah kritis: Z > 1.645")
val_list = df["Daerah"].values.tolist()
tset, pval = stats.ttest_1samp(val_list, 4700)
print("Nilai P: ", pval)
# tes yang diperlukan one-tailed, sementara fungsi menghitung two-ended, sehingga P daerah kritis perlu 2x lipat
# note: keberadaan tail kedua dinilai tidak memengaruhi hasil
if pval < 0.10: 
   print("Pvalue lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga rata-rata diatas 4700")
else:
  print("Pvalue lebih besar dari alpha, Hipotesis null diterima, sehingga rata-rata 4700")
df.boxplot(column="Daerah")


# In[70]:


print("4.b: Nilai Rata-rata Sumbu Utama tidak sama dengan 116?")
print("h0: rata-rata = 116")
print("h1: rata-rata =/= 116")
print("alpha = 0.05")
print("Tes yang digunakan: One Sample Two-Tailed Normal test")
print("Daerah kritis: Z > 1.96 atau Z < -1.96")
val_list = df["SumbuUtama"].values.tolist()
tset, pval = stats.ttest_1samp(val_list, 116)
print("Nilai P: ", pval)
if pval < 0.05:
   print("Pvalue lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga rata-rata bukan 116")
else:
  print("Pvalue lebih besar dari alpha, Hipotesis null diterima, sehingga rata-rata 116")
df.boxplot(column="SumbuUtama")


# In[71]:


print("4c. Nilai Rata-rata 20 baris pertama kolom Sumbu Kecil bukan 50?")
print("h0: rata-rata = 50")
print("h1: rata-rata =/= 50")
print("alpha = 0.05")
print("Tes yang digunakan: One Sample Two-Tailed Normal test")
print("Daerah kritis: Z > 1.96 atau Z < -1.96")
val_list = df["SumbuKecil"].head(20).values.tolist()
tset, pval = stats.ttest_1samp(val_list, 50)
print("Nilai P: ", pval)
if pval < 0.05:
   print("Pvalue lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga rata-rata bukan 50")
else:
  print("Pvalue lebih besar dari alpha, Hipotesis null diterima, sehingga rata-rata 50")
df.boxplot(column="SumbuKecil")


# In[72]:


print("4d. Proporsi nilai Diameter yang lebih dari 85, adalah tidak sama dengan 15% ?")
print("h0: p = 0.15")
print("h1: p =/= 0.15")
print("alpha = 0.05")
print("Tes yang digunakan: Two-Tailed Binomial Test")
print("Daerah kritis: Z > 1.96 atau Z < -1.96")
dia_above_85 = len(df[df['Diameter'] > 85])
pval = stats.binom_test(dia_above_85, len(df), 0.15)
print("Nilai P: ", pval)
if pval < 0.05:
   print("Pvalue lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga proporsi bukan 15%")
else:
  print("Pvalue lebih besar dari alpha, Hipotesis null diterima, sehingga proporsi 15%")
df.boxplot(column="Diameter")


# In[73]:


print("4e. Proporsi nilai Keliling yang kurang dari 100, adalah kurang dari 5% ?")
print("h0: p = 0.05")
print("h1: p < 0.05")
print("alpha = 0.05")
print("Tes yang digunakan: One-Tailed Binomial Test")
print("Daerah kritis: Z < -1.645")
kel_below_100 = len(df[df['Keliling'] < 100])
print(kel_below_100)
pval = stats.binom_test(kel_below_100, len(df), 0.05)
print("Nilai P: ", pval)
# tes yang diperlukan one-tailed, sementara fungsi menghitung two-ended, sehingga P daerah kritis perlu 2x lipat
# note: keberadaan tail kedua dinilai tidak memengaruhi hasil
if pval < 0.10:
   print("Pvalue lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga proporsi bukan 5%")
else:
  print("Pvalue lebih besar dari alpha, Hipotesis null diterima, sehingga proporsi 5%")
df.boxplot(column="Keliling")


# In[74]:


# 5.a
print("5a. Data kolom AreaBulatan dibagi 2 sama rata: bagian awal dan bagian akhir kolom. Benarkah rata-rata kedua bagian tersebut sama?")
df_length = int(len(df)/2)
sample1 = df[df_length:]["AreaBulatan"]
sample2 = df[:df_length]["AreaBulatan"]
print("1. h0 : meanSample1 = meanSample2")
print("2. h1 : meanSample1 =/= meanSample2")
print("3. alpha = 0.05")
print("4. Two-Sample Two-Tailed Normal Test")
print("Daerah kritis: Z > 1.96 atau Z < -1.96")
ttest,pval = stats.ttest_ind(sample1, sample2)
print("5. Nilai P: ", pval)
if pval < 0.05:
   print("6. P lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga rata-rata kedua bagian tidak sama")
else:
  print("6. P lebih besar dari alpha, Hipotesis null diterima, sehingga rata-rata kedua bagian tidak sama")
df.boxplot(column="AreaBulatan")


# In[75]:


#5.b
print("5b. Data kolom Kadar Air dibagi 2 sama rata: bagian awal dan bagian akhir kolom. Benarkah rata-rata bagian awal lebih besar dari pada bagian akhir sebesar 0.2?")
df_length = int(len(df)/2)
sample1 = df[df_length:]["KadarAir"]
sample2 = df[:df_length]["KadarAir"]
print("1. h0 : meanSample1-meanSample2 = 2")
print("2. h1 : meanSample1-meanSample2 > 2")
print("3. alpha = 0.05")
print("4. Two-Sample Two-Tailed Normal Test")
print("Daerah kritis: Z > 1.645")
ttest,pval = stats.ttest_ind(sample1, sample2)
print("5. Nilai P: ", pval)
if pval < 0.05:
   print("6. P lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga perbedaan rata-rata kedua bagian sama dengan dua")
else:
  print("6. P lebih besar dari alpha, Hipotesis null diterima, sehingga perbedaan rata-rata kedua bagian tidak sama dengan dua")
df.boxplot(column="KadarAir")


# In[76]:


# 5.c
print("5c. Rata-rata 20 baris pertama kolom Bulatan sama dengan 20 baris terakhirnya?")
sample1 = df[:20]["Bulatan"]
sample2 = df[-20:]["Bulatan"]
print("1. h0 : meanSample1 = meanSample2")
print("2. h1 : meanSample1 =/= meanSample2")
print("3. alpha = 0.05")
print("4. Two-Sample Two-Tailed Normal Test")
print("Daerah kritis: Z > 1.96 atau Z < -1.96")
ttest,pval = stats.ttest_ind(sample1, sample2)
print("5. Nilai P: ", pval)
if pval < 0.05:
   print("6. P lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga rata-rata kedua bagian tidak sama")
else:
  print("6. P lebih besar dari alpha, Hipotesis null diterima, sehingga rata-rata kedua bagian sama")
df.boxplot(column="Bulatan")


# In[77]:


#5.d
print("5d. Proporsi nilai bagian awal Ransum yang lebih dari 2, adalah lebih besar daripada, proporsi nilai yang sama di bagian akhir Ransum?")
data = df[df.Ransum > 2]["Ransum"]
data_length = int(len(data)/2)
sample1 = data[df_length:]
sample2 = data[:df_length]
print("1. h0 : Sample1 = Sample2")
print("2. h1 : Sample1 > Sample2")
print("3. alpha = 0.05")
pt = len(sample1)/len(df)
pc = len(sample2)/len(df)
print("4. Two-Sample One-Tailed Binomial Test")
print("Daerah kritis: Z > 1.645")
p = (len(sample1) + len(sample2))/len(df)
q = 1-p
z = (pt-pc)/math.sqrt(p * q * ((1/len(sample1) + (1/len(sample2)))))
pval = stats.norm.sf(abs(z)) #one-sided
print("5. Nilai P: ", pval)
if pval < 0.05:
   print("6. P lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga proporsi bagian awal lebih besar")
else:
  print("6. P lebih besar dari alpha, Hipotesis null diterima, sehingga proporsi bagian awal tidak lebih besar")
df.boxplot(column="Ransum")


# In[79]:


#5.e
print("5e. Bagian awal kolom Diameter memiliki variansi yang sama dengan bagian akhirnya?")
data = df[df.Ransum > 2]["Diameter"]
data_length = int(len(data)/2)
sample1 = data[df_length:]
sample2 = data[:df_length]
print("1. h0 : VarSample1 = VarSample2")
print("2. h1 : VarSample1 =/= VarSample2")
print("3. alpha = 0.05")
print("4. Two-Tailed Dist f Test")
F = sample1.var() / sample2.var()
p_val = stats.f.cdf(F, len(sample1)-1, len(sample2)-1)
print("5. Nilai P: ", pval)
if pval < 0.05:
    print("6. P lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga variansi tidak sama")
else:
    print("6. P lebih besar dari alpha, Hipotesis null diterima, sehingga variansi sama")
df.boxplot(column="Diameter")


# In[ ]:




