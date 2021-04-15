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

