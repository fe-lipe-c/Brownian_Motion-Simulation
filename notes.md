# 22. Simulation of Brownian Motion

## 24.3. Brownian Motion

### Independent Increments

The simplest method to generate a Brownian path uses the property of stationary and independent increments.

----------
**24.15 Algorithm (Independent Increments)** \
Let $0= t_{0}<t_{1}<\dots < t_{n}$ be a time grid.
1. Initialize $b_{0}=0$
2. For $j=1$ to $n$ \
	**a)** Generate $y \stackrel{s}{\sim} N (1,t_{j}-t_{j-1})$\
	**b)** Set $b_{t_{j}} = b_{t_{j-1}} +y$\

Then $(b_{0},b_{t_{1}},\dots,b_{t_{n}}) \stackrel{s}{\sim} (B_{0},B_{t_{1}},\dots, B_{t_{n}})$.

----------
This method works particularly well if the step size $\delta = t_{j}- t_{j-1}$ is constant for all $j$, in this case one has to generate only $y \stackrel{s}{\sim} N (0,\sigma)$ repeatedly. A drawback of the method is, that any refinement of the discretization yields a new simulation and, thus, a different path. 

### Interpolation

To get a refinement of an already simulated path, one can use the idea of Lévy's original argument.

----------
**24.16 Algorithm (Interpolation. Lévy argument)** \
Let $0 \leq s_{0}<s < s_{1}$ be fixed times and $(b_{s_{0}},b_{s_{1}})$ be a sample value of $(B_{s_{0}},B_{s_{1}})$.
1. Generate $b_{s}\stackrel{s}{\sim} N \left( \frac{(s_{1}-s)b_{s_{0}} + (s - s_{0})b_{s_{1}}}{s_{1}-s_{0}}, \frac{(s-s_{0})(s_{1}-s)}{s_{1}-s_{0}}\right)$\

Then $(b_{s_{0}},b_{s},b_{s_{1}}) \stackrel{s}{\sim} (B_{s_{0}},B_{s},B_{s_{1}})$ given that $B_{s_{0}}= b_{s_{0}}$ and $B_{s_{1}}= b_{s_{1}}$.

----------





