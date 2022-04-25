# Gist of Approximating Spread Option by using Bachelier's Model

## Review of Bachelier's Model

When $S_1(t)$ and $S_2(t)$ are given by

$$
\begin{aligned}
d S_{1}(t) &=\mu S_{1}(t) d t+\sigma_{1} d W_{1}(t) \\
d S_{2}(t) &=\mu S_{2}(t) d t+\sigma_{2} d W_{2}(t)
\end{aligned}$$

Set spread $S(t)=\alpha_{2} S_{2}(t)-\alpha_{1} S_{1}(t)$, by choosing $\sigma=\sqrt{\alpha_{1}^{2} \sigma_{1}^{2}+\alpha_{2}^{2} \sigma_{2}^{2}-2 \rho \alpha_{1} \alpha_{2} \sigma_{1} \sigma_{2}}$ spread $S(t)$ can be written into the following SDE

$$
d S(t)=\mu S(t) d t+\sigma d W(t)
$$

which has closed-form solution

$$
c_{B}(t, x ; K, T, \sigma)=\\
e^{-r(T-t)}\left(x e^{r(T-t)}-K\right) \Phi\left(\frac{x e^{r(T-t)}-K}{\sqrt{\frac{\sigma^{2}}{2 r}\left(e^{2 r(T-t)}-1\right)}}\right) \\
\quad+e^{-r(T-t)} \sqrt{\frac{\sigma^{2}}{2 r}\left(e^{2 r(T-t)}-1\right)} \phi\left(\frac{x e^{r(T-t)}-K}{\sqrt{\frac{\sigma^{2}}{2 r}\left(e^{2 r(T-t)}-1\right)}}\right)
$$


## Approximation option value under BS model using Bachelier's model

For BS Model

$$
\begin{aligned}
d S_{1}(t) &=S_{1}(t)  \left[\mu_1  d t+\sigma_{1} d W_{1}(t)\right] \\
d S_{2}(t) &=S_{2}(t)  \left[\mu_2 d t+\sigma_{2} d W_{2}(t)\right]
\end{aligned}
$$

Let $u$ be the option value, define infinitesimal generator $L$ to be

$$
Lu = \frac{\partial u}{\partial t}+\frac{1}{2} \sigma_{1}^{2} x_{1}^{2} \frac{\partial^{2} u}{\partial x_{1}^{2}}+\rho \sigma_{1} \sigma_{2} x_{1} x_{2} \frac{\partial^{2} u}{\partial x_{1} \partial x_{2}}+\frac{1}{2} \sigma_{2}^{2} x_{2}^{2} \frac{\partial^{2} u}{\partial x_{2}^{2}}+\mu_{1} x_{1} \frac{\partial u}{\partial x_{1}}+\mu_{2} x_{2} \frac{\partial u}{\partial x_{2}}
$$

$u$ is the solution to

$$
Lu = ru
$$

Also, under Bachelier's model, we can define another infinitesimal generator $\bar{L}$

$$
\bar{L} \bar{u} = \frac{\partial u}{\partial t}+\frac{1}{2} \sigma_{1}^{2}  \frac{\partial^{2} u}{\partial x_{1}^{2}}+\rho \sigma_{1} \sigma_{2} x_{1} x_{2} \frac{\partial^{2} u}{\partial x_{1} \partial x_{2}}+\frac{1}{2} \sigma_{2}^{2}  \frac{\partial^{2} u}{\partial x_{2}^{2}}+\mu x_{1} \frac{\partial u}{\partial x_{1}}+\mu x_{2} \frac{\partial u}{\partial x_{2}}
$$

Even though we can use KM's method to do the following approximating

$$
L \Delta u(t, x)+(L-\bar{L}) \bar{u}(t, x)= r \Delta u(t,x)
$$

$(L-\bar{L}) \bar{u}(t, x)$ can be complex(Notice that under Bachelier's model, the coefficients for drift term is the same.)

## solution(to be tested)

1. Using BS model as aux model, like approximating option price under Heston Model.
2. Still using Bachelier's model as aux model, and choose appropriate $\alpha_1, \alpha_2$ in spread $S(t)=\alpha_{2} S_{2}(t)-\alpha_{1} S_{1}(t)$, such that first-order partial derivative with respect to $x_1$ and $x_2$ can be canceled. This method may converge faster.

## Transformation of Bachelier's model(solution 2)

Rewrite $S_1^*(t) = \alpha_1 S_1(t)$, $S_2^*(t) = \alpha_2 S_2(t)$, we have

$$
\begin{aligned}
d S_{1}^*(t) &= \alpha_1 d S_{1}(t) = \mu \alpha_1 S_{1}(t) d t+\sigma_{1} \alpha_1 d W_{1}(t) \\
d S_{2}^*(t) &= \alpha_2 d S_{2}(t) = \mu \alpha_2 S_{2}(t) d t+\sigma_{2} \alpha_2  d W_{2}(t)
\end{aligned}$$

Then spread $S(t)= S_2^*(t) - S_1^*(t)$ still follows the SED above and option value has the same closed-form solution.

Under our new setting, $(L-\bar{L})u$ can be more simple.

$\bar{L}$ is defined by

$$
\bar{L} \bar{u} = \frac{\partial u}{\partial t}+\frac{1}{2} \alpha_1^2 \sigma_{1}^{2}  \frac{\partial^{2} u}{\partial x_{1}^{2}}+\rho \alpha_1 \alpha_2 \sigma_{1} \sigma_{2} x_{1} x_{2} \frac{\partial^{2} u}{\partial x_{1} \partial x_{2}}+\frac{1}{2} \alpha_2^2 \sigma_{2}^{2}  \frac{\partial^{2} u}{\partial x_{2}^{2}}+\mu \alpha_1 x_{1} \frac{\partial u}{\partial x_{1}}+\mu \alpha_2 x_{2} \frac{\partial u}{\partial x_{2}}
$$

Since $\alpha_1$ and $\alpha_2$ is flexible, we can set $\mu \alpha_1=\mu_1$, $\mu \alpha_2 = \mu_2$, then $\alpha_1 \sigma_1 = \sigma^*_1$, $\alpha_2 \sigma_2 = \sigma^*_2$, partial derivatives to drift terms can be canceled.

$$
\begin{aligned}
d S_{1}^*(t) &= \mu_1 S_{1}(t) d t+ (\sigma^*_1)^2 d W_{1}(t) \\
d S_{2}^*(t) &= \mu_2 S_{2}(t) d t+(\sigma^*_2)^2  d W_{2}(t)
\end{aligned}$$

$$
(L-\bar{L}) \bar{u}(t, x) = \frac{1}{2} (\sigma_1^2x_1^2 -  (\sigma_{1}^*)^{2})  \frac{\partial^{2} u}{\partial x_{1}^{2}}+(\rho \sigma_{1} \sigma_{2} x_{1} x_{2} - \rho \sigma_{1}^* \sigma_{2}^*) \frac{\partial^{2} u}{\partial x_{1} \partial x_{2}}+\frac{1}{2} (\sigma_2^2x_2^2-  (\sigma_{2}^*)^{2})  \frac{\partial^{2} u}{\partial x_{2}^{2}}
$$