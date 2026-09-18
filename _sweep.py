from bot import config, backtest
config.prepare()
rcfg = config.risk_cfg()
candles = backtest.load_cached_candles(list(rcfg["pairs"]))

import itertools
results = []
for window_hours, entry_z, exit_z, stop_extra_z in itertools.product(
    [168, 240, 336], [2.0, 2.5, 3.0], [0.5, 1.0], [1.0, 1.5, 2.0]
):
    cfg = {
        "hypothesis": "PROTO", "strategy": "mean_reversion_stop",
        "params": {
            "window_hours": window_hours, "entry_z": entry_z, "exit_z": exit_z,
            "stop_extra_z": stop_extra_z, "vol_lookback_hours": 168,
            "target_vol_annual": 0.30, "max_weight": 0.25,
        }
    }
    try:
        m = backtest.run_backtest(candles, cfg, rcfg, max_days=365)
    except Exception as e:
        continue
    results.append((window_hours, entry_z, exit_z, stop_extra_z, m["gross_pnl"], m["cost_coverage"], m["max_drawdown"], m["n_trades"], m["trades_per_pair_per_day_max"]))

results.sort(key=lambda r: -r[4])
for r in results[:15]:
    print(r)
