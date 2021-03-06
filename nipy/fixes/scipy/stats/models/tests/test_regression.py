# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Test functions for models.regression
"""

from numpy.random import standard_normal
from numpy.testing import *

from nipy.fixes.scipy.stats.models.regression import OLSModel, ARModel

W = standard_normal

class TestRegression(TestCase):

    def testOLS(self):
        X = W((40,10))
        Y = W((40,))
        model = OLSModel(design=X)
        results = model.fit(Y)
        self.assertEquals(results.df_resid, 30)

    def testAR(self):
        X = W((40,10))
        Y = W((40,))
        model = ARModel(design=X, rho=0.4)
        results = model.fit(Y)
        self.assertEquals(results.df_resid, 30)

    def testOLSdegenerate(self):
        X = W((40,10))
        X[:,0] = X[:,1] + X[:,2]
        Y = W((40,))
        model = OLSModel(design=X)
        results = model.fit(Y)
        self.assertEquals(results.df_resid, 31)

    def testARdegenerate(self):
        X = W((40,10))
        X[:,0] = X[:,1] + X[:,2]
        Y = W((40,))
        model = ARModel(design=X, rho=0.9)
        results = model.fit(Y)
        self.assertEquals(results.df_resid, 31)



