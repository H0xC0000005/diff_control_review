"""Exact rechecks of accepted AS1/AS2/AS3 witness admission, without rollout.

Speeds, densities and lengths below are normalized by the arbitrary positive
u, kappa and ell in the existing analytical family. Only static identities
and inequalities are checked. No traffic, ODE, numerical gradient or
optimization calculation is performed, and no model parameter is selected.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def main() -> None:
    checks: list[dict[str, str | bool]] = []

    def check(name: str, condition: bool, value: F | str) -> None:
        assert condition, name
        checks.append({"name": name, "passed": True, "exact_value": str(value)})

    v_lo, v_hi, wave, jam = F(1), F(2), F(2), F(3)
    receiving, far_receiving = F(39, 20), F(1)
    ending = F(3, 5)
    low_a, high_a = F(1, 5), F(7, 20)
    low_b, high_b = high_a, low_a
    gamma, base_work, beta = F(2), F(11, 10), F(1, 100)
    footprint, prep_length, terminal_length = F(1), F(2), F(1)
    k_wave = wave * jam

    def capacity(speed: F) -> F:
        return k_wave * speed / (wave + speed)

    def critical(speed: F) -> F:
        return k_wave / (wave + speed)

    total_low = footprint * (ending + low_a + low_b)
    total_high = footprint * (ending + high_a + high_b)
    r_low, r_high = ending + low_a, ending + high_a
    check("positive_speed_interval", 0 < v_lo < v_hi, "[1, 2]")
    check("capacity_endpoint_order", capacity(v_hi) > capacity(v_lo), capacity(v_hi) - capacity(v_lo))
    check("critical_density_endpoint_order", critical(v_hi) < critical(v_lo), critical(v_lo) - critical(v_hi))
    check("fixed_ending_and_continuing_total", low_a + low_b == high_a + high_b == F(11, 20), low_a + low_b)
    check("genuine_adjacent_imbalance", low_a != high_a and low_b != high_b, high_a - low_a)
    check("actual_total_mass_equal", total_low == total_high == F(23, 20), total_low)
    check("independent_EA_loads", r_low == F(4, 5) and r_high == F(19, 20), r_high - r_low)
    check("ending_initial_free", 0 < ending <= critical(v_hi), critical(v_hi) - ending)
    check("all_continuing_initial_free", 0 < min(low_a, high_a, low_b, high_b) <= max(low_a, high_a, low_b, high_b) <= critical(v_hi), critical(v_hi) - max(low_a, high_a))
    ordinary_margin = receiving - v_hi * max(r_low, r_high)
    check("ordinary_EA_underload_at_worst_endpoint", ordinary_margin == F(1, 20) > 0, ordinary_margin)
    check("receiving_feasible_at_lowest_advice", receiving <= capacity(v_lo), capacity(v_lo) - receiving)
    check("EA_free_headroom_at_highest_advice", max(r_low, r_high) < critical(v_hi), critical(v_hi) - r_high)
    far_margin = far_receiving - v_hi * max(low_b, high_b)
    check("far_lane_service_margin", far_margin == F(3, 10) > 0, far_margin)
    check("far_service_feasible_at_lowest_advice", far_receiving <= capacity(v_lo), capacity(v_lo) - far_receiving)
    storage_ratio = total_low / (jam * terminal_length)
    check("total_mass_storage_margin", storage_ratio == F(23, 60) < 1, storage_ratio)
    check("finite_footprint_inside_preparation", 0 < footprint < prep_length, prep_length - footprint)
    check("preparation_penalty_domain", gamma >= 1, gamma)
    eta = base_work - beta * (1 + v_hi / wave)
    check("strict_service_root_margin", eta == F(27, 25) > 0, eta)
    chi = beta / (capacity(v_hi) * v_hi)
    check("fixed_physical_anchor_value", chi == F(1, 600), chi)

    donor = v_hi * ending
    receive_low = (capacity(v_hi) - v_hi * low_a) / gamma
    receive_high = (capacity(v_hi) - v_hi * high_a) / gamma
    check("common_initial_donor_offer", donor == F(6, 5), donor)
    check("lower_A_donor_limited", receive_low == F(13, 10) > donor, receive_low)
    check("higher_A_receiving_limited", receive_high == F(23, 20) < donor, receive_high)
    check("distinct_selected_transfer", min(donor, receive_low) > min(donor, receive_high), min(donor, receive_low) - min(donor, receive_high))

    # Accepted specialization exp(ell/h)=6/5; no trajectory is evaluated.
    exposure_factor = F(6, 5)
    earliest_e = ending * exposure_factor
    minimum_a_in = r_low - earliest_e
    worst_donor_density = r_high + (gamma - 1) * earliest_e
    check("loader_earliest_E", earliest_e == F(18, 25), earliest_e)
    check("loader_positive_A_input", minimum_a_in == F(2, 25) > 0, minimum_a_in)
    check("loader_donor_margin", worst_donor_density == F(167, 100) < critical(v_lo), critical(v_lo) - worst_donor_density)
    check("loader_exposure_inside_accepted_interval", 1 < exposure_factor < F(4, 3), F(4, 3) - exposure_factor)
    check("AS3_switch_before_first_exposure", F(23, 22) ** 2 < exposure_factor, exposure_factor - F(23, 22) ** 2)

    # Separate AS3 common-fastest work range, not AS1's illustrative cost.
    delta_end = F(132, 2645)
    front_high = F(19, 10) + F(529, 528) * delta_end
    front_low = F(8, 5) + delta_end
    check("common_fastest_interval_nonzero", delta_end > 0, delta_end)
    check("common_fastest_high_A_boundary", front_high == receiving, front_high)
    check("common_fastest_low_A_fits", front_low < receiving, receiving - front_low)

    result = {
        "status": "passed",
        "scope": "Exact static rechecks of already accepted analytical families",
        "source_family": [
            "vsl_as1_asymmetric_forward_contract.tex, Section 5",
            "vsl_as2_information_and_history.tex, Section 2",
            "vsl_as3_asymmetric_actions_and_gradients.tex, Sections 2-3",
        ],
        "arithmetic": "Python standard-library fractions.Fraction",
        "normalization": "arbitrary positive u, kappa and ell; not calibrated task values",
        "check_count": len(checks),
        "checks": checks,
        "traffic_rollout_or_ODE": False,
        "numerical_gradient_or_optimization": False,
        "whole_proof_machine_verified": False,
        "physical_admission": False,
    }
    output = Path(__file__).with_name("vsl_global_assumptions_static_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"{len(checks)} exact static checks passed; results: {output.name}")


if __name__ == "__main__":
    main()
