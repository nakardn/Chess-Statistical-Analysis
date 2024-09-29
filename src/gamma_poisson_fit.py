import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize

def log_likelihood_gamma_poisson(params, data):
    """
    Calculates the log-likelihood of a mixture of Gamma and Poisson distributions.

    Args:
        params: A tuple containing the parameters: (a, c, loc, scale, lam, w).
                a, c, loc, scale are the Gamma distribution parameters.
                lam is the Poisson distribution parameter.
                w is the weight of the Gamma distribution (Poisson weight is 1-w).
        data: The observed data.

    Returns:
        The negative log-likelihood (for minimization).
    """
    a, c, loc, scale, lam, w = params
    if a <= 0 or c <= 0 or scale <= 0 or lam <= 0 or w < 0 or w > 1:  # Parameter constraints
        return np.inf

    gamma_pdf = stats.gengamma.pdf(data, a, c, loc=loc, scale=scale)
    poisson_pmf = stats.poisson.pmf(data, lam)

    likelihood = w * gamma_pdf + (1 - w) * poisson_pmf
    log_likelihood = np.sum(np.log(likelihood)) 

    return -log_likelihood # Negative for minimization

def fit_gamma_poisson(data):
    # Initial guesses for parameters
    initial_params = (2, 2, 10, 5, 25, 0.6)  # Example initial guess

    # Set up the figure and axes
    fig, axs = plt.subplots()

    # Optimization (find maximum likelihood estimates)
    result = minimize(log_likelihood_gamma_poisson, initial_params, args=(data,), method='Nelder-Mead')

    # Fitted parameters
    a_fitted, c_fitted, loc_fitted, scale_fitted, lam_fitted, w_fitted = result.x

    print("Fitted parameters:")
    print(f"  a: {a_fitted}, c: {c_fitted}, loc: {loc_fitted}, scale: {scale_fitted}")
    print(f"  lambda: {lam_fitted}")
    print(f"  w (Gamma weight): {w_fitted}")


    # Plotting
    x = np.linspace(1, data.max(), data.max()) # Ensure integer spacing
    pdf_fitted = w_fitted * stats.gengamma.pdf(x, a_fitted, c_fitted, loc=loc_fitted, scale=scale_fitted) + (1 - w_fitted) * stats.poisson.pmf(x, lam_fitted)

    sns.histplot(data, kde=False, stat='density', label='Data') # Add discrete=True for better visualization of discrete data
    plt.plot(x, pdf_fitted, label='Fitted Gamma-Poisson Mixture PDF', color='red')
    plt.xlabel('Turns')
    plt.ylabel('Density')
    plt.legend()

    return fig