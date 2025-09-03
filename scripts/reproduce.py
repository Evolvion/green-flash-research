import json, hashlib, time, pathlib
from greenflash.flash import delta_R_arcsec, tau_pred
from greenflash.sensors import detectability_thresholds

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()

def main(cfg):
    ΔR = delta_R_arcsec(cfg["lambda_green_nm"], cfg["lambda_red_nm"],
                        cfg["lambda_ref_nm"], cfg["R0_arcmin"])
    v_alt = 1920.0 / cfg["t_contact_s"]
    τ = tau_pred(ΔR, v_alt)
    th = detectability_thresholds(ΔR)
    res = {
        "delta_R_arcsec": ΔR,
        "v_alt_arcsec_per_s": v_alt,
        "tau_pred_s": τ,
        "detectability": th,
        "input": cfg,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    outdir = pathlib.Path("results"); outdir.mkdir(exist_ok=True)
    j = json.dumps(res, indent=2).encode()
    (outdir/"summary.json").write_bytes(j)

    art = {
      "id":"deltaR_tau_v1",
      "type":"result",
      "desc":"Predicted color separation and flash duration",
      "path":"results/summary.json",
      "sha256": sha256_bytes(j),
      "generated_in_round": 1,
      "inputs":["config/example.json"],
      "seed": 0,
      "software":{"python":"3.11","libs":{"pytest":"8.3.2"}},
      "commit_hint":"HEAD"
    }
    adir = pathlib.Path("artifacts"); adir.mkdir(exist_ok=True)
    (adir/"manifest.json").write_text(json.dumps([art], indent=2))
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    import argparse, json
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="config/example.json")
    a = p.parse_args()
    cfg = json.load(open(a.config))
    main(cfg)
