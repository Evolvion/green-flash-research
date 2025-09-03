# Green Flash — External Review Brief

**Authors:** Jan Vorel  
**Date:** 2025-09-03  
**Version:** v0.1

## 1) Summary
Mechanistic bound for green–red rim separation `ΔR` from atmospheric dispersion. Practical estimator for flash duration `τ` from video. Minimal benchmark schema (FlashBench). Reproducible repo with tests and a paper build.

## 2) Claims to audit
- C1: `ΔR ≈ R0 * ((n(λg)−1)−(n(λr)−1)) / (n(λ0)−1)` with `R0 ≈ 35.4′`, `λ0=589.3 nm`.  
- C2: Using Edlén standard air: `ΔR(546.1 nm, 650 nm) ≈ 12″ ± 2″`.  
- C3: `τ ≈ ΔR / v_alt`, with `v_alt = 1920″ / t_contact`. For `t_contact = 180 s`, `τ ≈ 1.1 s`.  
- C4: Necessary visibility: `FWHM_system < ΔR`.  
- C5: Ratio-based `ΔR` is robust to density scaling; Edlén vs Ciddor drift ≤ 2%.

## 3) Assumptions
Clear horizon. Standard-air dispersion in the visible. Small-angle refraction scaling with refractivity `(n−1)`. Normal color vision. No strong mirage unless flagged.

## 4) Methods (audit targets)
**Derivation:** treat horizon refraction `R0` as scale; use dispersion ratio for color split.  
**Estimator:** measure `t_contact` from video; compute `v_alt`; estimate `τ = ΔR / v_alt`.  
**Instrument thresholds:** pixel scale `≤ ΔR/2` (~6″/px) and `fps ≥ 3/τ_pred`.  
**Benchmark:** FlashBench fields = `{lat, lon, UTC, optics, pixel_scale, fps, t_contact, τ_meas, mirage_flag, radiosonde_id, video_sha256}`.

## 5) Reproducibility
Repo layout provided. Expected commands:
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
make reproduce   # writes results/summary.json
make paper       # builds paper/preprint.pdf
pytest -q        # unit tests
```
**Expected numbers (default config):** `ΔR ≈ 12″`, `v_alt ≈ 10.7″/s`, `τ_pred ≈ 1.1 s`.

## 6) What to check (concrete)
- **Theory:** Recompute Edlén and Ciddor indices at 546.1, 589.3, 650 nm. Confirm C2 and C5.  
- **Scaling:** Verify density scaling cancels in the ratio.  
- **Estimator:** Validate `τ_pred` against videos with known `t_contact`.  
- **Thresholds:** Confirm detectability breakpoints near 6″/px and 30–120 fps.  
- **Edge cases:** Low latitude (high `v_alt`), layered inversions, ducting; report deviations.  
- **Numerics:** Unit tests bounds: `ΔR ∈ [8″,25″]`, `τ ∈ [0.5,2.0]` for `t_contact∈[120,300] s`.

## 7) Data request
Provide a short sunset/sunrise clip with EXIF. Include FlashBench CSV row. Flag mirage presence. Optional radiosonde ID.

## 8) Known limitations
Model isolates dispersion. Mirage geometry and temperature inversions can extend `τ`. Full ray-tracing is out of scope.

## 9) Acceptance criteria
All claims C1–C5 hold within stated tolerances. Repro build succeeds. At least two external datasets match `τ_pred` within 15% without mirage; with mirage, mismatch is documented.

## 10) References
- Edlén, *Metrologia* 1966.  
- Ciddor, *Applied Optics* 1996.  
- Bennett, *Journal of Navigation* 1982.  
- Young, “Sunset science. III. Visual adaptation and green flashes,” online notes.  
- Young, “Realistic green-flash simulations,” online notes.

## 11) How to respond
Open a review issue with: system, site, raw or link to video, FlashBench row, and findings. Or annotate this file and return diffs.
