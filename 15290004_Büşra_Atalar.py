import networkx as nx
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
%matplotlib inline  
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
from ndlib.viz.mpl.TrendComparison import DiffusionTrendComparison

# g ağı temsil ediyor, erdos renyi rastgale bir ağdır,  topluluk ilişkilerinin 
# bu ağ tipinde olduğu var sayılıabilir. networkx de çok sayıda ağ tipi tanımlı

g = nx.erdos_renyi_graph(1000, 0.1)

#Ağ ve bağlantıları grafiği //1000 olan node sayısını azaltırsan ağ daha anlaşılır görünür
plt.figure(3,figsize=(24,12)) 
nx.draw_networkx(g,with_labels=False,node_color='g',edge_color='k',node_size=100,linewidths=0.01,width=0.01,pos=nx.spring_layout(g))
#%%
# Model ndlib SIS ve ndlib SIR hastalık yayılma modelleri  aşağıda var 

# SIS model
model =  ep.SISModel(g)

cfg = mc.Configuration()
cfg.add_model_parameter('beta', 0.001) #hastalanma olasılığı
cfg.add_model_parameter('lambda', 0.002)  #iyileme olasılığı ---> SIS model
cfg.add_model_parameter("fraction_infected", 0.5)  #başlangıç
model.set_initial_status(cfg)

# modelin çalışması
iterations = model.iteration_bunch(200)
trends = model.build_trends(iterations)


viz = DiffusionTrend(model, trends)
viz.plot(percentile=20)
plt.show()



# SIR Model
model1 = ep.SIRModel(g)


cfg = mc.Configuration()
cfg.add_model_parameter('beta', 0.001)
cfg.add_model_parameter('gamma', 0.002)
cfg.add_model_parameter("fraction_infected", 0.5)
model1.set_initial_status(cfg)


iterations = model1.iteration_bunch(200)
trends1 = model1.build_trends(iterations)



viz = DiffusionTrend(model1, trends1)
viz.plot(percentile=20)
plt.show()



#SI MODELİ

model2 = ep.SIModel(g)


# Model Configuration
cfg = mc.Configuration()
cfg.add_model_parameter('beta', 0.001)
cfg.add_model_parameter("fraction_infected", 0.5)
model2.set_initial_status(cfg)

# Simulation execution
iterations = model2.iteration_bunch(200)
trends2= model2.build_trends(iterations)

#GÖRSELLEŞTİRME
viz = DiffusionTrend(model2, trends2)
viz.plot(percentile=20)



#SEİR MODELİ

model3 = ep.SEIRModel(g)

# Model Configuration
cfg = mc.Configuration()
cfg.add_model_parameter('beta', 0.001)
cfg.add_model_parameter('gamma', 0.002)
cfg.add_model_parameter('alpha', 0.05)
cfg.add_model_parameter("fraction_infected", 0.5)
model3.set_initial_status(cfg)

# Simulation execution
iterations = model3.iteration_bunch(200)
trends3= model3.build_trends(iterations)

viz = DiffusionTrend(model3, trends3)
viz.plot(percentile=20)


plt.show()


#SEİS MODELİ

# Model selection
model4 = ep.SEISModel(g)

# Model Configuration
cfg = mc.Configuration()
cfg.add_model_parameter('beta', 0.001)
cfg.add_model_parameter('lambda', 0.002)
cfg.add_model_parameter('alpha', 0.05)
cfg.add_model_parameter("fraction_infected", 0.5)
model4.set_initial_status(cfg)

# Simulation execution
iterations = model4.iteration_bunch(200)
trends4= model4.build_trends(iterations)

viz = DiffusionTrend(model4, trends4)
viz.plot(percentile=20)




viz = DiffusionTrendComparison([model,model1,model2,model3,model4], [trends,trends1,trends2,trends3,trends4])
viz.plot(percentile=20)
plt.show()

