# Green Flash: bounds, estimator, and benchmark
This repo provides:
1) A mechanistic bound for green-rim separation ΔR from atmospheric dispersion.
2) A practical estimator for flash duration τ from video.
3) FlashBench, a minimal field benchmark schema.

## Quickstart
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
make reproduce
make paper    # requires tectonic or latexmk
```

## Reproduce
`make reproduce` regenerates `/results/summary.json` and `/artifacts/manifest.json` using `config/example.json`.

## Core formulas (standard air)
- ΔR ≈ R₀ · [(n(λg)−1)−(n(λr)−1)] / (n(λ₀)−1), λ₀=589.3 nm, R₀≈35.4′.
- v_alt ≈ 1920″ / t_contact.
- τ_pred ≈ ΔR / v_alt.

Necessary visibility condition: FWHM_system < ΔR.

**FlashBench fields:** lat, lon, UTC time, optics, pixel_scale, fps, t_contact, τ_meas, mirage_flag, radiosonde_id, video_sha256.
