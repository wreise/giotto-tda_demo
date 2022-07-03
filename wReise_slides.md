---
title:
- Point avancement
author:
- Wojciech Reise
place:
- Vernon
date:
- 17 Mars 2022
fontsize: 10pt
---


## A tutorial on persistent homoloy with GUDHI and giotto-tda

Persistent homology thoery has been shown a relevant tool, in both theoretical and applied settings.

There are numerous constructions, available in different librairies. The choice of which to use is dictated by the invariants to compute (Cech, homology, cohomology), the complexity of the available algorithms. In a statistical learning context where topology is used to extract features, there also come the issues of integration with other feature extraction methods, parameter selection and more generally, large-scale cross-validation.

The first part is tackled in the excellent paper (Roadmap to computing PH), but the landscape has since changed. First, with the appearance of giotto-tda, giotto-ph and the improvements over ripser.

In this talk, I would like to give a tutorial about two libraries: Gudhi and giotto-tda.

We will adopt a pragmatic perspective, where we try to put to use certain existing methods on concrete examples. The tutorial is made to demonstrate the flexibility of libraries and does not provide any relevant scientific advance in the field of inference or topological machine learning.

## Gudhi
most of it is in C++ and 

### References

## Giotto-tda

### Team
aaaa

### Pillars
**From Umbertos' slides**
- Seemless integration with ML frameworks: notion of a dataset; applying the transformer to a collection of point-clouds/graphs; specific treatment of diagrams by homology dimension.
- Code modularity: topological algorithms as scikit-learn transformers
- Standardisation: inclusion of most available and popular TDA techniques.
- Performance: relying on state-of-the-art implementations of persistent homology (giotto-ph, 

### Persistent homology pipeline
In the notebook; or maybe put this in the slide?



