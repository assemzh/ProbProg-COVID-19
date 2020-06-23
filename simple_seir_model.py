import matplotlib.pyplot as plt
test_cap = 0.001
hygiene = 1- 1.72/2.11    #parameters to be infered
distancing = 0.7 # US/Ital after lockdown
lockdown = 0.93
quarantine = 0.7 # Korea

hospital_cap = 2* 1/3400
transmission_days = 16.92/2.11/1.5
exposed_days = 3.59 
recovery_days = 16.92 
# waning_days = 365

susceptible0 = 0.9999
infected0 = 0.0001
exposed0 = 0
recovered0 = 0

population = 1000000

def virus_model(days):
  transmission_rate = (1/ transmission_days)
  incubation_rate = (1/  exposed_days)
  recovery_rate = (1/ recovery_days)
  # immunity_loss_rate = (1/ waning_days)
  death_rate_with_med = 0.01
  death_rate_without_med = 0.9
  ser_case_rate = 0.15


  r0 = 2.11

  susceptible =  susceptible0
  infected = infected0
  exposed = exposed0
  recovered = recovered0
  dead = 0

  susc= [population * susceptible0]
  exp = [population * exposed0]
  inf = [population * infected0]
  rec = [population * recovered0]
  re = [r0]
  d = [0]
  testing = 0
  # transmission_rate = transmission_rate * (1- hygiene) * (1- distancing) * (1- lockdown) * (1- quarantine)
  # transmission_rate0 = susceptible0transmission_rate * (1- testing)
  # transmission_rate = transmission_rate0
  # transmission_rate = transmission_rate * (1-lockdown)
  for day in range(days):
    # if test_cap < infected + exposed:
    #   transmission_rate = transmission_rate0
    # else:
    #   transmission_rate = transmission_rate0
    susceptible -= susceptible * infected * transmission_rate 
    exposed +=  susceptible * infected * transmission_rate
    exposed -= exposed * incubation_rate

    infected += exposed * incubation_rate 
    infected -= infected * recovery_rate

    if (ser_case_rate*exposed * incubation_rate < hospital_cap):
      dead += ser_case_rate*exposed * incubation_rate * death_rate_with_med
      infected -= ser_case_rate*exposed * incubation_rate * death_rate_with_med
    else:
      dead += hospital_cap*death_rate_with_med + (exposed * incubation_rate * ser_case_rate - hospital_cap) * death_rate_without_med
      infected -= hospital_cap*death_rate_with_med + (exposed * incubation_rate * ser_case_rate - hospital_cap) * death_rate_without_med

    

    recovered += infected * recovery_rate
    # recovered -= recovered * immunity_loss_rate

    # susceptible += recovered * immunity_loss_rate

    re.append((transmission_rate/ recovery_rate)*susceptible)
    susc.append(population* susceptible)
    exp.append(population* exposed)
    inf.append(population* infected)
    rec.append(population* recovered)
    d.append(population* dead)
  
  return susc, exp, inf, rec, d, re

days = 600

result = virus_model(days)
# for i in result:
#  print(i)
m = [m for m in range(days+1)]

plt.plot(m, result[0], label="line S")
plt.plot()
plt.show()

plt.plot(m, result[1], label="line E")
plt.plot()
plt.show()

plt.plot(m, result[2], label="line I")
plt.plot()
plt.show()

plt.plot(m, result[3], label="line R")
plt.plot()
plt.show()

plt.plot(m, result[4], label="line D")
plt.plot()
plt.show()

# plt.plot(m, result[5], label="line Re")
# plt.plot()
# plt.show()
