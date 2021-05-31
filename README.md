# ProbProg-COVID-19

The COVID-19 pandemic left its unique mark on the 21st century as one of the most significant disasters in history, triggering governments all over the world to respond with a wide range of interventions. However, these restrictions come with a substantial price tag. It is crucial for governments to form anti-virus strategies that balance the trade-off between protecting public health and minimizing the economic cost. This work proposes a probabilistic programming method to quantify the efficiency of major non-pharmaceutical interventions. We present a generative simulation model that accounts for the economic and human capital cost of adopting such strategies, and provide an end-to-end pipeline to simulate the virus spread and the incurred loss of various policy combinations. By investigating the national response in 10 countries covering four continents, we found that social distancing coupled with contact tracing is the most successful policy, reducing the virus transmission rate by 96\%. We also investigate the recent vaccination efforts and found that widespread vaccination successfully mitigates the virus spread.

# Data:
* https://www.kaggle.com/imdevskp/corona-virus-report?select=full_grouped.csv&fbclid=IwAR3ZDw5Kc9lo9kbIiw63fyrvSdV1CPSnQUbFAVXgKx9jIIxm6nWce5DFRs0 
* https://git.io/Jvoxz

# Pipeline:

<img src="https://user-images.githubusercontent.com/50063452/120110974-e9708a80-c1aa-11eb-9be5-9177e590d02f.png" width = "400" height = "400">

1. Get the virus statistic by Compartmental Model  (SEIRD) --> Compartmental_model.ipynb

2. Infer statistics on how policies affect the virus spread by the Change-point model. --> Changing_point_model.ipynb

3. Simulation with artifitial country by Generative model --> Policy_cost.ipynb

You can input your own country's parameters.

# Experiment
To see all experiments, please, refer to the Experiments folder

If you have problem viewing the file: "Sorry, something went wrong. Reload?", please follow these links:

Source code:

[Compartmental model](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Compartmental_model.ipynb)

[Change-point model](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Change_point_model.ipynb)

[Generative model](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Policy_cost.ipynb)

Experiment files:

[Canada](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Can_changing_point.ipynb) 

[Australia](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Aus_changing_point.ipynb)  

[China](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/China_changing_point.ipynb)  

[South Korea](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Kr_changing_point.ipynb)    

[New Zealand](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/NZ_changing_point.ipynb)   

[Singapore](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Sing_changing_point.ipynb)   

[The US](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/US_changing_point.ipynb)    

[Israel](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Israel_changing_point.ipynb)   

[Japan](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Japan_virus_model.ipynb)   

[Sweden](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Sweden_virus_model.ipynb)    

# Results:

![image](https://user-images.githubusercontent.com/50063452/120111026-2b013580-c1ab-11eb-87f0-bd749d922ec4.png)

![image](https://user-images.githubusercontent.com/50063452/120111036-381e2480-c1ab-11eb-9d74-68994bdee294.png)



| Policy combination   | Cases  | Deaths | Loss \(billion $\) |
|:--------------------:|:------:|:------:|:----------------------:|
| MT \| T \| T         | 10734  | 577    | 4\.525967         |
| T \| T \| T          | 11003  | 591    | 4\.569165         |
| L \| L \| L          | 11003  | 591    | 4\.932606         |
| MDLT \| MDLT \| MDLT | 10006  | 539    | 5\.482550         |
| D \| D \| D          | 22478  | 1138   | 8\.436941         |
| mt \| Lt \| Dl       | 26023  | 1378   | 10\.463221        |
| mt \| Lt \| Dlt      | 25736  | 1370   | 10\.472406        |
| mt \| L \| DlT       | 25887  | 1383   | 10\.561816        |
| m \| L \| DT         | 59338  | 3502   | 25\.313706        |
| M \| M \| M          | 201929 | 8941   | 63\.400395        |
| \- \| m \| \-        | 515900 | 23447  | 165\.681432       |
| \- \| \- \| d        | 453512 | 23862  | 168\.641122       |
| \- \| \- \| M        | 478792 | 24620  | 173\.993851       |
| \- \| \- \| m        | 534917 | 26295  | 185\.788009       |
| \- \| \- \| \-       | 592136 | 28018  | 197\.926939       |
| \- \| \- \| \-       | 592136 | 28018  | 197\.926939       |



Table represents loss regarding applied policies. The most effective policy combination is listed at the top. The meaning of policy notatioin is as follows:

*   None: Doing nothing
*   Uppercase: full efficacy
*   Lowercase: half efficacy


*   L/l: Lockdown
*   T/t: Tracing with distancing
*   D/d: Distancing
*   M/m: Masks and Hygiene

*Example: L | l | D denotes the consecutive policy execution of full lockdown (1st month), half lockdown (2nd month) and full distancing (3rd month).*

# Code references: 
We adapt some of our code from these sources:
https://nbviewer.jupyter.org/github/jramkiss/jramkiss.github.io/blob/master/_posts/notebooks/covid19-changes.ipynb
https://docs.pyro.ai/en/dev/_modules/pyro/contrib/epidemiology/models.html#SimpleSEIRModel
