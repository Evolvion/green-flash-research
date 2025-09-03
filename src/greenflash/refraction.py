# Edlén 1966 standard-air dispersion for visible wavelengths.
# (n-1)*1e8 = 8342.13 + 2406030/(130 - σ^2) + 15997/(38.9 - σ^2), σ in μm^-1
def n_air_edlen(lambda_nm: float) -> float:
    lam_um = lambda_nm/1000.0
    sigma = 1.0/lam_um
    N = 8342.13 + 2406030.0/(130.0 - sigma**2) + 15997.0/(38.9 - sigma**2)
    return 1.0 + N*1e-8
