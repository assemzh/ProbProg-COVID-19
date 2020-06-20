import matplotlib.pyplot as plt
test_cap = 0.001
hygiene = 1- 1.72/2.11    #parameters to be infered
distancing = 0.7 # US/Italy after lockdown
lockdown = 0.93
quarantine = 0.7 # Korea

hospital_cap = 2* 1/3400
transmission_days = 16.92/2.11
exposed_days = 3.59 
recovery_days = 16.92 
# waning_days = 365

susceptible0 = 0.99999
infected0 = 0.00001
exposed0 = 0
recovered0 = 0

population = 1000000


def virus_model(hygiene_list, distancing_list,lockdown_list,quarantine_list):

  assert len(hygiene_list) == len(distancing_list) == len(lockdown_list) == len(quarantine_list)

  duration = len(hygiene_list)

  
  transmission_rate = (1/ transmission_days)
  incubation_rate = (1/  exposed_days)
  recovery_rate = (1/ recovery_days)
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
  policy = []
  
  testing = 0
  # transmission_rate = transmission_rate * (1- hygiene) * (1- distancing) * (1- lockdown) * (1- quarantine)
  # transmission_rate0 = susceptible0transmission_rate * (1- testing)
  # transmission_rate = transmission_rate0
  # transmission_rate = transmission_rate * (1-lockdown)
  for day in range(duration):
    # if test_cap < infected + exposed:
    #   transmission_rate = transmission_rate0
    # else:
    #   transmission_rate = transmission_rate0
    ld_point = - population * 0.1 * 30 /365
    qr_point = - population * infected * 0.1
    hg_point = - population * 0.005
    dst_point = - population * 0.1 * 15 /365
  
    policy_point = hg_point * hygiene_list[day] + dst_point * distancing_list[day] + ld_point*lockdown_list[day] + qr_point*quarantine_list[day]
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
    policy.append(policy_point)
  
  return susc, exp, inf, rec, d, re, policy


def evaluate(inf, rec, d, policy):

  dd_point = -4900
  inf_point = -100
  rec_point = 100

  return sum(inf)*inf_point + sum(rec)*rec_point + sum(d)*dd_point + sum(policy)


hygiene_list = [1]*10
distancing_list = [0]*10
lockdown_list = [0,0,0,1,1,1,0,0,0,0]
quarantine_list = [0,0,1,0,0,0,0,0,0,0]
days = 10

susc, exp, inf, rec, d, re, policy = virus_model(hygiene_list, distancing_list,lockdown_list,quarantine_list)
print(evaluate(inf, rec, d, policy))

##for i in result:
## print(i)
##m = [m for m in range(days+1)]
##
##plt.plot(m, result[0], label="line S")
##plt.plot()
##plt.show()
##
##plt.plot(m, result[1], label="line E")
##plt.plot()
##plt.show()
##
##plt.plot(m, result[2], label="line I")
##plt.plot()
##plt.show()
##
##plt.plot(m, result[3], label="line R")
##plt.plot()
##plt.show()
##
##plt.plot(m, result[4], label="line D")
##plt.plot()
##plt.show()
##
##plt.plot(m, result[5], label="line Re")
##plt.plot()
##plt.show()
