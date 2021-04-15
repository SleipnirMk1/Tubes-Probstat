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
