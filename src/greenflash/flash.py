from .refraction import n_air_edlen

def delta_R_arcsec(lambda_green_nm=546.1, lambda_red_nm=650.0,
                   lambda_ref_nm=589.3, R0_arcmin=35.4) -> float:
    n_g = n_air_edlen(lambda_green_nm) - 1.0
    n_r = n_air_edlen(lambda_red_nm) - 1.0
    n_0 = n_air_edlen(lambda_ref_nm) - 1.0
    return R0_arcmin*60.0 * ((n_g - n_r)/n_0)

def tau_pred(delta_R_arcsec_val: float, v_alt_arcsec_per_s: float) -> float:
    return delta_R_arcsec_val / v_alt_arcsec_per_s
