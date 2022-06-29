import sample
import plot

# Chama os aquivos 

s1 = sample.Sample("C5P1")
s1.read_from_xlsx("input/CAMPO_5_POCO_1.xlsx")
s2 = sample.Sample("C5P2")
s2.read_from_xlsx("input/CAMPO_5_POCO_2.xlsx")
s3 = sample.Sample("C5P3")
s3.read_from_xlsx("input/CAMPO_5_POCO_3.xlsx")
s4 = sample.Sample("C6P1")
s4.read_from_xlsx("input/CAMPO_6_POCO_1.xlsx")

#Gera os arquivos xlsx de saida com o diagnostico

s1.diagnostics_xlsx("c5p1.xlsx")
s2.diagnostics_xlsx("c5p2.xlsx")
s3.diagnostics_xlsx("c5p3.xlsx")
s4.diagnostics_xlsx("c6p1.xlsx")

#gera o grafico de intensidade similar de Kendrick
plot.dbe_c(s1, "NO2", filename="%s_NO2.png" % (s1.name))
plot.dbe_c(s2, "NO2", filename="%s_NO2.png" % (s2.name))
plot.dbe_c(s3, "NO2", filename="%s_NO2.png" % (s3.name))
plot.dbe_c(s4, "NO2", filename="%s_NO2.png" % (s4.name))
plot.dbe_c(s1, "O2", filename="%s_O2.png" % (s1.name))
plot.dbe_c(s2, "O2", filename="%s_O2.png" % (s2.name))
plot.dbe_c(s3, "O2", filename="%s_O2.png" % (s3.name))
plot.dbe_c(s4, "O2", filename="%s_O2.png" % (s4.name))
plot.dbe_c(s1, "N", filename="%s_N.png" % (s1.name))
plot.dbe_c(s2, "N", filename="%s_N.png" % (s2.name))
plot.dbe_c(s3, "N", filename="%s_N.png" % (s3.name))
plot.dbe_c(s4, "N", filename="%s_N.png" % (s4.name))
#adiciona objeto
p1 = plot.Plot()
p1.add_group([s1], "C5P1")
p1.add_group([s2], "C5P2")
p1.add_group([s3], "C5P3")
p1.add_group([s4], "C6P1")

# plota a distribuição de carbono para um determinado DBE de uma classe
p1.c_dbe("O2", 1, filename="O2_DBE1.png")

# plota os parametros de maturidade
p1.maturity(filenames=["m1.png", "m2.png", "m3.png", "m4.png", "m5.png"])

# Plota os parametros de paleoambiente
p1.paleoenvironment(filenames=["p1.png", "p2.png", "p3.png", "p4.png"])

# Plota os parametros de biodegradacao
p1.biodegradation(filenames=["b1.png", "b2.png", "b3.png", "b4.png", "b5.png"])

# Plota o a distribuicao heteroatomica de uma amostra tem que mudar no plotpy
#p1.heteroatomic_dist(s1, filename="ra.png")

# Plota o a distribuicao heteroatomica de todas amostras juntas
p1.heteroatomic_dist(filename="ra.png")


# plota a distribuicao de DBE para algumas classes
p1.class_dbe("N", filename="dbes_N.png")
p1.class_dbe("NO", filename="dbes_NO.png")
p1.class_dbe("O", filename="dbes_O.png")
p1.class_dbe("O2", filename="dbes_O2.png")
p1.class_dbe("O3", filename="dbes_O3.png")
p1.class_dbe("O4", filename="dbes_O4.png")
p1.class_dbe("O5", filename="dbes_O5.png")
