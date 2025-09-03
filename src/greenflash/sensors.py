def detectability_thresholds(delta_R_arcsec: float):
    return {
        "required_pixel_scale_arcsec_per_px": delta_R_arcsec/2.0,
        "recommended_fps_min": max(30, int(3.0/(delta_R_arcsec/10.0))+1)
    }
