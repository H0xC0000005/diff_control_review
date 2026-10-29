"""AS1 exact algebra and rational domain checks; no traffic evolution is run.

This review utility performs no time stepping, ODE solve, AD, numerical
gradient, calibration or optimization. The causal proof is a human-reviewed
mathematical dependency argument, not certified by these algebra checks.
"""

from pathlib import Path
import json
import sympy as sp


def main() -> None:
    identities: dict[str, bool] = {}
    static: dict[str, bool] = {}

    def identity(name: str, expression: sp.Expr) -> None:
        identities[name] = bool(sp.simplify(expression) == 0)

    e, a, far, f, h, v, s = sp.symbols('e a b0 f h v s', positive=True)
    e0, a0, b0, ell, d, cont = sp.symbols('e0 a0 b0 ell d cont', real=True)
    rho = e0 + a0 + b0
    identity('independent_initial_total', ell*rho - ell*(e0+a0) - ell*b0)
    FE, FA, FB, Jlat = sp.symbols('F_E F_A F_B J_lat', real=True)
    state = sp.Matrix([s,e,a,far,FE,FA,FB,Jlat])
    before = sp.Matrix([0,-f/h,f/h,0,0,0,0,s*f/h])
    during = sp.Matrix([-v,-f/h,f/h,0,v*e,v*a,v*far,s*f/h])
    def along(expression: sp.Expr, rhs: sp.Matrix) -> sp.Expr:
        return (sp.Matrix([expression]).jacobian(state)*rhs)[0]
    identity('paired_transfer_conserves_E_A', along(e+a,before))
    identity('prep_E_balance_before_front', along(s*e+FE+Jlat,before))
    identity('prep_A_balance_before_front', along(s*a+FA-Jlat,before))
    identity('prep_E_balance_during_pulse', along(s*e+FE+Jlat,during))
    identity('prep_A_balance_during_pulse', along(s*a+FA-Jlat,during))
    identity('prep_B_balance_during_pulse', along(s*far+FB,during))
    identity('prep_total_balance_during_pulse', along(s*(e+a+far)+FE+FA+FB,during))
    identity('old_symmetric_total_error', ell*(e0+2*a0)-ell*rho-ell*(a0-b0))
    identity('fixed_E_continuing_total', (cont/2+d)+(cont/2-d)-cont)
    identity('fixed_total_mass_under_split', ell*(e0+cont/2+d+cont/2-d)-ell*(e0+cont))
    identity('varying_E_A_load', (e0+cont/2+d)-(e0+cont/2)-d)

    z, zs, es, delta, gamma = sp.symbols('z zs es Delta gamma', positive=True)
    donor = es*sp.exp(-(z-zs)/h)
    receiving = (es+delta)*sp.exp(-(z-zs)/(gamma*h))-delta
    identity('donor_progress_solution', sp.diff(donor,z)+donor/h)
    identity('receiving_progress_solution', sp.diff(receiving,z)+(delta+receiving)/(gamma*h))
    identity('branch_threshold_agreement', (delta+delta/(gamma-1))/gamma-delta/(gamma-1))
    identity('A_E_offer_sum', v*(a+e)-v*a-v*e)
    identity('arrival_A_increase_rate', along(v*a,before)-v*f/h)

    K, w, speed, flow = sp.symbols('K w speed flow', positive=True)
    C = lambda u: K*u/(w+u)
    U = lambda g: w*g/(K-g)
    identity('flow_speed_inverse', C(U(flow))-flow)
    identity('capacity_increases_with_advice', sp.diff(C(speed),speed)-K*w/(w+speed)**2)
    identity('critical_density_decreases_with_advice', sp.diff(K/(w+speed),speed)+K/(w+speed)**2)
    L, x = sp.symbols('L x', positive=True)
    travel = sp.integrate(rho*(L-x)/v,(x,0,ell))
    identity('three_lane_remaining_travel', travel-ell*rho*(L-ell/2)/v)

    # Normalize density by kappa, speed by u, and flow by kappa*u.
    # Interval endpoints suffice for the affine load/positivity restrictions;
    # capacity monotonicity handles the whole advice interval analytically.
    q = sp.Rational
    ehat, chat = q(3,5), q(11,20)
    alow, ahigh = q(1,5), q(7,20)
    blow, bhigh = ahigh, alow
    rlow, rhigh = ehat+alow, ehat+ahigh
    Rhat, RBhat = q(39,20), sp.Integer(1)
    kcfast, Cslow, Cfast = q(3,2), sp.Integer(2), sp.Integer(3)
    c0, beta = q(11,10), q(1,100)
    eta = c0-beta*(1+q(2,2))
    offer = 2*ehat
    receivelow = (Cfast-2*alow)/2
    receivehigh = (Cfast-2*ahigh)/2
    checks = {
        'distinct_positive_swapped_A_B': 0<alow<ahigh and blow==ahigh and bhigh==alow,
        'same_E_and_continuing_total': alow+blow==ahigh+bhigh==chat,
        'same_true_three_lane_density': ehat+chat==q(23,20),
        'all_initial_lane_densities_free': max(ehat,ahigh,blow)<kcfast,
        'whole_split_interval_positive': q(11,40)-q(3,40)==alow>0,
        'whole_split_interval_upper_endpoint': q(11,40)+q(3,40)==ahigh,
        'E_A_load_range': rlow==q(4,5) and rhigh==q(19,20),
        'worst_ordinary_E_A_margin': Rhat-2*rhigh==q(1,20)>0,
        'shared_service_below_slowest_capacity': Rhat<Cslow,
        'worst_far_lane_margin': RBhat-2*blow==q(3,10)>0,
        'far_service_below_slowest_capacity': RBhat<=Cslow,
        'true_total_storage_fraction': (ehat+chat)/3==q(23,60)<1,
        'root_monotonicity_margin': eta==q(27,25)>0,
        'same_donor_offer': offer==q(6,5),
        'less_crowded_A_donor_limited': receivelow==q(13,10)>offer,
        'more_crowded_A_receiving_limited': receivehigh==q(23,20)<offer,
        'strict_local_transfer_difference': min(offer,receivelow)-min(offer,receivehigh)==q(1,20)>0,
        'old_total_understates_first_member': ehat+2*alow-(ehat+chat)==-q(3,20),
        'old_total_overstates_second_member': ehat+2*ahigh-(ehat+chat)==q(3,20),
    }
    static.update({name:bool(value) for name,value in checks.items()})
    failures=[name for name,okay in {**identities,**static}.items() if not okay]
    result={
        'date':'2026-10-19',
        'scope':'Exact symbolic identities and static rational inequalities only; no traffic evolution or numerical experiment',
        'sympy_version':sp.__version__,
        'passed':not failures,
        'symbolic_identity_count':len(identities),
        'static_check_count':len(static),
        'symbolic_identities':identities,
        'static_checks':static,
        'failures':failures,
        'limits':'Algebra checks do not certify the full causal theorem, empirical admission, observation equivalence, action differences or gradients.',
    }
    Path(__file__).with_name('vsl_as1_symbolic_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['passed','sympy_version','symbolic_identity_count','static_check_count','failures']},indent=2))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
