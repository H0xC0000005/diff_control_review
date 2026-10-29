"""Exact algebra only: no traffic rollout, ODE solve, AD or numerical gradient."""

from pathlib import Path
import json
import sympy as sp


def main() -> None:
    identities: dict[str, bool] = {}
    static: dict[str, bool] = {}

    def identity(name: str, expression: sp.Expr) -> None:
        identities[name] = sp.simplify(expression) == 0

    w, K, u, ar, theta = sp.symbols('w K u ar theta', positive=True)
    R, m, c0, beta, a, p = sp.symbols('R m c0 beta a p', positive=True)
    v, h, ell, L, Lp, b, rho = sp.symbols('v h ell L Lp b rho', positive=True)
    t, x, z = sp.symbols('t x z', real=True)
    speed = sp.symbols('speed', positive=True)
    flow = sp.symbols('flow', positive=True)
    C = lambda s: K*s/(w+s)
    U = lambda g: w*g/(K-g)
    identity('fd_inverse', C(U(flow)) - flow)
    identity('fd_speed_derivative', sp.diff(C(speed), speed) - K*w/(w+speed)**2)
    S = sp.sqrt((w+u)**2 + 2*w*ar*theta)
    D = R - C(S-w)
    identity('profile_mark_derivative', sp.diff(D, u) + K*w*(w+u)/S**3)
    identity('profile_age_derivative', sp.diff(D, theta) + K*w*w*ar/S**3)
    ur, vv = sp.symbols('u_R V', positive=True)
    area = sp.integrate((K-C(ur))*(ur-vv)/(w*ar), (vv, u, ur))
    W0 = K/(w+ur)*ur**2/(2*ar)
    identity('isolated_loss_area', area - K/(w+ur)*(ur-u)**2/(2*ar))
    identity('zero_mark_area', area.subs(u, 0) - W0)
    identity('uniform_account_bound_scale', (R/c0)*W0/m - R*W0/(m*c0))

    fast = (R-a)/c0
    slow = (R-p-a)/(c0+beta)
    exact_difference = (beta*(R-a)+c0*p)/(c0*(c0+beta))
    bound = p/c0 + R*beta/c0**2
    identity('service_bracket_difference', fast-slow-exact_difference)
    identity('service_bound_nonnegative_remainder',
             bound-(fast-slow)-beta*(c0*p+R*beta+c0*a)/(c0**2*(c0+beta)))
    H = sp.symbols('H', positive=True)
    eps = sp.symbols('eps', positive=True)
    identity('uniform_queue_area_bound_integral', sp.integrate(t*eps, (t, 0, H))-H**2*eps/2)
    mass = sp.symbols('M', positive=True)
    identity('common_horizon_service_clearance',
             (c0+1)*mass/(R/2)-2*(c0+1)*mass/R)

    chi, g, ua = sp.symbols('chi g u_A', positive=True)
    root = g*(c0+chi*a*(ua-U(g)))
    Hg = c0+chi*a*(ua-U(g)-g*sp.diff(U(g),g))
    Ha = chi*g*(ua-U(g))
    Hu = chi*a*g
    identity('root_flow_partial', sp.diff(root,g)-Hg)
    identity('root_A_flow_partial', sp.diff(root,a)-Ha)
    identity('root_A_speed_partial', sp.diff(root,ua)-Hu)
    identity('queued_speed_derivative', sp.diff(U(g),g)-w*K/(K-g)**2)
    af, uf, gf, xf = [sp.Function(name)(v) for name in ['a','u','g','x']]
    composed = gf*(c0+chi*af*(uf-U(gf)))
    implicit = sp.solve(sp.diff(composed,v)-sp.diff(xf,v),sp.diff(gf,v))[0]
    expected = (sp.diff(xf,v)-Ha.subs({g:gf,a:af,ua:uf})*sp.diff(af,v)
                -Hu.subs({g:gf,a:af,ua:uf})*sp.diff(uf,v))/Hg.subs({g:gf,a:af,ua:uf})
    identity('implicit_root_chain_rule', implicit-expected)

    density = sp.Function('e')
    arrival_rate = v*density(v*t-b,v)
    # Independent argument symbols preserve a partial derivative when its
    # evaluated progress argument itself depends on the advice.
    independent_v = sp.symbols('independent_v')
    rate_chain = (density(v*t-b,v)
                  +v*sp.Subs(sp.diff(density(z,independent_v),independent_v),
                             (z,independent_v),(v*t-b,v))
                  +v*t*sp.Subs(sp.diff(density(z,independent_v),z),
                               (z,independent_v),(v*t-b,v)))
    identity('moving_arrival_rate_chain', (sp.diff(arrival_rate,v)-rate_chain).doit())
    cumulative = sp.Integral(density(Lp-x,v),(x,L-v*t,ell))
    cumulative_expected = sp.Integral(sp.diff(density(Lp-x,v),v),(x,L-v*t,ell))+t*density(Lp-L+v*t,v)
    identity('moving_arrival_count_leibniz', sp.diff(cumulative,v)-cumulative_expected)
    identity('front_time_derivative', sp.diff((L-ell)/v,v)+(L-ell)/v**2)
    identity('rear_time_derivative', sp.diff(L/v,v)+L/v**2)
    baseline = sp.integrate(rho*(L-x)/v,(x,0,ell))
    identity('uniform_initial_remaining_travel', baseline-rho*ell*(L-ell/2)/v)
    identity('baseline_advice_derivative', sp.diff(baseline,v)+rho*ell*(L-ell/2)/v**2)

    go, Zt, Zo, Do = sp.symbols('g_old Z_t Z_old D_old', nonzero=True)
    identity('rank_cutoff_rate_cancellation', -Do*go*(Zt-Zo)/go+Do*(Zt-Zo))
    aa, bb, cc, cutoff, event = [sp.Function(name)(v) for name in ['A','B','C','cutoff','tau']]
    s = sp.symbols('s',real=True)
    left, right = aa*s+bb, cc*s**2
    split_integral = sp.integrate(left,(s,cutoff,event))+sp.integrate(right,(s,event,t))
    split_derivative = (sp.integrate(sp.diff(left,v),(s,cutoff,event))
                        +sp.integrate(sp.diff(right,v),(s,event,t))
                        +(left.subs(s,event)-right.subs(s,event))*sp.diff(event,v)
                        -left.subs(s,cutoff)*sp.diff(cutoff,v))
    identity('history_event_and_cutoff_leibniz', sp.diff(split_integral,v)-split_derivative)
    fm, fp, end = sp.symbols('F_minus F_plus end',nonzero=True)
    guard_level = sp.Function('guard_level')(v)
    tau = guard_level/fm
    endpoint = guard_level+fp*(end-tau)
    identity('identity_reset_event_timing', sp.diff(endpoint,v)-(fm-fp)*sp.diff(tau,v))
    qa, qb = sp.Function('qa')(v), sp.Function('qb')(v)
    queue_curve = (t-qa)*(qb-t)
    queue_area = sp.integrate(queue_curve,(t,qa,qb))
    identity('zero_queue_endpoint_area_terms', sp.diff(queue_area,v)-sp.integrate(sp.diff(queue_curve,v),(t,qa,qb)))

    # Recheck the reused exact H1/H1-T1 identities independently of any rollout.
    kappa, pastu = sp.symbols('kappa pastu',positive=True)
    delta = 6*kappa*pastu/(2*pastu+v)-19*kappa/20
    efh = (7*kappa/10+delta)**2/(8*delta)
    identity('high_front_density', efh.subs(v,2*pastu)-125*kappa/352)
    identity('high_front_advice_derivative', sp.diff(efh,v).subs(v,2*pastu)-225*kappa/(7744*pastu))
    d0, pulse, forced, pulse_moment, base = sp.symbols('D0 duration Ebar moment base', real=True)
    original = base+d0*pulse/(2*c0)+(1-1/c0)*pulse_moment/v+(d0+(c0-1)*forced)**2/(2*c0*R)
    I0 = base+pulse_moment/v+(d0-forced)*forced/R
    I1 = d0*pulse/2-pulse_moment/v+(d0-forced)**2/(2*R)
    identity('archived_complete_objective_expansion',original-(c0*forced**2/(2*R)+I0+I1/c0))

    f = sp.Rational
    values = {
        'same_total_density': f(3,5)+2*f(3,10)==f(7,10)+2*f(1,4)==f(6,5),
        'same_aggregate_prefix_recipe': f(9,10)+f(3,10)==f(19,20)+f(1,4),
        'high_pair_initial_below_fast_critical': f(19,20)<f(3,2),
        'ordinary_high_pair_margin': f(39,20)-2*f(19,20)==f(1,20)>0,
        'ordinary_low_pair_margin': f(39,20)-2*f(9,10)==f(3,20)>0,
        'downstream_capacity_admission': f(39,20)<2,
        'far_lane_capacity_admission': 2*f(3,10)<=1<=2,
        'finite_storage_fraction': f(6,5)/3==f(2,5)<1,
        'loading_nonnegative_high': f(7,10)*f(4,3)<f(19,20),
        'loading_nonnegative_low': f(3,5)*f(4,3)<f(9,10),
        'loading_donor_work_bound': f(19,20)+f(14,15)==f(113,60)<2,
        'high_switch_before_front': f(25,22)**2<2,
        'exact_positive_maneuver_negative_threshold':
            f(19,10)+f(125,176)*f(44,625)==f(39,20),
        'low_free_at_high_negative_threshold':
            f(9,5)+f(3,5)*f(44,625)<f(39,20),
        'nonzero_negative_interval': f(44,625)>0,
        'sustained_queue_sufficient_threshold':
            f(9,10)+(f(17,3)-1)*f(9,40)==f(39,20),
        'positive_preparation_advice_sensitivity': f(225,7744)>0,
    }
    static.update({name:bool(value) for name,value in values.items()})
    failures = [name for name,okay in {**identities,**static}.items() if not okay]
    result = {
        'scope':'Exact symbolic identities and static rational checks only; no traffic/ODE/AD/finite-difference experiment',
        'sympy_version':sp.__version__,
        'passed':not failures,
        'symbolic_identity_count':len(identities),
        'static_check_count':len(static),
        'symbolic_identities':identities,
        'static_checks':static,
        'failures':failures,
        'limits':'Checks support algebra, not independent machine certification of comparison proofs, hybrid regularity, empirical validity or numerical gradients.',
    }
    out=Path(__file__).with_name('vsl_step3_standalone_symbolic_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['passed','sympy_version','symbolic_identity_count','static_check_count','failures']},indent=2))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
