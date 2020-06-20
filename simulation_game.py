import matplotlib.pyplot as plt
import pyro
import pyro.distributions as dist
from pyro.nn import PyroModule, PyroSample
import torch

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

  result = sum(inf)*inf_point + sum(rec)*rec_point + sum(d)*dd_point + sum(policy)
  return result


##hygiene_list = [1]*10
##distancing_list = [0]*10
##lockdown_list = [0,0,0,1,1,1,0,0,0,0]
##quarantine_list = [0,0,1,0,0,0,0,0,0,0]
##days = 10
##
##susc, exp, inf, rec, d, re, policy = virus_model(hygiene_list, distancing_list,lockdown_list,quarantine_list)
##print(evaluate(inf, rec, d, policy))


def model(guess):
##    def forward(self):
        h1 = pyro.sample("h1",dist.Normal(guess["h1"], 0.25))
        h2 = pyro.sample("h2",dist.Normal(guess["h2"], 0.25))
        h3 = pyro.sample("h3",dist.Normal(guess["h3"], 0.25))

        d1 = pyro.sample("d1",dist.Normal(guess["d1"], 0.25))
        d2 = pyro.sample("d2",dist.Normal(guess["d2"], 0.25))
        d3 = pyro.sample("d3",dist.Normal(guess["d3"], 0.25))
        
        l1 = pyro.sample("l1",dist.Normal(guess["l1"], 0.25))
        l2 = pyro.sample("l2",dist.Normal(guess["l2"], 0.25))
        l3 = pyro.sample("l3",dist.Normal(guess["l3"], 0.25))
        
        q1 = pyro.sample("q1",dist.Normal(guess["q1"], 0.25))
        q2 = pyro.sample("q2",dist.Normal(guess["q2"], 0.25))
        q3 = pyro.sample("q3",dist.Normal(guess["q3"], 0.25))
        
        hygiene_list = [h1]*30 + [h2]*30 + [h3]*30
        distancing_list = [d1]*30 + [d2]*30 + [d3]*30
        lockdown_list = [l1]*30 + [l2]*30 + [l3]*30
        quarantine_list = [q1]*30 + [q2]*30 + [q3]*30

        susc, exp, inf, rec, d, re, policy = virus_model(hygiene_list, distancing_list,lockdown_list,quarantine_list)
        
        point = evaluate(inf, rec, d, policy)

##        print(point)

##        obs = pyro.sample("obs", dist.Normal(point, 10000), obs=torch.tensor(0.))
        
##        return h1,h1,h3,d1,d2,d3,l1,l2,l3,q1,q2,q3
        return pyro.sample("obs", dist.Normal(point, 10000))
import argparse
import logging

import torch

import pyro
import pyro.distributions as dist
import pyro.poutine as poutine
from pyro.infer import MCMC, NUTS

logging.basicConfig(format='%(message)s', level=logging.INFO)
pyro.enable_validation(__debug__)
pyro.set_rng_seed(0)

def scale(guess):
    return model(guess)
conditioned_scale = pyro.condition(scale, data={"obs": torch.tensor(0.)})
from pyro.infer.mcmc import MCMC
from pyro.infer.mcmc.nuts import HMC
from pyro.infer import EmpiricalMarginal
import matplotlib.pyplot as plt
# %matplotlib inline
guess_prior = {"h1": 0.5, "h2": 0.5, "h3": 0.5, "d1": 0.5, "d2": 0.5, "d3": 0.5, "l1": 0.5, "l2": 0.5, "l3": 0.5, "q1": 0.5, "q2": 0.5, "q3": 0.5}
hmc_kernel = HMC(conditioned_scale, step_size=0.9, num_steps=4)
posterior = MCMC(hmc_kernel, 
                 num_samples=400, 
                 warmup_steps=50).run(guess_prior)
mcmc.summary()
# def conditioned_model(model):
#     return poutine.condition(model, data={"obs": 0})


# def main(args):
#     nuts_kernel = NUTS(conditioned_model, jit_compile=args.jit)
#     mcmc = MCMC(nuts_kernel,
#                 num_samples=args.num_samples,
#                 warmup_steps=args.warmup_steps,
#                 num_chains=args.num_chains)
#     mcmc.run(model)
#     mcmc.summary()


# if __name__ == '__main__':
# ##    assert pyro.__version__.startswith('1.3.0')
#     parser = argparse.ArgumentParser(description='COVID GAME MCMC')
#     parser.add_argument('--num-samples', type=int, default=1000,
#                         help='number of MCMC samples (default: 1000)')
#     parser.add_argument('--num-chains', type=int, default=1,
#                         help='number of parallel MCMC chains (default: 1)')
#     parser.add_argument('--warmup-steps', type=int, default=1000,
#                         help='number of MCMC samples for warmup (default: 1000)')
#     parser.add_argument('--jit', action='store_true', default=False)
#     args = parser.parse_args()

#     main(args)


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
