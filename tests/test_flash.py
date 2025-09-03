from greenflash.flash import delta_R_arcsec, tau_pred

def test_deltaR_range():
    d = delta_R_arcsec()
    assert 8.0 <= d <= 25.0

def test_tau_example():
    v = 1920.0/180.0
    τ = tau_pred(delta_R_arcsec(), v)
    assert 0.5 <= τ <= 2.0
