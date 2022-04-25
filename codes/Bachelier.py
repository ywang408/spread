import numpy as np
from scipy.stats import norm


def solution(r, x, K, T, sigma):
    df = np.exp(-r * T)
    F = x / df
    v = np.sqrt(sigma ** 2 / 2 / r * (np.exp(2 * r * T) - 1))
    tmp = (F - K) / v
    return df * ((F - K) * norm.cdf(tmp) + v * norm.pdf(tmp))


def simulation1(r, x, K, T, sigma, n, m):
    # n: time steps, m: num of path
    dt = T / n
    s = np.ones(m) * x
    for i in range(n):
        z = np.random.normal(0, 1, size=m)
        s = s + r * s * dt + sigma * z * np.sqrt(dt)
    payoffs = np.maximum(s - K, 0)
    return np.exp(-r * T) * payoffs.mean()


def simulation2(r, x1, x2, K, T, sigma1, sigma2, rho, alpha1, alpha2, n, m):
    dt = T / n
    s1 = np.ones(m) * x1
    s2 = np.ones(m) * x2
    for i in range(n):
        z1 = np.random.normal(0, 1, size=m)
        z2 = np.random.normal(0, 1, size=m)
        z3 = rho * z1 + np.sqrt(1 - rho ** 2) * z2
        s1 = s1 + r * s1 * dt + sigma1 * z1 * np.sqrt(dt)
        s2 = s2 + r * s2 * dt + sigma2 * z3 * np.sqrt(dt)
    s = alpha2 * s2 - alpha1 * s1
    payoffs = np.maximum(s - K, 0)
    return np.exp(-r * T) * payoffs.mean()


if __name__ == "__main__":
    x1 = 20
    x2 = 50
    alpha1 = 1
    alpha2 = 0.8
    x = alpha2 * x2 - alpha1 * x1
    K = 10
    sigma1 = 20 * 0.1
    sigma2 = 30 * 0.15
    rho = 0.5
    sigma = np.sqrt(alpha1 ** 2 * sigma1 ** 2 + alpha2 ** 2 * sigma2 ** 2 - 2 * rho * alpha1 * alpha2 * sigma1 * sigma2)
    r = 0.1
    T = 1
    res1 = solution(r, x, K, T, sigma)
    res2 = simulation1(r, x, K, T, sigma, 1000, 100000)
    res3 = simulation2(r, x1, x2, K, T, sigma1, sigma2, rho, alpha1, alpha2, 1000, 100000)
    print("closed-form solution: ", res1)
    print("Simulating Spread Process: ", res2)
    print("Simulating s1 and s2: ", res3)
