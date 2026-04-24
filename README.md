# **Evaluating the Association Between Grade 8 ELA IAB Exposure and Summative Pass Rates**

[View the full report](./ela-iab-exposure-pass-rate-analysis.html) 

## **Overview**

This project evaluates whether exposure to a Grade 8 ELA Interim Assessment Block (IAB) is associated with differences in pass rates on the Grade 8 ELA Summative assessment.

The analysis builds on prior feature importance modeling (SHAP), which identified the IAB as a potentially meaningful predictor of summative performance. Because feature importance reflects predictive contribution rather than outcome-level effects, this project conducts statistical testing to better understand the relationship between IAB exposure and student outcomes.

---

## **Key Question**

Is exposure to the Grade 8 ELA IAB associated with higher pass rates on the Grade 8 ELA Summative assessment?

---

## **Methods**

### **Data Preparation**

* Student-level assessment data was reshaped to a wide format using pivot operations.  
* A single ELA Summative outcome column was constructed for Grade 8 students.  
* The analysis was restricted to Grade 8 to ensure alignment between exposure and outcome.

### **Group Definition**

* **Exposed group**: Students with a recorded score for the Grade 8 ELA IAB  
* **Unexposed group**: Students without a recorded score

### **Statistical Approach**

Two complementary methods were used:

1. **Bayesian Analysis (Beta–Binomial Model)**  
   * Prior: Beta(2,2)  
   * Posterior sampling used to estimate:  
     * Probability that exposed pass rate exceeds unexposed  
     * Distribution of effect size  
2. **Frequentist Analysis (Two-Proportion Z-Test)**  
   * Hypothesis test for difference in pass rates  
   * Confidence interval for effect size

---

## **Results**

### **Bayesian**

* Probability exposed group has higher pass rate: **0.896**  
* Mean difference: **\+5.4%**  
* 95% credible interval: **\[-3%, \+13.6%\]**

### **Frequentist**

* p-value: **0.21** (not statistically significant)  
* 95% confidence interval: **\[-3%, \+13.7%\]**

---

## **Interpretation**

The results suggest a likely positive association between IAB exposure and pass rates. However, uncertainty remains substantial, with both small negative and moderate positive effects consistent with the data.

The frequentist result does not provide statistically significant evidence of a difference, aligning with the wide uncertainty observed in the Bayesian analysis.

Overall, the findings are directionally encouraging but not conclusive.

---

## **Limitations**

* Exposure was not randomly assigned (observational data)  
* Cohort differences may influence results  
* Potential confounding factors (e.g., classroom, teacher, or student characteristics) are not controlled for

---

## **Recommendation**

The IAB may serve as a useful early indicator of summative performance, but additional data or more controlled comparisons are needed before making instructional or policy decisions based on this relationship.

---

## **Files**

* `ela-iab-exposure-pass-rate-analysis.ipynb` — full analysis notebook  
* `ela-iab-exposure-pass-rate-analysis.html` — rendered report

---

## **Tools & Technologies**

* Python (pandas, numpy, scipy)  
* Bayesian modeling via NumPy sampling  
* Data visualization with matplotlib / seaborn

---

## **How to Run**

1\. Clone the repository:  
```  
bash

git clone https://github.com/cadupee1464/ela-iab-analysis  
cd ela-iab-analysis  
```

2\. Open the notebook:  
`jupyter notebook` OR `jupyter lab`  

3\. Run all cells in:  
`Ela-iab-exposure-pass-rate-analysis.ipynb`

## **Notes**

This project demonstrates:

* Translation of model-based insights (SHAP) into statistical validation  
* Use of both Bayesian and frequentist frameworks  
* Careful handling of observational data and interpretation limits

---

