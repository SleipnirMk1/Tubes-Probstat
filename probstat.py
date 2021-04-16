import pandas as pd
import pylab 
import scipy.stats as stats

df = pd.read_csv("Gandum.csv")

df.describe()

print("Modus: ")
df.mode()
#Beberapa data memiliki 500 modus karena setiap datanya unik

print("Skewness: ")
df.skew()

print("Variance: ")
df.var()

print("Kurtosis: ")
df.kurt()

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

#Mengetahui distribusi normal dapat dengan membandingkan bentuk histogram dengan normal probability curve
#Daerah
df.hist(column="Daerah")

df.boxplot(column="Daerah")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Daerah"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Berdistribusi normal")

#Sumbu Utama
df.hist(column="SumbuUtama")

df.boxplot(column="SumbuUtama")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["SumbuUtama"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal, terdapat outlier yang signifikan")

#Sumbu Kecil
df.hist(column="SumbuKecil")

df.boxplot(column="SumbuKecil")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["SumbuKecil"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Berdistribusi normal")

#Keunikan
df.hist(column="Keunikan")

df.boxplot(column="Keunikan")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Keunikan"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal")

#Area Bulatan
df.hist(column="AreaBulatan")

df.boxplot(column="AreaBulatan")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["AreaBulatan"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Berdistribusi normal")

#Diameter
df.hist(column="Diameter")

df.boxplot(column="Diameter")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Diameter"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Berdistribusi normal")

#Kadar Air
df.hist(column="KadarAir")

df.boxplot(column="KadarAir")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["KadarAir"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal")

#Keliling
df.hist(column="Keliling")

df.boxplot(column="Keliling")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Keliling"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal")

#Bulatan
df.hist(column="Bulatan")

df.boxplot(column="Bulatan")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Bulatan"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal")

#Ransum
df.hist(column="Ransum")

df.boxplot(column="Ransum")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Ransum"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal")

#Kelas
df.hist(column="Kelas")

df.boxplot(column="Kelas")

print("Pengujian distribusi normal dengan normality test Quartile-Quartile plot: ")
stats.probplot(df["Kelas"], dist="norm", plot=pylab)
pylab.show()
print("Kesimpulan: Tidak berdistribusi normal")

#Korelasi
#Target adalah kolom "Kelas", yang memiliki nilai 1 atau 2
print("Correlations")

#Kelas-Daerah
df.plot.scatter("Kelas", "Daerah")

print("Korelasi negatif kuat (0.6-0.79)")
df["Kelas"].corr(df["Daerah"])

#Kelas-SumbuUtama
df.plot.scatter("Kelas", "SumbuUtama")

print("Korelasi negatif kuat (0.6-0.79)")
df["Kelas"].corr(df["SumbuUtama"])

#Kelas-SumbuKecil
df.plot.scatter("Kelas", "SumbuKecil")

print("Korelasi negatif sangat lemah (0.0-0.19)")
df["Kelas"].corr(df["SumbuKecil"])

#Kelas-Keunikan
df.plot.scatter("Kelas", "Keunikan")

print("Korelasi negatif kuat (0.6-0.79)")
df["Kelas"].corr(df["Keunikan"])

#Kelas-AreaBulatan
df.plot.scatter("Kelas", "AreaBulatan")

print("Korelasi negatif kuat (0.6-0.79)")
df["Kelas"].corr(df["AreaBulatan"])

#Kelas-Diameter
df.plot.scatter("Kelas", "Diameter")

print("Korelasi negatif kuat (0.6-0.79)")
df["Kelas"].corr(df["Diameter"])

#Kelas-KadarAir
df.plot.scatter("Kelas", "KadarAir")

print("Korelasi positif sangat lemah (0.0-0.19)")
df["Kelas"].corr(df["KadarAir"])

#Kelas-Keliling
df.plot.scatter("Kelas", "Keliling")

print("Korelasi negatif kuat (0.6-0.79)")
df["Kelas"].corr(df["Keliling"])

#Kelas-Bulatan
df.plot.scatter("Kelas", "Bulatan")

print("Korelasi positif sedang (0.4-0.59)")
df["Kelas"].corr(df["Bulatan"])

#Kelas-Ransum
df.plot.scatter("Kelas", "Ransum")

print("Korelasi negatif sangat kuat (0.8-1.0)")
df["Kelas"].corr(df["Ransum"])

#Tes Hipotesis 1 sampel
#a
print("Tes Hipotesis 1 Sampel")
print("4.a: Nilai rata-rata Daerah di atas 4700?")
print("h0: rata-rata = 4700")
print("h1: rata-rata > 4700")
print("alpha = 0.05")
val_list = df["Daerah"].values.tolist()
tset, pval = stats.ttest_1samp(val_list, 4700)
print("Nilai P: ", pval)
if pval < 0.10:    # tes yang diperlukan one-tailed, sementara fungsi menghitung two-ended, sehingga Z daerah kritis perlu 2x lipat
   print("P lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga rata-rata diatas 4700")
else:
  print("P lebih besar dari alpha, Hipotesis null diterima, sehingga rata-rata 4700")

#b
print("4.b: Nilai Rata-rata Sumbu Utama tidak sama dengan 116?")
print("h0: rata-rata = 116")
print("h1: rata-rata =/= 116")
print("alpha = 0.05")
val_list = df["SumbuUtama"].values.tolist()
tset, pval = stats.ttest_1samp(val_list, 116)
print("Nilai P: ", pval)
if pval < 0.05:
   print("P lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga rata-rata bukan 116")
else:
  print("P lebih besar dari alpha, Hipotesis null diterima, sehingga rata-rata 116")

#c
print("4c. Nilai Rata-rata 20 baris pertama kolom Sumbu Kecil bukan 50?")
print("h0: rata-rata = 50")
print("h1: rata-rata =/= 50")
print("alpha = 0.05")
val_list = df["SumbuKecil"].head(20).values.tolist()
tset, pval = stats.ttest_1samp(val_list, 50)
print("Nilai P: ", pval)
if pval < 0.05:
   print("P lebih kecil dari alpha, Hipotesis null tidak diterima, sehingga rata-rata bukan 50")
else:
  print("P lebih besar dari alpha, Hipotesis null diterima, sehingga rata-rata 50")

