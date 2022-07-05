import numpy as np
from gtda.plotting import plot_betti_curves, plot_diagram
from gudhi.representations import BettiCurve

def diagram_gudhi_to_gtda(dgm):
    return np.array([[pt[0], pt[1], dim] for dim, pt in dgm])

def plot_diagram_gudhi(dgm):
    return plot_diagram(diagram_gudhi_to_gtda(dgm))

def plot_betti_curves_gudhi(dgm):
    dimensions = np.unique([d for d, _ in dgm])
    dgm_array = [
        np.array([pt for d, pt in dgm if (d==dim)&(np.isfinite(pt[1]))])
        for dim in dimensions
    ]
    BC = BettiCurve(resolution=300)

    bc = BC.fit_transform(dgm_array)
    bc[0, :] += 1.
    samplings = np.linspace(*BC.sample_range, BC.resolution)[None,:].repeat(len(dimensions), axis=0)
    return plot_betti_curves(bc, samplings)
