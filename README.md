# ProbProg-COVID-19

This repo is the Pyro and Python codes for "Responses to COVID-19 with Probabilistic Programming" published in Frontiers in Public Health
> [**Responses to COVID-19 with Probabilistic Programming**](https://www.frontiersin.org/articles/10.3389/fpubh.2022.953472/full)
> >
> Assem Zhunis, Tung-Duong Mai, Sundong Kim.
> 
> The COVID-19 pandemic left its unique mark on the 21st century as one of the most significant disasters in history, triggering governments all over the world to respond with a wide range of interventions. However, these restrictions come with a substantial price tag. It is crucial for governments to form anti-virus strategies that balance the trade-off between protecting public health and minimizing the economic cost. This work proposes a probabilistic programming method to quantify the efficiency of major non-pharmaceutical interventions. We present a generative simulation model that accounts for the economic and human capital cost of adopting such strategies, and provide an end-to-end pipeline to simulate the virus spread and the incurred loss of various policy combinations. By investigating the national response in 10 countries covering four continents, we found that social distancing coupled with contact tracing is the most successful policy, reducing the virus transmission rate by 96\%. We also investigate the recent vaccination efforts and found that widespread vaccination successfully mitigates the virus spread.


## Data:

[1. COVID-19 Dataset | Kaggle](https://www.kaggle.com/imdevskp/corona-virus-report?select=full_grouped.csv&fbclid=IwAR3ZDw5Kc9lo9kbIiw63fyrvSdV1CPSnQUbFAVXgKx9jIIxm6nWce5DFRs0 )

[2. COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://git.io/Jvoxz)


## Pipeline:
To quantitatively express and analyze the success and failure of different countries in mitigation of virus spread, we utilize a probabilistic approach to tackle the COVID-19 transmission dynamics. As illustrated in the figure below, our approach has three major components:
1. We infer COVID-19 related parameters such as basic reproduction number R0, incubation rate σ, recovery rate γ, and mortality rate μ using the compartmental model. ([Compartmental_model.ipynb](https://github.com/assemzh/ProbProg-COVID-19/blob/master/Compartmental_model.ipynb))
2. We apply the change-point model to infer policy efficiencies from different countries. ([Changing_point_model.ipynb](https://github.com/assemzh/ProbProg-COVID-19/blob/master/Changing_point_model.ipynb))
3. Finally, using inferred parameters from previous steps and economic parameters from real-world data, we run the generative model in artificial country simulation to estimate the economic cost for different COVID-19 policy combinations. ([Policy_cost.ipynb](https://github.com/assemzh/ProbProg-COVID-19/blob/master/Policy_cost.ipynb))
<p align="center">
<img src="https://user-images.githubusercontent.com/50063452/120110974-e9708a80-c1aa-11eb-9be5-9177e590d02f.png" width = "400" height = "400"> </center>
</p>
<p align="center">
  NOTE: You can input your own country's parameters.
</p>

## Experiments
To see all experiments, please, refer to the [Experiments folder](https://github.com/assemzh/ProbProg-COVID-19/tree/master/Experiments)

If you have problem viewing the file: "Sorry, something went wrong. Reload?", please follow these links:

**Source code:**

1. [Compartmental model](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Compartmental_model.ipynb)

2. [Change-point model](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Change_point_model.ipynb)

3. [Generative model](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Policy_cost.ipynb)

**Experiment files:**

* [🇨🇦 Canada](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Can_changing_point.ipynb) 

* [🇦🇺 Australia](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Aus_changing_point.ipynb)  

* [🇨🇳 China](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/China_changing_point.ipynb)  

* [🇰🇷 South Korea](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Kr_changing_point.ipynb)    

* [🇳🇿 New Zealand](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/NZ_changing_point.ipynb)   

* [🇸🇬 Singapore](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Sing_changing_point.ipynb)   

* [🇺🇸 The US](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/US_changing_point.ipynb)    

* [🇮🇱 Israel](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Israel_changing_point.ipynb)   

* [🇯🇵 Japan](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Japan_virus_model.ipynb)   

* [🇸🇪 Sweden](https://nbviewer.jupyter.org/github/assemzh/ProbProg-COVID-19/blob/master/Experiments/Sweden_virus_model.ipynb)    

## Results:

1. Estimation results of COVID-19 virus parameters without any interventions. 
<p align="center">
<img src="https://user-images.githubusercontent.com/50063452/210205793-094308e7-0a0c-432c-aaeb-6f11df33a4ed.jpeg"> </center>
</p>

2. Estimated efficacies of policies in 10 countries.
<p align="center">
<img src="https://user-images.githubusercontent.com/50063452/210205781-7100cba1-0406-475c-b0b4-b0907bda7be2.jpeg"> </center>
</p>

3. Estimated cost of various policy combinations.
  
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

## Code references: 
We adapt some of our code from these sources:
* [Estimating the Date of COVID-19 Changes using Pyro](https://nbviewer.jupyter.org/github/jramkiss/jramkiss.github.io/blob/master/_posts/notebooks/covid19-changes.ipynb)
* [SEIR Model Implementation in Pyro](https://docs.pyro.ai/en/dev/_modules/pyro/contrib/epidemiology/models.html#SimpleSEIRModel)

## Citation
If you find this code useful, please cite the [original paper](https://www.frontiersin.org/articles/10.3389/fpubh.2022.953472/full):
```LaTeX
@article{zhunis2022responses,
  title={Responses to COVID-19 with probabilistic programming},
  author={Assem Zhunis and Tung-Duong Mai and Sundong Kim},
  journal = {Frontiers in Public Health},
  year = {2022}
}
```
